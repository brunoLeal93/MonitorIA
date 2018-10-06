from google.cloud import storage

storage_client = storage.Client()

# from monitor.upAudio import ultimoAudio, upload_blob

from PLN_GS_v2 import transcribe

# from monitor.col import *

from monitor import monitora

bucket_name = 'ligacoes_gravadas'
source_dir = 'C:/Users/Bruno/PycharmProjects/MonitorIA/audios/*'
destination_blob_name = 'OP00115082018.flac'   # Audio com 1 voz
# destination_blob_name = 'OP000209092018.flac'  # Audio com 2 vozes
source_file_name = 'C:/Users/Bruno/PycharmProjects/MonitorIA/audios/' + destination_blob_name  # 
gcs_uri = 'gs://ligacoes_gravadas/' + destination_blob_name


# ultimoAudio()
# upload_blob(bucket_name, source_file_name, destination_blob_name)


audio_transcrito = transcribe(gcs_uri)

#audio_transcrito = ['alo bom dia gostaria de falar com senhor joão', 'Por favor você poderia seu nome completo',
#                   'meu nome é Bruno e falo daqui do broadcast', 'o motivo do meu contato é devido a um debito no valor de XXXXX ',
#                    'você pode efetuar o pagamento avista no valor XXXXX ou parcelado', 'apenas confirmando, seu endereço é XXXXX',
#                    'seu e-mail', '']

monitora(audio_transcrito)
