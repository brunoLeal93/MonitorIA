from app import db
from flask_login.mixins import UserMixin


class User(db.Document, UserMixin):
    meta = {'collection': 'Usuario'}
    cod_usu = db.StringField(required=True)
    senha_usu = db.StringField(required=True)
    nome_usu = db.StringField(required=True)
    tipo_usu = db.StringField(required=True)
    equipe_usu = db.ListField()


class Lista(db.Document):


    list_desc = db.StringField(required=True, unique=True)
    ptpositivo = db.IntField(required=True)
    ptnegativo = db.IntField(required=True)
    meta = {
        'collection': 'Lista',
    }


class Sentenca(db.Document):
    meta = {'collection': 'Sentencas'}
    desc_palavra = db.StringField(required=True)
    lista = db.StringField(required=True)


class sentDitas(db.EmbeddedDocument):
    sent = db.StringField()
    list = db.StringField()
    ptpositivo = db.IntField()


class sentNDitas(db.EmbeddedDocument):
    sent = db.StringField()
    list = db.StringField()
    ptnegativo = db.IntField()


class Monitorados(db.Document):
    meta = {'collection': 'Monitorados'}
    cod_audio = db.StringField(required=True)
    cod_usu = db.StringField(required=True)
    datahora = db.DateTimeField()
    total_ptpositivo = db.IntField(required=True)
    total_ptnegativo = db.IntField(required=True)
    sentditas = db.ListField(db.EmbeddedDocumentField(sentDitas))
    sentnditas = db.ListField(db.EmbeddedDocumentField(sentNDitas))

class othersConfig(db.Document):
    meta = {'collection': 'outrasConfig'}
    dir_audio = db.StringField(required=True)
