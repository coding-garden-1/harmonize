import requests
from pydub import AudioSegment
import re

def generate_audio(text_content, filename):
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/qurfk0sJaRdz3LpIIybi"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "6730e95ac0ce0aaada5714c299f58a04"
    }

    data = {
        "text": text_content,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }


    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        with open(f'{filename}.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)

        print(f'Audio file "{filename}.mp3" generated successfully')
        return f'{filename}.mp3'
    else:
        print(f'Error: {response.status_code}, {response.text}')

def concatenate_audio(audio_files, output_filename):
    final_audio = AudioSegment.empty()
    for i, audio_file in enumerate(audio_files):
        audio_segment = AudioSegment.from_file(audio_file)
        final_audio += audio_segment
        # Add twenty seconds of silence after each audio file except the last one
        if i < len(audio_files) - 1 or len(audio_files) == 1:
            final_audio += AudioSegment.silent(duration=20000)

    # Increase the volume by 25%
    final_audio = final_audio + 19

    final_audio.export(output_filename, format="mp3")
    print(f'Concatenated audio saved as "{output_filename}"')

def split_into_sentences(text):
    # Split text into sentences using regular expression
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!|\-)\s', text)
    return sentences

def eleven_labs_voice_generation(text_content, filename):
    sentences = split_into_sentences(text_content)
    audio_files = []

    for i, sentence in enumerate(sentences):
        # Clean up any leading or trailing whitespace
        sentence = sentence.strip()
        if sentence:
            audio_file = generate_audio(sentence, f'{filename}_{i}')
            if audio_file:
                audio_files.append(audio_file)

    if audio_files:
        concatenate_audio(audio_files, f'{filename}_final_output.mp3')

# Example usage:
# text_content = "Your text content goes here."
# eleven_labs_voice_generation(text_content, "meditate")
