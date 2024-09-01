# database.py
from peewee import SqliteDatabase
from dotenv import load_dotenv
from os import getenv

# Configurando variáveis de ambiente
load_dotenv()

DB_NAME = getenv("DB_NAME")

if not DB_NAME:
    raise AttributeError("DB_NAME não está definida nas variáveis de ambiente.")

db = SqliteDatabase(f'{DB_NAME}')
