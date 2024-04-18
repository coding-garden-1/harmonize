
import openai
from openai import OpenAI
import os
import time 

import openai 
from openai import OpenAI


def whisper_transcription(key):
    openai.api_key = key
    client = OpenAI(api_key=key)
    audio_file = open("recorded_audio.wav", "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )
    print(str(transcript))
    return transcript
  

   