cod_audio = ""
cod_usu = ""
datahora = ''
total_ptpositivo = 0
total_ptnegativo = 0
sent = ""
lista = ""
ptpositivo = 0
ptnegativo = 0

send_ditas:{
    "sent": sent,
    "lista": lista,
    "ptpositivo": ptpositivo
}

send_nditas:{
    "sent": sent,
    "lista": lista,
    "ptnegativo": ptnegativo
}

Monitorados: {
    "cod_audio": cod_audio,
    "cod_usu": cod_usu,
    "datahora": datahora,
    "total_ptpositivo": total_ptpositivo,
    "total_ptnegativo": total_ptnegativo,
    "send_ditas": [send_ditas],
    "send_nditas": [send_nditas]
}