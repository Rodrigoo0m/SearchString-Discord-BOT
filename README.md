# Discord File Search Bot

Este projeto é um bot do Discord que permite aos usuários pesquisar em arquivos de texto por meio de um canal privado no servidor do Discord. O bot cria um canal exclusivo para o usuário que executa o comando de início e fornece uma interface interativa para selecionar o arquivo e inserir a consulta de pesquisa.

## Funcionalidades

- Criação de um canal privado para interações de pesquisa.
- Pesquisa em arquivos de texto específicos baseada em consultas fornecidas pelo usuário.
- Interface interativa com botões para selecionar o arquivo desejado.
- Envio de resultados de pesquisa diretamente para o usuário, tanto em texto quanto como um arquivo, dependendo do tamanho.

## Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://python.org/). 
Além disso, é bom ter um editor para trabalhar com o código, como o [VSCode](https://code.visualstudio.com/).

## Configuração

Para executar este projeto, você precisará adicionar um arquivo `.env` na raiz do projeto com o token do seu bot:

DISCORD_BOT_TOKEN=seu_token_aqui


Substitua `seu_token_aqui` pelo token do seu bot do Discord.

## Instalação

```bash
# Clone este repositório
$ git clone <https://github.com/seu-usuario/seu-repositorio>

# Acesse a pasta do projeto no terminal/cmd
$ cd seu-repositorio

# Instale as dependências
$ pip install -r requirements.txt

# Execute a aplicação
$ python main.py


Uso
Use o comando !start em qualquer canal do seu servidor Discord para iniciar o bot.
O bot criará um canal privado e fornecerá opções de arquivos para pesquisar.
Clique no botão correspondente ao arquivo que deseja pesquisar.
Insira sua consulta de pesquisa.
Os resultados serão enviados para você no canal privado criado.
Contribuições
Contribuições são sempre bem-vindas! Para contribuir, siga estes passos:

Faça um fork do projeto.
Crie uma nova branch com as suas modificações: git checkout -b minha-feature.
Salve as modificações e crie uma mensagem de commit contando o que você fez: git commit -m "feature: Minha nova feature".
Envie as suas modificações: git push origin minha-feature.

Feito com ❤️ por Rodrigoo0m
