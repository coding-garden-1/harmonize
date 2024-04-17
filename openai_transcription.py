
import openai
from openai import OpenAI
import os
import time 

import openai 
from openai import OpenAI
client = OpenAI(
    api_key='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',
)
def whisper_transcription():
    openai.api_key = "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"
    audio_file = open("recorded_audio.wav", "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )
    print(str(transcript))
    return transcript
  

   