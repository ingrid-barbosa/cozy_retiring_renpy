init python in cozy_radio_estado:
    import atexit
    import os
    import shutil
    import socket
    import tempfile
    from urllib.error import HTTPError, URLError
    import cozy_radio

    try:
        import ssl
    except ImportError:
        ssl = None

    pasta = None
    faixas = []
    tocando = None
    ocupado = False
    request_number = 0
    aviso = "Search Jamendo or play the local soundtrack."

    def preparar_pasta():
        global pasta
        if pasta is None:
            pasta = tempfile.mkdtemp(prefix="cozy_radio_")
            renpy.config.searchpath.append(pasta)
            atexit.register(shutil.rmtree, pasta, ignore_errors=True)
        return pasta

    def tocar_local(mensagem="Playing the local soundtrack.", filename=None):
        global tocando, aviso
        if filename is None:
            tracks = renpy.store.local_story_tracks("neutral", "neutral")
            filename = renpy.store.select_story_track(tracks)
        if not filename or not renpy.loadable(filename):
            aviso = "No local track is available."
            return
        renpy.music.play(filename, channel="radio_preview", loop=True, fadeout=0.5, fadein=0.5)
        title = filename.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        tocando, aviso = {"name": title, "album_name": "Local soundtrack"}, mensagem

    def parar():
        global tocando, aviso
        renpy.music.stop(channel="radio_preview", fadeout=0.3)
        tocando, aviso = None, "Playback stopped."

    def close_radio():
        global ocupado, request_number
        request_number += 1
        ocupado = False
        parar()

    def entregar(request, tipo, resultado, erro):
        global ocupado, faixas, tocando, aviso
        if request != request_number:
            return
        ocupado = False
        if erro:
            if tipo == "busca":
                faixas = []
            aviso = erro
        elif tipo == "busca":
            faixas = resultado
            if faixas:
                aviso = "{} online results. Select a playable track to listen.".format(len(faixas))
            else:
                aviso = "Jamendo returned no results. Try a different search."
        else:
            faixa, nome = resultado
            try:
                renpy.music.play(nome, channel="radio_preview", loop=True)
                tocando, aviso = faixa, "Playing the selected track."
            except Exception:
                aviso = "Could not play the selected Jamendo track."
        renpy.restart_interaction()

    def connection_error(error, tipo):
        reason = error.reason if isinstance(error, URLError) else error
        if ssl is not None and isinstance(reason, ssl.SSLCertVerificationError):
            return "Ren'Py could not verify Jamendo's HTTPS certificate (code {}).".format(reason.verify_code)
        if ssl is not None and isinstance(reason, ssl.SSLError):
            return "The HTTPS handshake with Jamendo failed ({}).".format(reason.reason or "TLS error")
        if isinstance(reason, socket.gaierror):
            return "Ren'Py could not resolve Jamendo's address (DNS error {}).".format(reason.errno)
        if isinstance(reason, TimeoutError):
            return "The request to Jamendo timed out."
        if reason == "unknown url type: https":
            return "This Ren'Py installation does not support HTTPS requests."
        if isinstance(reason, OSError):
            code = getattr(reason, "winerror", None) or reason.errno
            if not isinstance(error, URLError) and reason.filename and tipo == "audio":
                return "Could not save the downloaded track (system error {}).".format(code or "unknown")
            if code is not None:
                return "The connection to Jamendo failed (system error {}).".format(code)
        return "Ren'Py could not open a connection to Jamendo ({}).".format(type(reason).__name__)

    def iniciar(tipo, tarefa):
        global ocupado, aviso, request_number
        if ocupado:
            return
        if renpy.emscripten:
            aviso = "Online radio is available in the desktop version."
            return
        ocupado, aviso = True, "Loading…"

        request_number += 1
        request = request_number

        def executar():
            try:
                resultado = tarefa()
            except ValueError as erro:
                mensagem = str(erro)
                if isinstance(erro, cozy_radio.json.JSONDecodeError):
                    mensagem = "The radio response could not be read."
                renpy.invoke_in_main_thread(entregar, request, tipo, None, mensagem)
            except HTTPError as erro:
                mensagem = "Jamendo returned HTTP {}.".format(erro.code)
                renpy.invoke_in_main_thread(entregar, request, tipo, None, mensagem)
            except OSError as erro:
                renpy.invoke_in_main_thread(entregar, request, tipo, None, connection_error(erro, tipo))
            except Exception:
                renpy.invoke_in_main_thread(entregar, request, tipo, None, "An error occurred in the radio.")
            else:
                renpy.invoke_in_main_thread(entregar, request, tipo, resultado, None)

        renpy.invoke_in_thread(executar)

    def configured_client_id():
        return os.environ.get("JAMENDO_CLIENT_ID", "").strip() or "812ed4dd"

    def buscar(busca, client_id):
        global aviso, faixas
        faixas = []
        if not client_id.strip():
            aviso = "Enter a Jamendo Client ID before searching."
            return
        if not busca.strip():
            aviso = "Enter a track, artist, or genre to search for."
            return
        iniciar("busca", lambda: cozy_radio.consultar(client_id.strip(), busca.strip()))

    def ouvir(faixa):
        global aviso
        def tarefa():
            return faixa, cozy_radio.baixar(faixa, destino)
        if renpy.emscripten:
            aviso = "Online radio is available in the desktop version."
            return
        try:
            destino = preparar_pasta()
        except OSError:
            aviso = "Could not prepare the Jamendo audio for playback."
            return
        iniciar("audio", tarefa)

init python in cozy_jamendo_ambience:
    import time
    import cozy_radio

    _constant = True
    filename = None
    loading = False
    retry_at = 0.0

    def receive(downloaded, error):
        global filename, loading, retry_at
        filename = downloaded
        loading = False
        if error:
            retry_at = time.monotonic() + 60
            renpy.log("Jamendo ambience: " + error)

    def update():
        global loading
        if renpy.emscripten:
            return
        if filename:
            if renpy.music.get_playing(channel="jamendo_ambience") != filename:
                renpy.music.play(filename, channel="jamendo_ambience", loop=True,
                                 fadein=1.0, if_changed=True, relative_volume=0.25)
            return
        if loading or time.monotonic() < retry_at:
            return

        radio = renpy.store.cozy_radio_estado
        client_id = radio.configured_client_id()
        try:
            destination = radio.preparar_pasta()
        except OSError as error:
            receive(None, type(error).__name__)
            return

        def download():
            try:
                track = cozy_radio.buscar_birdstrem(client_id)
                downloaded = cozy_radio.baixar(track, destination)
            except ValueError as error:
                renpy.invoke_in_main_thread(receive, None, str(error))
            except OSError as error:
                renpy.invoke_in_main_thread(receive, None, radio.connection_error(error, "audio"))
            except Exception as error:
                renpy.invoke_in_main_thread(receive, None, type(error).__name__)
            else:
                renpy.invoke_in_main_thread(receive, downloaded, None)

        loading = True
        renpy.invoke_in_thread(download)

screen cozy_radio_tela():
    tag menu
    default busca = "relaxation"
    default client_id = cozy_radio_estado.configured_client_id()
    on "hide" action Function(cozy_radio_estado.close_radio, _update_screens=False)
    on "replaced" action Function(cozy_radio_estado.close_radio, _update_screens=False)

    use game_menu(_("Jamendo Radio"), scroll="viewport"):
        vbox:
            style_prefix "book_radio"
            spacing 18

            text _("Jamendo Client ID") size 29
            $ client_id_input = ScreenVariableInputValue("client_id", default=False)
            textbutton _("Edit Client ID") action client_id_input.Enable()
            frame:
                xfill True
                padding (20, 12)
                input value client_id_input length 60 size 30

            text _("Search by track, artist, or genre") size 29
            $ search_input = ScreenVariableInputValue("busca")
            textbutton _("Edit search") action search_input.Enable()
            frame:
                xfill True
                padding (20, 12)
                input value search_input length 60 size 30

            hbox:
                spacing 24
                textbutton _("Search online") action Function(cozy_radio_estado.buscar, busca, client_id) sensitive (not cozy_radio_estado.ocupado)
                textbutton _("Local soundtrack") action Function(cozy_radio_estado.tocar_local) sensitive (not cozy_radio_estado.ocupado)
                textbutton _("Stop") action Function(cozy_radio_estado.parar) sensitive (not cozy_radio_estado.ocupado and cozy_radio_estado.tocando is not None)

            text cozy_radio_estado.aviso size 27 substitute False

            if cozy_radio_estado.tocando:
                $ faixa_atual = cozy_radio_estado.tocando
                $ titulo_atual = "{} — {}".format(faixa_atual.get("name", ""), faixa_atual.get("artist_name", ""))
                $ detalhes = "Album: {}  |  License: {}".format(faixa_atual.get("album_name") or "Independent track", faixa_atual.get("license_ccurl") or ("See Jamendo" if faixa_atual.get("id") else "Not listed"))
                text titulo_atual size 32 substitute False
                text detalhes size 23 substitute False

            if cozy_radio_estado.faixas:
                label _("Jamendo results")
            for faixa in cozy_radio_estado.faixas:
                $ rotulo = "{} — {}".format(faixa.get("name", ""), faixa.get("artist_name", ""))
                if cozy_radio_estado.cozy_radio.pode_baixar(faixa):
                    button:
                        action Function(cozy_radio_estado.ouvir, faixa)
                        sensitive not cozy_radio_estado.ocupado
                        text rotulo substitute False
                else:
                    text rotulo substitute False
                    text _("Unavailable for in-game download") size 22

            label _("Local tracks")
            for group in ("seasonal", "neutral", "dark"):
                label group.title()
                for filename in local_story_tracks(group, ""):
                    $ local_title = filename.rsplit("/", 1)[-1].rsplit(".", 1)[0].title()
                    textbutton local_title action Function(cozy_radio_estado.tocar_local, filename=filename) sensitive (not cozy_radio_estado.ocupado)

style book_radio_text is gui_text:
    color "#49262c"

style book_radio_label_text is gui_label_text:
    color "#632f3c"

style book_radio_button is button
style book_radio_button_text is button_text:
    color "#59434a"
    hover_color "#8c3048"
    selected_color "#8c3048"
    insensitive_color "#897475"

style book_radio_input is input:
    color "#49262c"

style book_radio_frame is frame:
    background Solid("#eee0d2")
