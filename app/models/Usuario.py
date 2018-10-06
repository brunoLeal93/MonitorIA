from app import mongo
from app.models.Forms import loginForm
from flask_login import UserMixin


class Usuario(UserMixin):

    def busca_usuario(self):
        result = mongo.Usuario.find_one

    def __init__(self, cod_usu="", senha_usu="", nome_usu="", tipo_usu="", equipe_usu=""):
        self.cod_usu = cod_usu
        self.senha_usu = senha_usu
        self.nome_usu = nome_usu
        self.tipo_usu = tipo_usu
        self.equipe_usu = equipe_usu
      #  self.insereUsuario()

        # self.tabela = mongo["Usuario"]

    #@property
    #def is_authenticated(self):
     #   return True

    #@property
    #def is_active(self):
    #    return False

    #@property
    #def is_anonymous(self):
    #    return False

    #def get_id(self):
    #    form = loginForm()
    #    for x in mongo.db.Usuario.find_one({"cod_usu": form.cod_func.data}):
    #       return str(x.get('_id'))


    #def insereUsuario(self):
    #    self.usu = {
    #       "cod_usu": self.cod_usu,
    #       "senha_usu": self.senha_usu,
    #        "nome_usu": self.nome_usu,
    #        "tipo_usu": self.tipo_usu,
    #        "equipe_usu": self.equipe_usu,
    #    }

    #    insert = mongo.db.Usuario.insert_one(self.usu)

    #   result = mongo.db.Usuario.find_one({"cod_usu": "SUP001"})

     #   print(result)


class Admin():
    pass


class Sup():
    pass


class Ope():
    pass


#u = Usuario()
# u.insereUsuario()
