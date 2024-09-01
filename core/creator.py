from os import system
from models import *
from apis import validar_email
from bcrypt import hashpw, gensalt, checkpw
from publi_creator import post_pb, like_publi, view_all_posts, view_user_posts_and_followed  # Importando as funções de criar postagens e curtir
from follow import follow_user  # Importando a função de seguir usuários

# Função de criar Usuário com defesa na senha
def create_user(name, password, email):
    if Client.select().where(Client.email == email).exists():  # Verifica se o email já existe
        print('Email já cadastrado...')
        return menu()
    try:
        with db.atomic():
            salt = gensalt()
            hash_pw = hashpw(password.encode('utf-8'), salt)  # Gera uma senha segura no banco de dados
            Client.create(
                name=name,
                password=hash_pw.decode('utf-8'),  # Decodificar para armazenar como string
                email=email
            )
    except AttributeError as e:
        print(f'Erro {e} ao criar usuário')
    finally:
        return menu()

# Passa os parametros para registar o usuario e valida o email
def register_user():
    name = input("Digite seu nome: ")
    password = input("Digite sua senha: ")
    email = input("Digite seu email: ")

    if email:  # Validador de email
        validator = validar_email(email)
        if validator:
            if len(password) <= 6:  # Força senha mais segura
                print('Digite uma senha mais longa com no mínimo 8 caracteres...')
                return menu()
            else:
                create_user(name, password, email)
        else:
            print('Email inválido, por favor, digite um email valido..')
            return menu()

# Fazer login
def login_user():
    email = input("Digite seu email: ")
    password_attempts = 0

    try:
        user = Client.get(Client.email == email)
    except Client.DoesNotExist:
        print('O usuário não existe...')
        return menu()

    while password_attempts < 3:
        password = input('Digite sua senha: ')

        if checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            print('Login bem-sucedido!')
            return home(user)
        else:
            print('Senha incorreta. Tente novamente.')
            password_attempts += 1

    print('Número de tentativas excedidas. Retornando ao Menu')
    return menu()

# Menu 
def menu():
    print("Seja bem-vindo!!\n1 - Fazer login\n2 - Criar conta\n3 - Sair...\n")
    user = input(': ')
    if user == '1':
        return login_user()
    elif user == '2':
        return register_user()
    elif user == '3':
        exit()
    else:
        system('clear')
        print("Digite: 1, 2 ou 3...\n")
    

def home(logged_client):
    while True:  # Loop para manter o usuário no menu até escolher sair
        print(f"Seja bem-vindo de volta, {logged_client.name}...\n1 - Criar postagem\n2 - Ver postagens\n3 - Ver suas publicações e das pessoas que você segue\n4 - Curtir Postagem\n5 - Seguir Usuário\n6 - Sair\n")
        user = input(': ')
        if user == '1':
            post_pb(logged_client)
        elif user == '2':
            view_all_posts()
        elif user == '3':
            view_user_posts_and_followed(logged_client)
        elif user == '4':
            publication_id = int(input('Digite o ID da publicação que deseja curtir: '))
            like_publi(logged_client.id, publication_id)
        elif user == '5':
            follow_user(logged_client)
        elif user == '6':
            print("Você foi desconectado.")
            break  # Sai do loop e retorna ao menu principal ou encerra
        else:
            system('clear')
            print("Digite: 1, 2, 3, 4, 5 ou 6...\n")




if __name__ == "__main__":
    menu()
