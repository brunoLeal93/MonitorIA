from app import db
from mongoengine import connect, Document
from app.models.Collections import Lista
connect('Base')

class Lista(Lista):

    def insereLista(self):





# lista = [
#     {
#        "_id": 1,
#        "list_desc": "Educação",
#        "ptpositivo": 5,
#        "ptnegativo": 0,
#    },
#
#    {
#        "_id": 2,
#        "list_desc": "Confiabilidade",
#        "ptpositivo": 50,
#        "ptnegativo": -10,
#     },
#
#   {
#        "_id": 3,
#        "list_desc": "Identificação",
#        "ptpositivo": 5,
#        "ptnegativo": -10,
#    }
# ]


mycoll_list = mydb["Lista"]

x = mycoll_list.insert_many(lista)

print(mydb.list_collection_names())