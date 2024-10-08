# The Facebook Clone

Este é um projeto de terminal que simula funcionalidades básicas de uma rede social, como criação de conta, login, postagens, curtidas e seguir usuários. O projeto é implementado em Python usando a biblioteca `peewee` para interagir com um banco de dados SQLite.

## Tecnologias Usadas

- **Python:** Linguagem de programação principal utilizada para desenvolvimento do projeto.
- **Peewee:** ORM (Object Relational Mapping) usado para interagir com o banco de dados SQLite.
- **SQLite:** Banco de dados leve utilizado para armazenamento de dados.
- **bcrypt:** Biblioteca utilizada para hash seguro de senhas.
- **requests:** Biblioteca usada para fazer requisições HTTP à API externa.
- **dotenv:** Utilizada para carregar variáveis de ambiente a partir de um arquivo `.env`.
- **API Externa:** A API `invertexto` é utilizada para validação de emails, garantindo que o usuário utilize um email válido ao criar uma conta.

## Funcionalidades

- **Criar Conta:** Permite ao usuário criar uma nova conta no sistema, verificando se o email já existe.

  - **Validação de Email:** Uma API externa é utilizada para validar o formato e a existência do email, evitando o uso de emails temporários ou inválidos.
  - **Segurança de Senhas:** As senhas dos usuários são protegidas utilizando a biblioteca `bcrypt` para hash e salting, aumentando a segurança contra ataques de dicionário e força bruta.
- **Login:** Autenticação de usuários com verificação de senha.

  - **Proteção contra Brute Force:** Após três tentativas de login com falha, o sistema retorna ao menu principal, dificultando ataques de brute force.
- **Criar Postagem:** Usuários autenticados podem criar postagens, que são armazenadas no banco de dados e exibidas para outros usuários.
- **Ver Postagens:** Visualizar todas as postagens disponíveis, ordenadas por data de criação, incluindo a contagem de curtidas e seguidores.
- **Curtir Postagem:** Usuários autenticados podem curtir postagens, com um controle para evitar múltiplas curtidas na mesma postagem.
- **Seguir Usuário:** Os usuários podem seguir outros usuários, permitindo que vejam as postagens daqueles que seguem.

  - **Lista de Usuários Disponíveis:** O sistema mostra uma lista de usuários disponíveis para seguir, excluindo aqueles que o usuário já segue.
- **Ver Postagens de Usuários Seguidos:** Permite que o usuário veja tanto suas próprias postagens quanto as postagens das pessoas que ele segue.

## Como Instalar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/the-facebook-clone.git
   cd the-facebook-clone
   ```

## Crie um ambiente virtual:

python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

## Instale as dependências

pip install -r requirements.txt

## Crie um arquivo com o nome .env:

DB_NAME=seu_banco_de_dados.sqlite
API_KEY_EMAIL_VALIDATOR=sua_chave_api

## Execute main.py:

python main.py
