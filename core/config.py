# config.py
from database import db
from models import *
from dotenv import load_dotenv
from os import getenv

# Configurando variáveis de ambiente
load_dotenv()

API_KEY_EMAIL_VALIDATOR = getenv("API_KEY_EMAIL_VALIDATOR")

if not API_KEY_EMAIL_VALIDATOR:
    raise AttributeError("API_KEY_EMAIL_VALIDATOR não está definida nas variáveis de ambiente.")

# Criando banco de dados e tabelas
try:
    with db.atomic():
        db.create_tables([Client, Publication, Like, Follow, Comment])
except AttributeError as e:
    print(f'Erro {e} ao criar o banco de dados...')
