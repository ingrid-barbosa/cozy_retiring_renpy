"""HTTP e JSON da rádio, independentes da interface Ren'Py."""
import json
from pathlib import Path
from urllib.parse import urlencode, urlparse
from urllib.request import urlopen
from uuid import uuid4


def consultar(client_id, busca):
    if not client_id:
        raise ValueError("Configure JAMENDO_CLIENT_ID para buscar músicas.")
    query = urlencode(dict(client_id=client_id, format="json", limit=8,
                           search=busca, audiodlformat="mp31"))
    with urlopen("https://api.jamendo.com/v3.0/tracks/?" + query, timeout=8) as resposta:
        dados = resposta.read(1_000_001)
    if len(dados) > 1_000_000:
        raise ValueError("A resposta da rádio é grande demais.")
    pacote = json.loads(dados.decode("utf-8"))
    if not isinstance(pacote, dict):
        raise ValueError("A rádio retornou uma resposta inválida.")
    cabecalho, resultados = pacote.get("headers"), pacote.get("results")
    if not isinstance(cabecalho, dict) or cabecalho.get("status") != "success":
        raise ValueError("A Jamendo recusou a consulta. Confira o Client ID.")
    if not isinstance(resultados, list):
        raise ValueError("A lista de músicas é inválida.")
    faixas = []
    for faixa in resultados[:8]:
        if not isinstance(faixa, dict) or faixa.get("audiodownload_allowed") is not True:
            continue
        url = faixa.get("audiodownload")
        if isinstance(url, str) and urlparse(url).scheme == "https":
            faixas.append(faixa)
    return faixas


def baixar(faixa, pasta):
    with urlopen(faixa["audiodownload"], timeout=10) as resposta:
        if urlparse(resposta.geturl()).scheme != "https":
            raise ValueError("O endereço da faixa é inválido.")
        dados = resposta.read(15_000_001)
    if not dados or len(dados) > 15_000_000:
        raise ValueError("A faixa está vazia ou excede o limite de tamanho.")
    if not (dados.startswith(b"ID3") or dados[0] == 255 and len(dados) > 1 and dados[1] & 224 == 224):
        raise ValueError("A faixa não está em formato MP3.")
    nome = "cozy_jamendo_" + uuid4().hex + ".mp3"
    (Path(pasta) / nome).write_bytes(dados)
    return nome
