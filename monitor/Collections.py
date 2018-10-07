from mongoengine import connect,Document, EmbeddedDocument, StringField, IntField, ListField, DateTimeField, EmbeddedDocumentField

connect('Base')


class Lista(Document):
    list_desc = StringField(required=True, unique=True)
    ptpositivo = IntField(required=True)
    ptnegativo = IntField(required=True)
    meta = {
        'collection': 'Lista',
    }


class Sentenca(Document):
    meta = {'collection': 'Sentencas'}
    desc_palavra = StringField(required=True)
    lista = StringField(required=True)


class sentDitas(EmbeddedDocument):
    sent = StringField()
    list = StringField()
    ptpositivo = IntField()


class sentNDitas(EmbeddedDocument):
    sent = StringField()
    list = StringField()
    ptnegativo = IntField()


class Monitorados(Document):
    meta = {'collection': 'Monitorados'}
    cod_audio = StringField(required=False)
    cod_usu = StringField(required=False)
    datahora = DateTimeField(required=False)
    total_ptpositivo = IntField(required=True)
    total_ptnegativo = IntField(required=True)
    sentditas = ListField(EmbeddedDocumentField(sentDitas))
    sentnditas = ListField(EmbeddedDocumentField(sentNDitas))

class otherConfig(Document):
    meta = {'collection': 'outrasConfig'}
    dir_audio = StringField(required=True)

