"""Radio HTTP and JSON handling, independent of the Ren'Py interface."""
import json
from pathlib import Path
from urllib.parse import urlencode, urlparse
from urllib.request import urlopen
from uuid import uuid4


def contexto_https():
    import ssl

    contexto = ssl.create_default_context()
    try:
        import certifi
    except ImportError:
        return contexto

    contexto.load_verify_locations(cafile=certifi.where())
    return contexto


def consultar(client_id, busca):
    if not client_id:
        raise ValueError("Enter a Jamendo Client ID before searching.")
    query = urlencode(dict(client_id=client_id, format="json", limit=20,
                           search=busca, type="single albumtrack", audiodlformat="mp31"))
    with urlopen("https://api.jamendo.com/v3.0/tracks/?" + query, timeout=8,
                 context=contexto_https()) as resposta:
        dados = resposta.read(1_000_001)
    if len(dados) > 1_000_000:
        raise ValueError("The radio response is too large.")
    pacote = json.loads(dados.decode("utf-8"))
    if not isinstance(pacote, dict):
        raise ValueError("The radio returned an invalid response.")
    cabecalho, resultados = pacote.get("headers"), pacote.get("results")
    if not isinstance(cabecalho, dict):
        raise ValueError("The response did not contain Jamendo API headers.")
    codigo = str(cabecalho.get("code", ""))
    if codigo != "0":
        if codigo == "5":
            raise ValueError("Jamendo could not validate the Client ID (code 5). Try your own application ID.")
        if codigo == "6":
            raise ValueError("Jamendo's rate limit was reached (code 6). Try again later.")
        if codigo == "11":
            raise ValueError("This Jamendo application is suspended (code 11).")
        if codigo.isascii() and codigo.isdecimal():
            raise ValueError("Jamendo rejected the search (code {}).".format(codigo))
        raise ValueError("The response did not contain a valid Jamendo API status code.")
    if not isinstance(resultados, list):
        raise ValueError("The track list is invalid.")
    return [faixa for faixa in resultados if isinstance(faixa, dict) and faixa.get("id")]


def buscar_birdstrem(client_id):
    for busca in ("Zeffon", "Birdstrem", "Birdstream"):
        for faixa in consultar(client_id, busca):
            artista = (faixa.get("artist_name") or "").strip().casefold()
            titulo = (faixa.get("name") or "").strip().casefold()
            if artista == "zeffon" and titulo in ("birdstrem", "birdstream") and pode_baixar(faixa):
                return faixa
    raise ValueError("Birdstrem by Zeffon was not available for download on Jamendo.")


def pode_baixar(faixa):
    url = faixa.get("audiodownload")
    return (faixa.get("audiodownload_allowed") is True
            and isinstance(url, str) and urlparse(url).scheme == "https")


def baixar(faixa, pasta):
    if not pode_baixar(faixa):
        raise ValueError("This Jamendo track cannot be downloaded for in-game playback.")
    with urlopen(faixa["audiodownload"], timeout=10, context=contexto_https()) as resposta:
        if urlparse(resposta.geturl()).scheme != "https":
            raise ValueError("The track URL is invalid.")
        dados = resposta.read(15_000_001)
    if not dados or len(dados) > 15_000_000:
        raise ValueError("The track is empty or exceeds the size limit.")
    if not (dados.startswith(b"ID3") or dados[0] == 255 and len(dados) > 1 and dados[1] & 224 == 224):
        raise ValueError("The track is not in MP3 format.")
    nome = "cozy_jamendo_" + uuid4().hex + ".mp3"
    (Path(pasta) / nome).write_bytes(dados)
    return nome
