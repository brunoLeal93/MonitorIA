
"""Asynchronously transcribes the audio file specified by the gcs_uri."""
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

gcs_uri= 'gs://ligacoes_gravadas/OP000209092018.flac'



def transcribe(gcs_uri):

    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='pt-BR')

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = operation.result()
    audio_transcrito = []
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))
        # print('Confidence: {}'.format(result.alternatives[0].confidence))

        audio_transcrito.append(result.alternatives[0].transcript)

    return audio_transcrito
