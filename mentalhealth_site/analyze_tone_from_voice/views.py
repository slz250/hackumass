from django.shortcuts import render
from django.http import HttpResponse
import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import json
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3

# Create your views here.
def index(request):
    text_from_audio = get_text_from_audio()
    print("******The text converted audio is:$$$$$$$", text_from_audio)
    tone = get_tone(text_from_audio)
    html_response = "<h1>Welome to Voice Analysis, your predicted tone is:"+tone+"</h1>"
    return HttpResponse(html_response)


def get_text_from_audio():
    print('******The current working directory is****:')
    os.system('pwd')
    os.system(
        "export GOOGLE_APPLICATION_CREDENTIALS='analyze_tone_from_voice/Google_cloud_key/My_First_Project_926af8a5744c.json'")
    os.system('ffmpeg -i analyze_tone_from_voice/input.m4a -acodec libmp3lame -ab 128k analyze_tone_from_voice/input.mp3')
    os.system('sox analyze_tone_from_voice/input.mp3 --rate 16k --bits 16 --channels 1 analyze_tone_from_voice/input.flac')

    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    file_name = 'analyze_tone_from_voice/input.flac'

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    # for result in response.results:
    text = response.results[0].alternatives[0].transcript
    # print('Transcript: {}'.format(response.results[0].alternatives[0].transcript))
    # remove audio files
    os.system('rm analyze_tone_from_voice/input.mp3')
    os.system('rm analyze_tone_from_voice/input.flac')
    return text



def get_tone(input):
    tone_analyzer = ToneAnalyzerV3(
        username='d2bb67f8-01c6-46f6-86c3-169179260d14',
        password='ipQZoxFok1Jx',
        version='2016-05-19')



    tones = tone_analyzer.tone(text=input)['document_tone']['tone_categories'][0]['tones']

    tone_name = []
    score = []
    for tone in tones:
        tone_name.append(tone['tone_name'])
        score.append(tone['score'])

    predicted_tone = sorted(zip(tone_name, score), key=lambda x: x[1], reverse=True)

    #print ("The emotion you are feeling is  : ", predicted_tone[0][0])
    tone = predicted_tone[0][0]
    return tone


