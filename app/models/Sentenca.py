import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Base"]


# palavra_id = palavra_id + 1

palavras = [
    {
        "_id": 1,
        "sent": "Bom dia",
        "lista": "Educação",
    },
    {
        "_id": 2,
        "sent": "Boa Noite",
        "lista": "Educação",
    },
    {
        "_id": 3,
        "sent": "Boa Tarde",
        "lista": "Educação",
    },
    {
        "_id": 4,
        "sent": "Por Favor",
        "lista": "Educação",
    },
    {
        "_id": 5,
        "sent": "Obrigado",
        "lista": "Educação",
    },
    {
        "_id": 6,
        "sent": "Obrigada",
        "lista": "Educação",
    },
    {
        "_id": 7,
        "sent": "Nome Completo",
        "lista": "Confiabilidade",
    },
    {
        "_id": 8,
        "sent": "cpf",
        "lista": "Confiabilidade",
    },
    {
        "_id": 9,
        "sent": "Seu Endereço",
        "lista": "Confiabilidade",
    },
    {
        "_id": 10,
        "sent": "Seu Telefone",
        "lista": "Confiabilidade",
    },
    {
        "_id": 11,
        "sent": "Meu Nome",
        "lista": "Identificaçãoo",
    },
    {
        "_id": 12,
        "sent": "Eu Sou",
        "lista": "Identificação",
    },
    {
        "_id": 13,
        "sent": "Falo da",
        "lista": "Identificação",
    },
    {
        "_id": 14,
        "sent": "Falo do",
        "lista": "Identificação",
    },
    {
        "_id": 15,
        "sent": "Broadcast",
        "lista": "Identificação",
    },
]
mycoll_sent = mydb["Sentencas"]

x = mycoll_sent.insert_many(palavras)
