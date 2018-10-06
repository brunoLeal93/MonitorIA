from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateTimeField, IntegerField
from wtforms.validators import DataRequired


class loginForm(FlaskForm):
    cod_func = StringField("cod_func", validators=[DataRequired()])
    senha_func = PasswordField("senha_func", validators=[DataRequired()])
    lembre_me = BooleanField("lembre_me")


class relForm(FlaskForm):
    data_ini = DateTimeField("data_ini")
    data_fim = DateTimeField("data_fim")
    nome_sup = StringField("nome_sup")
    nome_ope = StringField("nome_ope")
    desc_audio = StringField("desc_audio")  # Não Inserido
    equipe = StringField("equipe")
    pts_positivo = BooleanField("pts_positivo")  # Não Inserido
    pts_negativo = BooleanField("pts_negativo")  # Não Inserido


class listaForm(FlaskForm):
    desc_lista = StringField("desc_lista")
    ptspositivo = IntegerField("ptspositivo")
    ptsnegativo = IntegerField("ptsnegativo")



class sentencaForm(FlaskForm):
    desc_sent = StringField("desc_palavra")
    lista = StringField("lista")