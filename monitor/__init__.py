from google.cloud import storage
storage_client = storage.Client()
from monitor.controlador import ultimoAudio, upload_blob
from monitor.PLN_GS import transcribe
from monitor.monitor import monitora
from monitor.Collections import otherConfig

config = otherConfig.objects()

for x in config:
    dir_audio = x.dir_audio

destination_blob_name = ultimoAudio(dir_audio)


source_file_name = dir_audio +'/' + destination_blob_name  #

bucket_name = 'ligacoes_gravadas'

gcs_uri = 'gs://'+bucket_name+'/' + destination_blob_name

upload_blob(bucket_name, source_file_name, destination_blob_name)


audio_transcrito = transcribe(gcs_uri)

monitora(audio_transcrito)
