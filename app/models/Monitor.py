import re
import pymongo
import Monitorados
import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Base"]



class monitor(object):

    def __init__(self, frases=[], cod_audio = ""):
        self.frases = frases
        self.ptsPositivoTotal = 0
        self.ptsNegativosTotal = 0
        self.cod_audio = cod_audio

    def montaCabecalho(self):
        coll_monit = mydb["Monitorado"]



        cod_usu, datahora = self.cod_audio.split('_')

        datahora_object = datetime.strptime(datahora, '%d%m%Y')



    def ptPositivo(self, list = ""):
        self.list = list
        coll_list = mydb["Lista"]
        #print(list)

        for x in coll_list.find({"list_desc": list}, {"_id": 0, "list_desc": 0, "ptnegativo": 0}):
            for a in x.values():
                return a


    def ptNegativo(self, list = ""):
        self.list = list
        coll_list = mydb["Lista"]
        #print(list)

        for x in coll_list.find({"list_desc": list}, {"_id": 0, "list_desc": 0, "ptpositivo": 0}):
            for a in x.values():
                return a

    def monitora(self):

        self.montaCabecalho()

        for frase in self.frases:
            coll_sent = mydb["Sentencas"]

            # for x in mycoll_list.find({"desc_palavra":"Bom dia"},{"_id":0, "lista":0}):
            for x in coll_sent.find({}, {"_id": 0, "lista": 0}):
                for a in x.values():

                    match = re.search(a.lower(), frase)

                    if match:
                        for y in coll_sent.find({"desc_palavra": a}, {"_id": 0, "desc_palavra": 0}):
                            for b in y.values():

                                ptPos = self.ptPositivo(b)
                                # self.ptsPositivosTotal = self.ptsPositivosTotal + ptPos
                                print(a)
                                print(b)
                                print(ptPos)
                                Monitorados.sent = a
                                Monitorados.lista = b
                                Monitorados.ptpositivo = ptPos


                    else:
                        for y in coll_sent.find({"desc_palavra": a}, {"_id": 0, "desc_palavra": 0}):
                            for b in y.values():
                                ptNeg = self.ptNegativo(b)

                                #self.ptsNegativosTotal = + ptNeg

                                Monitorados.sent = a
                                Monitorados.lista = b
                                Monitorados.ptnegativo = ptNeg