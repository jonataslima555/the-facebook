# models.py
from peewee import Model, CharField, ForeignKeyField, TextField, DateTimeField, SQL
from database import db

class BaseModel(Model):
    class Meta:
        database = db

class Client(BaseModel):
    name = CharField()
    password = CharField()
    email = CharField()

class Publication(BaseModel):
    client = ForeignKeyField(Client, backref="clients")
    name_publi = CharField()
    descr_publi = TextField()
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

class Like(BaseModel):
    client = ForeignKeyField(Client, backref='likes')
    publication = ForeignKeyField(Publication, backref='likes')
    class Meta:
        database = db
        constraints = [SQL('UNIQUE(client_id, publication_id)')]

class Follow(BaseModel):
    follower = ForeignKeyField(Client, backref='following')
    followee = ForeignKeyField(Client, backref='followers')
    class Meta:
        database = db
        constraints = [SQL('UNIQUE(follower_id, followee_id)')]

class Comment(BaseModel):
    client = ForeignKeyField(Client, backref='comments')
    publication = ForeignKeyField(Publication, backref='comments')
    content = TextField()
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
