import os
import requests
from pydub import AudioSegment
from pydub.silence import split_on_silence
import nltk
nltk.download('punkt')

def night_affirmations(text_content, filename_prefix, key, voice_id):
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/IeLNnte4ZJSgJPLpPcem"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "4416030f04da168d96f7faf0ff743f1d",
    }

    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text_content)
    output_files = []

    # Batch the sentences into groups of seven
    for batch_index in range(0, len(sentences), 7):
        batch = sentences[batch_index:batch_index + 7]
        if not batch:
            continue
        
        # Combine sentences into a single text
        batch_text = ' '.join(batch)
        
        data = {
            "text": batch_text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            output_file = f'{filename_prefix}_{batch_index // 7 + 1}.mp3'
            with open(output_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)
            output_files.append(output_file)
        else:
            print(f'Error: {response.status_code}, {response.text}')
    
    # Concatenate all audio files with 20 seconds of silence between each
    combined_audio = AudioSegment.silent(duration=0)
    for output_file in output_files:
        audio = AudioSegment.from_mp3(output_file)
        combined_audio += audio
        combined_audio += AudioSegment.silent(duration=20000)  # 20 seconds of silence
    
    # Export the combined audio
    combined_audio.export(f'{filename_prefix}_combined.mp3', format="mp3")

    # Clean up individual output files
    for output_file in output_files:
        os.remove(output_file)
