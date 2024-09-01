from models import *
from apis import validar_email
from bcrypt import hashpw, gensalt, checkpw
# Função de criar Usuário com defesa na senha
def create_user(name, password, email):
    if Client.select().where(Client.email == email).exists(): # Verifica se o email já existe
        print('Email já cadastrado...')
        return menu()
    try:
        with db.atomic():
            salt = gensalt()
            hash_pw = hashpw(password.encode('utf-8'), salt) # Gera uma senha segura no banco de dados
            Client.create(
                name=name,
                password=hash_pw,
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

    
    if email: # Validador de email
        validator = validar_email(email)
        if validator:
            if len(password) <= 6: # Força senha mais segura
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
            return home()
        else:
            print('Senha incorreta. Tente novamente.')
            password_attempts += 1

    print('Número de tentativas excedidas. Retornando ao Menu')
    return menu()

# Menu 
def menu():
    print('Menu')

def home():
    print('Home')


if __name__ == "__main__":
    login_user()
    #register_user()