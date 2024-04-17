from process_prompts_from_file import process_prompts_from_file
import os
# main.py
from create_combined_clip import create_combined_clip
import audio_recorder
import openai_transcription
import affirmation_generator
import eleven_labs_voice_generation
import audio_looper
#import video_merger_and_subtitler
from audio_recorder import record_audio
from openai_transcription import whisper_transcription
from affirmation_generator import affirmation_generation
from eleven_labs_voice_generation import eleven_labs_voice_generation
#from video_merger_and_subtitler import merge_audio_with_video_and_add_subtitles
from audio_looper import audio_looper
from thumbnail_generator10 import thumbnail_generate
from thumbnail_text import text_maker
from affirmation_visualizer import affirmation_visualizer
from visual_output import visualization_image_output
from move_fonts_to_directory import move_fonts_to_directory 
from meditation_from_tape import meditation_from_tape
from image_renamer import rename_images_in_folder
from output_folder_maker import output_folder_maker
from prompt_refiner import prompt_refiner
import time
from animation_mover import move_files_to_directory
if __name__ == "__main__":
    #folder for animations, prompt text
    folder_name = output_folder_maker()
    print('New folder made.')
    source_dir = "./font"
    
    move_fonts_to_directory(source_dir, folder_name)
    os.chdir(folder_name)
    # Audio record
    record_audio()
    #Whisper transcription;
    transcript = whisper_transcription()
    #affirmation generation
    text_content = affirmation_generation(transcript)
 
    # Filename
    thumbnail_text = text_maker(text_content) 
    filename_full = f"sleep_audio_{thumbnail_text}.mp3"
    filename_meditate = f"daily_meditation_{thumbnail_text}.mp3"
    # 11labs affirmation audio generation; 20 seconds between each
    eleven_labs_voice_generation(text_content, filename_full)
    # thumbnail text
    
    # thumbnail
    thumbnail = thumbnail_generate(thumbnail_text)
    # video_title = title_maker(text_content)
    # 11 hr audio
    tape_choice = input("Do you want a full tape w/ meditation or just meditation? (1 for full, 2 for meditation)")
    if tape_choice == '1':
      looped_audio_filename = audio_looper(filename_full, 11*60)
    elif tape_choice == '2':
      print('Got it')
    else: 
      print('Invalid choice. Restart app for full tape, continuing with meditation for now.')
    # 20 min meditation from tape
    meditation_affirmations = meditation_from_tape(text_content)
    eleven_labs_voice_generation(meditation_affirmations, filename_meditate)
    looped_audio_filename = audio_looper(filename_meditate, 20)
    # stable ai prompts
    
    visual_prompts = affirmation_visualizer(meditation_affirmations, folder_name)
    print('prompts done')
    prompt_refiner()
    textfilepath = './output_text_visual_refined.txt'
    # stable ai creations
    sanitized_prompts=process_prompts_from_file(textfilepath)
    target_directory = os.getcwd()
    visual_images = visualization_image_output(sanitized_prompts)
    rename_images_in_folder()
    print('opening video creator')
    import webbrowser

    # URL of the webpage you want to open
    url = "https://colab.research.google.com/drive/139Pmgv6PoPrplwk_6oqWky8VB98SFfFo"

    # Open the URL in the default web browser
    webbrowser.open(url)

      # Infinite loop to prompt the user until "completed" is entered
    while True:
        user_input = input("Enter 'completed' when animations are completed: ")
        if user_input.lower() == "completed":
            # Call the function to move files to the target directory
            moved_files = move_files_to_directory(target_directory)
            print("Files moved:", moved_files)
            combined_clip = create_combined_clip(moved_files)
            combined_clip.write_videofile("combined_video.mp4", codec="libx264", audio_codec="aac", bitrate='1000k')
            import os

# Get the current working directory
            cwd = os.getcwd()

            # Open File Explorer to the current working directory
            os.startfile(cwd)

            break  # Break out of the loop once "completed" is entered
        else:
            print("c() enter 'completed' to proceed.")

    
    # animations
    #animations = image_to_video(visual_images)
    # Subtitled meditation (Optional)
  #   merge_audio_with_video_and_add_subtitles("./" + looped_audio_filename, "./input/sensory.mp4", str(filename + "_meditation"), timestamp)
    #youtube api upload
    # open audio file
