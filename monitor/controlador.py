from monitor import storage_client
import glob
import os
from monitor.Collections import otherConfig

# Função faz upload de arquivo no GC Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


def ultimoAudio(dir_audio):

    list_of_files = glob.glob(dir_audio + '/*')  # * means all if need specific format then *.csv

    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)

    vet = latest_file.split('\\')

    audio_name = vet[1]

    return audio_name

