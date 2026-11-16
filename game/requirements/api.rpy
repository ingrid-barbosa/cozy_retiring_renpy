init python in cozy_radio_estado:
    import atexit
    import os
    import shutil
    import tempfile
    import cozy_radio

    pasta = None
    faixas = []
    tocando = None
    ocupado = False
    aviso = "Busque na Jamendo ou toque a trilha local."

    local = {
        "name": "Brisa do bosque",
        "artist_name": "Trilha procedural do projeto",
        "license_ccurl": "CC0"
    }

    def preparar_pasta():
        global pasta
        if pasta is None:
            pasta = tempfile.mkdtemp(prefix="cozy_radio_")
            renpy.config.searchpath.append(pasta)
            atexit.register(shutil.rmtree, pasta, ignore_errors=True)
        return pasta

    def tocar_local(mensagem="Tocando a trilha local."):
        global tocando, aviso
        renpy.music.play("audio/brisa.wav", channel="music", loop=True)
        tocando, aviso = local, mensagem

    def parar():
        global tocando, aviso
        renpy.music.stop(channel="music", fadeout=0.3)
        tocando, aviso = None, "Reprodução interrompida."

    def entregar(tipo, resultado, erro):
        global ocupado, faixas, tocando, aviso
        ocupado = False
        if erro:
            if tipo == "busca":
                faixas = []
            tocar_local(erro + " Tocando a trilha local.")
        elif tipo == "busca":
            faixas = resultado
            if faixas:
                aviso = "Selecione uma faixa para ouvir."
            else:
                tocar_local("Nenhuma faixa disponível para reprodução. Tocando a trilha local.")
        else:
            faixa, nome = resultado
            try:
                renpy.music.play(nome, channel="music", loop=True)
                tocando, aviso = faixa, "Tocando a faixa selecionada."
            except Exception:
                tocar_local("Falha ao reproduzir. Tocando a trilha local.")
        renpy.restart_interaction()

    def iniciar(tipo, tarefa):
        global ocupado, aviso
        if ocupado:
            return
        if renpy.emscripten:
            tocar_local("A rádio online está disponível na versão de desktop.")
            return
        ocupado, aviso = True, "Carregando…"

        def executar():
            try:
                resultado = tarefa()
            except ValueError as erro:
                mensagem = str(erro)
                if isinstance(erro, cozy_radio.json.JSONDecodeError):
                    mensagem = "A resposta da rádio não pôde ser lida."
                renpy.invoke_in_main_thread(entregar, tipo, None, mensagem)
            except (OSError, TimeoutError):
                renpy.invoke_in_main_thread(entregar, tipo, None, "Falha de conexão ou acesso ao áudio.")
            except Exception:
                renpy.invoke_in_main_thread(entregar, tipo, None, "A rádio encontrou um erro.")
            else:
                renpy.invoke_in_main_thread(entregar, tipo, resultado, None)

        renpy.invoke_in_thread(executar)

    def buscar(busca):
        client_id = os.environ.get("JAMENDO_CLIENT_ID", "").strip()
        iniciar("busca", lambda: cozy_radio.consultar(client_id, busca.strip()))

    def ouvir(faixa):
        def tarefa():
            return faixa, cozy_radio.baixar(faixa, destino)
        if renpy.emscripten:
            tocar_local("A rádio online está disponível na versão de desktop.")
            return
        try:
            destino = preparar_pasta()
        except OSError:
            tocar_local("Não foi possível preparar o áudio. Tocando a trilha local.")
            return
        iniciar("audio", tarefa)

screen cozy_radio_tela():
    tag menu
    default busca = "relaxation"

    use game_menu(_("Rádio Jamendo"), scroll="viewport"):
        vbox:
            spacing 18

            text _("Busca por faixa, artista ou gênero") size 29
            frame:
                xfill True
                padding (20, 12)
                input value ScreenVariableInputValue("busca") length 60 size 30

            hbox:
                spacing 24
                textbutton _("Buscar") action Function(cozy_radio_estado.buscar, busca) sensitive (not cozy_radio_estado.ocupado)
                textbutton _("Trilha local") action Function(cozy_radio_estado.tocar_local) sensitive (not cozy_radio_estado.ocupado)
                textbutton _("Parar") action Function(cozy_radio_estado.parar) sensitive (not cozy_radio_estado.ocupado and cozy_radio_estado.tocando is not None)

            text cozy_radio_estado.aviso size 27 substitute False

            if cozy_radio_estado.tocando:
                $ faixa_atual = cozy_radio_estado.tocando
                $ titulo_atual = "{} — {}".format(faixa_atual.get("name", ""), faixa_atual.get("artist_name", ""))
                $ detalhes = "Álbum: {}  |  Licença: {}".format(faixa_atual.get("album_name") or "Faixa independente", faixa_atual.get("license_ccurl") or "Consulte a Jamendo")
                text titulo_atual size 32 substitute False
                text detalhes size 23 substitute False

            for faixa in cozy_radio_estado.faixas:
                $ rotulo = "{} — {}".format(faixa.get("name", ""), faixa.get("artist_name", ""))
                button:
                    action Function(cozy_radio_estado.ouvir, faixa)
                    sensitive not cozy_radio_estado.ocupado
                    text rotulo substitute False
