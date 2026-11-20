# 🌿 The cozy retiring

### Uma visual novel sobre recomeços, escolhas e memórias.

Depois de séculos como guardiã, Fern recebe a oportunidade de escolher um novo lar e decidir como deseja viver. Durante três dias, suas escolhas revelam sua personalidade, criam memórias e abrem diferentes possibilidades de futuro.

**Projeto final de Raciocínio Algorítmico — PUCPR**  
**Desenvolvido por:** Ingrid Barbosa Silva e Evelin Monique Ferreira da Silva  
**Engine:** Ren’Py · **Idioma do jogo:** inglês

---

## 📥 Baixar e jogar

**Para jogar pelas versões prontas, não é necessário instalar Python, Ren’Py ou VS Code.**

| Sistema | Download | Arquivo para abrir |
|:--|:--|:--|
| 🪟 **Windows 64 bits** | [Baixar pacote PC](Thecozyretiring-1.0-dists/Thecozyretiring-1.0-pc.zip) | `Thecozyretiring.exe` |
| 🐧 **Linux x86_64** | [Baixar pacote PC](Thecozyretiring-1.0-dists/Thecozyretiring-1.0-pc.zip) | `Thecozyretiring.sh` |
| 🍎 **macOS** | [Baixar pacote Mac](Thecozyretiring-1.0-dists/Thecozyretiring-1.0-mac.zip) | `Thecozyretiring.app` |

### Como baixar pelo GitHub

1. Clique no download correspondente ao seu sistema.
2. Na página do arquivo, clique em **Download raw file**, no ícone de download ou em **View raw**, conforme a opção exibida.
3. Aguarde o download terminar.
4. **Extraia o ZIP inteiro** antes de abrir o jogo.

> Os pacotes estão armazenados com **Git LFS**, pois ultrapassam o limite de tamanho dos arquivos comuns do GitHub. Para baixá-los pelo navegador, você não precisa instalar Git LFS.

O pacote PC tem aproximadamente **159 MiB**, e o pacote Mac, **153 MiB**. Se o download resultar em um arquivo minúsculo contendo um texto que começa com `version https://git-lfs.github.com/spec/v1`, você recebeu somente a referência LFS. Volte à página do arquivo e baixe o conteúdo original.

---

## 🪟 Jogar no Windows

1. Baixe **Thecozyretiring-1.0-pc.zip**.
2. Clique com o botão direito no ZIP e selecione **Extrair tudo**.
3. Abra a pasta extraída **Thecozyretiring-1.0-pc**.
4. Dê dois cliques em **Thecozyretiring.exe**.

> Mantenha o `.exe` junto das pastas `game`, `lib`, `renpy` e dos demais arquivos extraídos. O executável precisa desses recursos para funcionar.

### Pelo terminal

Abra o PowerShell dentro da pasta extraída e execute:

```powershell
.\Thecozyretiring.exe
```

### Por um atalho

Você pode criar um atalho para `Thecozyretiring.exe` na área de trabalho. Mantenha a pasta completa do jogo no local original.

---

## 🐧 Jogar no Linux

O pacote PC também inclui a versão para **Linux x86_64**.

1. Baixe **Thecozyretiring-1.0-pc.zip**.
2. Extraia o ZIP no Linux.
3. Abra o terminal dentro da pasta **Thecozyretiring-1.0-pc**.
4. Conceda permissão de execução e inicie o jogo:

```bash
chmod +x Thecozyretiring.sh lib/py3-linux-x86_64/Thecozyretiring
./Thecozyretiring.sh
```

Dependendo do gerenciador de arquivos, também é possível abrir o `.sh` diretamente após conceder a permissão de execução.

> Este pacote não inclui um executável nativo para Linux ARM.

---

## 🍎 Jogar no macOS

1. Baixe **Thecozyretiring-1.0-mac.zip**.
2. Extraia o ZIP no próprio Mac.
3. Abra **Thecozyretiring.app**.
4. Se desejar, mova o aplicativo completo para a pasta **Aplicativos**.

Não retire arquivos de dentro do pacote `.app`.

Se o macOS bloquear a abertura por não reconhecer o desenvolvedor, confira a origem do download e siga as orientações de segurança do próprio sistema.

Se o aplicativo aparecer como danificado, tente baixar novamente e extrair diretamente no Mac. Evite extrair e recomprimir a distribuição no Windows.

---

## 💻 Baixar pelo Git e Git LFS

Esta opção permite obter o código-fonte e os pacotes prontos pelo terminal.

Instale:

- [Git](https://git-scm.com/)
- [Git LFS](https://git-lfs.com/)

Depois, execute:

```bash
git lfs install
git clone https://github.com/ingrid-barbosa/cozy_retiring_renpy.git
cd cozy_retiring_renpy
git lfs pull
```

Os pacotes completos ficarão na pasta:

```text
Thecozyretiring-1.0-dists/
```

Extraia o ZIP correspondente ao seu sistema e siga as instruções de abertura.

### Já clonou o repositório?

Abra o terminal dentro dele e execute:

```bash
git lfs install
git lfs pull
```

### Sobre “Code → Download ZIP”

Esse botão baixa uma cópia do repositório com o código-fonte. A inclusão dos pacotes completos do Git LFS depende da configuração do repositório.

Se os ZIPs das distribuições vierem somente como referências LFS:

- Baixe os pacotes individualmente pelos links da tabela inicial; ou
- Utilize Git com `git lfs pull`.

O código dentro de `projeto-final` pode ser executado pelo Ren’Py mesmo sem baixar as distribuições prontas.

---

## 🛠️ Executar o código pelo Ren’Py

Esta opção é indicada para estudar, editar ou executar o projeto-fonte.

### Dependências

- **Ren’Py SDK 8.5.3**, versão indicada para o projeto.
- Python e runtime incluídos no próprio SDK.
- Internet para os recursos online da Jamendo.

➡️ [Baixar Ren’Py SDK 8.5.3](https://www.renpy.org/release/8.5.3)

Não é necessário instalar Python separadamente, criar um ambiente virtual ou executar `pip install` para a execução básica.

### Pelo launcher

1. Baixe e extraia o repositório ou clone pelo Git.
2. Abra o launcher do Ren’Py.
3. Entre em **Preferences / Preferências**.
4. Em **Projects Directory / Diretório de projetos**, escolha a pasta que contém `projeto-final`.
5. Retorne à lista de projetos.
6. Selecione o jogo correspondente a `projeto-final`.
7. Clique em **Launch Project / Iniciar projeto**.

A estrutura deve ser:

```text
pasta-do-repositorio/
└── projeto-final/
    └── game/
        ├── script.rpy
        ├── screens.rpy
        └── ...
```

> O diretório selecionado no launcher deve conter `projeto-final`. Não selecione diretamente a pasta `game`.

### Pelo terminal do SDK

No **Windows**, abra o PowerShell dentro da pasta do Ren’Py SDK:

```powershell
.\renpy.exe "C:\caminho\cozy_retiring_renpy\projeto-final" run
```

No **Linux ou macOS**, abra o terminal dentro da pasta do SDK:

```bash
./renpy.sh "/caminho/cozy_retiring_renpy/projeto-final" run
```

Substitua os caminhos de exemplo pela localização do projeto no seu computador.

### Pelo VS Code

Abra `projeto-final` no VS Code para visualizar ou editar os arquivos. Para executar, utilize o launcher do Ren’Py ou os comandos do SDK no terminal.

> Os arquivos `.rpy` usam a linguagem do Ren’Py e não devem ser executados pelo botão **Run Python File** como scripts Python comuns.

---

## 🎮 Controles

| Ação | Controle |
|:--|:--|
| Completar o texto ou avançar o diálogo | Clique ou barra de espaço |
| Escolher uma opção | Clique na opção |
| Consultar memórias | Ícone do livro no canto superior direito |
| Abrir o menu do jogo | Esc |
| Salvar e carregar partidas | Opções dos menus do jogo |
| Ajustar volumes e velocidade do texto | Preferences |

---

## 🌸 Funcionalidades

- **Três rotas:** primavera, verão e outono.
- **Escolha de lar:** casa e estação influenciam a experiência.
- **Personalidade:** pontos de empatia, coragem, curiosidade e independência.
- **Continuidade narrativa:** diálogos que consideram encontros e acontecimentos anteriores.
- **Aleatoriedade:** aparições de personagens em situações específicas.
- **Livro de memórias:** decisões organizadas por dia e vinculadas à partida.
- **Diferentes finais:** possibilidades relacionadas à trajetória de Fern.
- **Interface personalizada:** caixas de diálogo, menus e efeitos visuais.
- **Ambientação sonora:** trilhas locais e áudio obtido pela Jamendo.

---

## 🎵 Áudio e API Jamendo

### Trilhas locais

As músicas acompanham automaticamente a estação e a situação narrativa.

Durante a exploração, a trilha principal alterna com quatro faixas neutras antes de retornar. Nos momentos de mistério, o jogo utiliza músicas específicas.

Esses arquivos já estão incluídos na distribuição.

### Ambientação online

A integração busca **Birdstrem, de Zeffon**, na Jamendo.

O jogo consulta a API pela internet, interpreta a resposta em JSON e baixa o áudio para uma pasta temporária. Depois, o Ren’Py reproduz a faixa em loop em um canal separado, junto das trilhas locais.

**É necessário ter internet para consultar e baixar a faixa.** Depois de baixada, ela pode continuar repetindo sem uma conexão permanente. Não se trata de uma transmissão ao vivo.

O menu **Jamendo Radio** também permite pesquisar outras faixas disponíveis.

As solicitações são executadas em segundo plano, com tratamento de erros. A narrativa e as músicas locais funcionam independentemente da disponibilidade do serviço.

### Configurar outro Client ID

A versão entregue possui um Client ID público configurado. Esse identificador representa a aplicação e não é uma senha.

Para substituir o identificador da ambientação automática sem modificar o código, defina a variável de ambiente `JAMENDO_CLIENT_ID` antes de iniciar o jogo.

<details>
<summary><strong>Windows</strong></summary>

Com o PowerShell aberto dentro da pasta extraída:

```powershell
$env:JAMENDO_CLIENT_ID = "SEU_CLIENT_ID"
.\Thecozyretiring.exe
```

</details>

<details>
<summary><strong>Linux</strong></summary>

Com o terminal aberto dentro da pasta extraída:

```bash
JAMENDO_CLIENT_ID="SEU_CLIENT_ID" ./Thecozyretiring.sh
```

</details>

<details>
<summary><strong>macOS</strong></summary>

Com o terminal na pasta que contém o aplicativo:

```bash
JAMENDO_CLIENT_ID="SEU_CLIENT_ID" "./Thecozyretiring.app/Contents/MacOS/Thecozyretiring"
```

</details>

Ao utilizar o código-fonte, defina a mesma variável e inicie o SDK pelo mesmo terminal.

O campo **Edit Client ID**, no menu Jamendo Radio, altera o identificador utilizado na busca manual. Ele não substitui a configuração da ambientação automática.

Não publique senhas ou tokens privados no repositório.

---

## 🔧 Problemas comuns

| Problema | Solução |
|:--|:--|
| O ZIP é muito pequeno e não abre | Baixe o conteúdo original do Git LFS ou execute `git lfs pull`. |
| O jogo não abre dentro do ZIP | Extraia todos os arquivos antes de executar. |
| O `.exe` não encontra recursos | Mantenha todas as pastas e arquivos da distribuição juntos. |
| Linux informa falta de permissão | Conceda permissão ao script e ao binário conforme o tutorial. |
| A ambientação online não toca | Confira internet, Client ID, disponibilidade da Jamendo e mensagens do menu de rádio. |
| Erro de certificado HTTPS | Confira data, hora, certificados e restrições da rede. Não desative a verificação de segurança. |
| O projeto não aparece no launcher | Selecione a pasta que contém `projeto-final`. |
| Erro ao executar `.rpy` como Python | Utilize o Ren’Py SDK. |
| Um save antigo apresenta erro | Teste uma nova partida; saves de versões diferentes podem ser incompatíveis. |

Quando houver erro, registre a mensagem exibida e, se gerado, o arquivo `traceback.txt`.

---

## 📂 Organização do repositório

| Localização | Conteúdo |
|:--|:--|
| `README.md` | Apresentação e instruções |
| `The cozy retiring · Apresentação Visual.html` | Página visual sobre o projeto |
| `Thecozyretiring-1.0-dists/` | Pacotes prontos para jogar |
| `projeto-final/game/script.rpy` | Fluxo principal |
| `projeto-final/game/story/` | Prólogo, rotas, escolhas e finais |
| `projeto-final/game/characters/` | Definições dos personagens |
| `projeto-final/game/system/` | Personalidade, memórias e trilhas |
| `projeto-final/game/requirements/api.rpy` | Integração da Jamendo no Ren’Py |
| `projeto-final/game/python-packages/cozy_radio.py` | Comunicação HTTPS e interpretação de JSON |
| `projeto-final/game/screens.rpy` | Telas e menus |
| `projeto-final/game/gui.rpy` | Configurações visuais |
| `projeto-final/game/images/` | Cenários, personagens e interface |
| `projeto-final/game/musics/` | Músicas e efeitos |
| `projeto-final/game/fonts/` | Fontes e licenças |
| `projeto-final/registros_individuais/` | Registros acadêmicos |
| `.gitattributes` | Configuração do Git LFS |
| `.gitignore` | Regras de arquivos ignorados pelo Git |

---

## 👩‍💻 Equipe

**Ingrid Barbosa Silva**  
Adaptação e desenvolvimento da narrativa, rotas, escolhas, condicionais, personalização visual, livro de memórias e ajustes de ambientação sonora.

**Evelin Monique Ferreira da Silva**  
Integração com a API e comunicação com o serviço externo.

A integração entre narrativa, áudio e serviço online envolveu colaboração entre as integrantes.

---

## 📌 Sobre as versões disponíveis

Esta entrega contém versões de desktop. Não há pacote Android, iOS ou versão web jogável incluída.

O HTML de apresentação descreve o projeto, mas não executa o jogo.

---

## 📚 Fontes e documentação

- [Ren’Py](https://www.renpy.org/)
- [Distribuições do Ren’Py](https://www.renpy.org/doc/html/build.html)
- [Execução pela linha de comando](https://www.renpy.org/doc/html/cli.html)
- [Jamendo](https://www.jamendo.com/)
- [Documentação da API Jamendo](https://developer.jamendo.com/v3.0)
- [Git LFS](https://git-lfs.com/)
- Ambientação online: **Birdstrem — Zeffon**.
- Licenças das fontes disponíveis em `projeto-final/game/fonts/`.

Os créditos dos demais recursos visuais e sonoros devem ser complementados com os respectivos autores e fontes.
