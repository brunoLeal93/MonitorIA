from Collections import Sentenca, Lista, Monitorados, sentNDitas, sentDitas
from datetime import datetime


def monitora(audio_trascrito):

    monitorado = Monitorados()
    sentditas = []
    sentNditas = []
    total_ptpositivo = 0
    total_ptnegativo = 0
    datahora = datetime(2018, 9, 22, 16, 41)
    cod_usu = 'OPE0003'
    cod_audio = 'OPE000322092018.flac'

    # atribui pontuação , falta melhorar a questão da logica (considerar mais configurações)
    for sentenca in Sentenca.objects():

        contTrue=0
        contFalse = 0

        for x in audio_trascrito:

            if str(sentenca.desc_palavra).lower() in x.lower():

                contTrue += 1
            else:
                contFalse += 1

        for lista in Lista.objects(list_desc=sentenca.lista):

           # print('Setença: {} \t Lista: {} \n Pt Positivo: {} \t Pt Negativo: {}\ncontTrue: {} \t contFalse {}  \n =  {} \t {}\n\n'.format(sentenca.desc_palavra, sentenca.lista, lista.ptpositivo,
            #                                                             lista.ptnegativo, contTrue, contFalse, contTrue*lista.ptpositivo, contFalse*lista.ptnegativo))

            #
            if contTrue > 0:
                stds = sentDitas(sent=sentenca.desc_palavra, list=sentenca.lista, ptpositivo=lista.ptpositivo)
                sentditas.append(stds)
                total_ptpositivo = total_ptpositivo + lista.ptpositivo

            else:
                if lista.ptnegativo < 0:
                    stnds = sentNDitas(sent=sentenca.desc_palavra, list=sentenca.lista, ptnegativo=lista.ptnegativo)
                    sentNditas.append(stnds)
                    total_ptnegativo = total_ptnegativo + lista.ptnegativo
    # fim de atribuição de pontos

    monitorado.cod_audio = cod_audio
    monitorado.cod_usu = cod_usu
    monitorado.datahora = datahora
    monitorado.total_ptpositivo = total_ptpositivo
    monitorado.total_ptnegativo = total_ptnegativo
    monitorado.sentditas = sentditas
    monitorado.sentnditas = sentNditas

    monitorado.save()
