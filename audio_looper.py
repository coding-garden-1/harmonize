import pydub
from pydub import AudioSegment
def audio_looper(final_audio_filename, tape_minutes):
    final_audio = AudioSegment.from_file(final_audio_filename, format="mp3")
    target_duration_seconds = tape_minutes * 60
    audio_duration_seconds = final_audio.duration_seconds
    repetitions = int(target_duration_seconds / audio_duration_seconds) + 1
    # Repeat the audio accordingly
    
   


    repeated_audio = final_audio
    for _ in range(repetitions - 1):
        repeated_audio += final_audio
        
    # Write the looped audio to a separate file
    looped_audio_filename = f"looped_{final_audio_filename}.mp3"
    repeated_audio.export(looped_audio_filename, format="mp3")
    print(f"Looped audio saved as: {looped_audio_filename}")
    return looped_audio_filename