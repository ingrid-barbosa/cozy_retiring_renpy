# The cozy retiring

Uma visual novel sobre recomeços, escolhas e memórias, desenvolvida em Ren’Py para o projeto final de Raciocínio Algorítmico da PUCPR.

**Integrantes:** Ingrid Barbosa Silva e Evelin Monique Ferreira da Silva.

## Sobre o jogo

Depois de séculos como guardiã, Fern recebe a oportunidade de escolher um novo lar e decidir como deseja viver.

A jogadora escolhe uma casa e uma estação e acompanha três dias dessa nova vida. Durante esse período, encontra personagens, explora cenários e toma decisões que influenciam seus diálogos, suas memórias e as possibilidades de final.

O jogo está em inglês.

## Funcionalidades

- Três rotas: primavera, verão e outono.
- Escolha de casa e estação.
- Decisões que acumulam pontos de personalidade.
- Cenas e diálogos condicionados aos acontecimentos da partida.
- Encontros aleatórios em situações específicas.
- Livro de memórias organizado por dia.
- Recapitulação das escolhas e diferentes possibilidades de final.
- Interface personalizada, efeitos visuais e texto gradual.
- Músicas locais que acompanham a estação e os momentos de mistério.
- Integração com a API Jamendo para busca e reprodução de áudio online.

## Tecnologias e dependências

- Ren’Py 8, com suporte a Python 3.
- Python integrado ao Ren’Py.
- API Jamendo.
- Bibliotecas padrão do Python, incluindo `json`, `urllib`, `ssl` e `tempfile`.

Recomenda-se utilizar o Ren’Py SDK 8.5.3 para abrir o projeto.

Não é necessário instalar Python separadamente ou executar `pip install` para a execução básica. O módulo `certifi` é consultado quando disponível; caso contrário, a integração utiliza os certificados acessíveis ao ambiente Python do Ren’Py.

A conexão com a internet é necessária para as funcionalidades da Jamendo. A narrativa e as músicas locais não dependem desse serviço.

## Como executar

### 1. Instalar o Ren’Py

Baixe e extraia o Ren’Py SDK:

https://www.renpy.org/

### 2. Obter o projeto

No GitHub, selecione **Code → Download ZIP** e extraia o arquivo.

Também é possível clonar o repositório:

```bash
git clone https://github.com/ingrid-barbosa/cozy_retiring_renpy.git
```

### 3. Localizar a pasta do jogo

A pasta que deve ser reconhecida pelo Ren’Py é:

```text
cozy_retiring_renpy/projeto-final
```

Ela contém a subpasta `game`. Mantenha os arquivos, imagens, fontes e áudios dentro da estrutura original.

### 4. Abrir no launcher

1. Execute o launcher do Ren’Py.
2. Abra **Preferences / Preferências**.
3. Em **Projects Directory / Diretório de projetos**, escolha a pasta `cozy_retiring_renpy`, que contém `projeto-final`.
4. Retorne à lista de projetos.
5. Selecione o projeto correspondente à pasta `projeto-final`.
6. Clique em **Launch Project / Iniciar projeto**.

Não execute os arquivos `.rpy` diretamente com o Python ou pelo botão de execução do VS Code.

## Controles

| Ação | Controle |
|---|---|
| Avançar o diálogo ou completar o texto | Clique ou barra de espaço |
| Escolher uma opção | Clique na opção |
| Consultar memórias | Ícone do livro no canto superior direito |
| Abrir o menu do jogo | Esc |
| Ajustar volumes e velocidade do texto | Preferences |

Os menus também permitem salvar e carregar partidas.

## Música e integração com a Jamendo

O áudio utiliza duas partes complementares:

### Trilhas locais

O código do jogo controla automaticamente as músicas conforme a estação e a situação narrativa.

Durante a exploração, a sequência alterna a trilha principal com quatro faixas neutras antes de retornar à principal. As cenas de mistério utilizam uma trilha própria.

### Ambientação online

A integração com a Jamendo busca a faixa de ambientação **Birdstrem, de Zeffon**, e tenta reproduzi-la em loop junto das músicas locais.

O menu **Jamendo Radio** também permite pesquisar faixas online e ouvir os resultados disponíveis para reprodução.

A API retorna informações em JSON. O jogo interpreta esses dados e obtém o áudio permitido para reprodução. As solicitações são realizadas em segundo plano para evitar bloquear a interface.

### Configuração do Client ID

A versão entregue possui um Client ID configurado. Esse identificador público da aplicação não é uma senha.

Para utilizar outra aplicação Jamendo sem alterar o código, é possível definir a variável de ambiente `JAMENDO_CLIENT_ID` antes de abrir o Ren’Py.

No PowerShell:

```powershell
$env:JAMENDO_CLIENT_ID = "SEU_CLIENT_ID"
```

Depois, inicie o launcher pelo mesmo PowerShell, ajustando o caminho para a instalação do SDK:

```powershell
& "C:\caminho\para\renpy-sdk\renpy.exe"
```

O campo **Edit Client ID**, dentro do menu Jamendo Radio, permite alterar o identificador utilizado na busca manual. Para a ambientação automática, utilize a variável de ambiente.

Não é necessário inserir senhas ou tokens privados no repositório.

### Se o áudio online não funcionar

Confira:

- A conexão com a internet.
- A validade do Client ID e a situação da aplicação na Jamendo.
- Eventuais mensagens de erro exibidas no menu de rádio.
- Bloqueios de rede, DNS ou problemas de certificados HTTPS.

A disponibilidade do áudio online depende da Jamendo e da faixa. Uma falha nessa integração não substitui nem remove as trilhas locais.

## Organização do projeto

| Localização | Conteúdo |
|---|---|
| `projeto-final/game/script.rpy` | Fluxo principal da partida |
| `projeto-final/game/story/` | Prólogo, escolha de lar, rotas e finais |
| `projeto-final/game/characters/` | Definições de personagens |
| `projeto-final/game/system/personality.rpy` | Pontuações e variáveis da partida |
| `projeto-final/game/system/memorias.rpy` | Registro e interface do livro |
| `projeto-final/game/system/soundtrack.rpy` | Controle das trilhas locais |
| `projeto-final/game/requirements/api.rpy` | Integração da Jamendo com o Ren’Py |
| `projeto-final/game/python-packages/cozy_radio.py` | Comunicação HTTP e interpretação das respostas |
| `projeto-final/game/screens.rpy` | Telas e menus |
| `projeto-final/game/gui.rpy` | Configurações visuais |
| `projeto-final/game/images/` | Cenários, personagens e interface |
| `projeto-final/game/musics/` | Músicas e efeitos locais |
| `projeto-final/game/fonts/` | Fontes utilizadas |
| `projeto-final/registros_individuais/` | Registros acadêmicos da equipe |

## Conceitos aplicados

- Condicionais para selecionar rotas, encontros e consequências.
- Variáveis para registrar acontecimentos anteriores.
- Acumuladores para os pontos de personalidade.
- Listas e dicionários para organizar memórias e informações.
- Funções para organizar comportamentos reutilizáveis.
- Aleatoriedade para variar encontros.
- Requisições HTTPS e interpretação de JSON.
- Tratamento de erros na comunicação com serviços externos.

## Contribuições da equipe

**Ingrid Barbosa Silva:** desenvolvimento e adaptação da narrativa, rotas, escolhas, condicionais, personalização visual, livro de memórias e ajustes de ambientação sonora.

**Evelin Monique Ferreira da Silva:** desenvolvimento da integração com a API e da comunicação com o serviço externo.

A integração entre narrativa, áudio e serviço online envolveu colaboração entre as integrantes.

## Demonstração sugerida

1. Iniciar uma nova partida.
2. Escolher uma estação e uma casa.
3. Tomar uma decisão durante a exploração.
4. Abrir o livro e conferir a memória registrada.
5. Observar a trilha da estação e demonstrar a integração online.
6. Carregar uma partida salva para apresentar uma cena posterior e o final.

## Créditos e fontes

- Ren’Py: https://www.renpy.org/
- Jamendo: https://www.jamendo.com/
- Documentação da API Jamendo: https://developer.jamendo.com/v3.0
- Ambientação online: **Birdstrem — Zeffon**.
- Licenças das fontes disponíveis na pasta `game/fonts`.

Os créditos dos demais recursos visuais e sonoros devem identificar seus respectivos autores e fontes.
