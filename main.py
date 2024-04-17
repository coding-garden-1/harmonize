import process_prompts_from_file
from process_prompts_from_file import process_prompts_from_file
import os
# main.py
from create_combined_clip import create_combined_clip
import audio_recorder
import openai_transcription
from affirmation_generator import night_transcript_maker
import eleven_labs_voice_generation
import audio_looper
from slideshow import make_slideshow
#import video_merger_and_subtitler
from audio_recorder import record_audio
from openai_transcription import whisper_transcription
import meditate_affirmations
from meditate_affirmations import meditate_affirmations
from eleven_labs_voice_generation import eleven_labs_voice_generation
#from video_merger_and_subtitler import merge_audio_with_video_and_add_subtitles
from audio_looper import audio_looper
from thumbnail_generator10 import thumbnail_generate
from thumbnail_text import text_maker
from affirmation_visualizer import affirmation_visualizer
from visual_output import visualization_image_output
from visual_output_sensory import visualization_image_output_sensory
from move_fonts_to_directory import move_fonts_to_directory 
from meditation_from_tape import meditation_from_tape

from image_renamer import rename_images_in_folder
from image_renamer_sensory import rename_images_in_folder_sensory
from output_folder_maker import output_folder_maker
from prompt_refiner import prompt_refiner
import time
from animation_mover import move_files_to_directory
from sensory_path import sensory_path
from overlay_videos import two_videos_overlay
if __name__ == "__main__":
    
    import webbrowser
    import getpass
    import os
    try:
      with open("openai_key.txt", 'r') as file:
          openai_key = file.read().strip()
    except FileNotFoundError:
      print("Error: openai_key.txt not found.")
      openai_key = None

    try:
      with open("eleven_key.txt", 'r') as file:
          eleven_key = file.read().strip()
    except FileNotFoundError:
      print("Error: eleven_key.txt not found.")
      eleven_key = None

# Open the Eleven Labs website if the user wants a tutorial
    
    response = input("Do you want a tutorial? (yes/no): ").strip().lower()

    if response == "yes":
        # Open the Eleven Labs website
        webbrowser.open("https://elevenlabs.io/app/voice-lab")
        print("Eleven Labs website opened in your web browser.")

        # Open the OpenAI website
        webbrowser.open("https://platform.openai.com/api-keys")
        print("OpenAI website opened in your web browser.")

        # Open the local HTML tutorial file
        tutorial_file = os.path.abspath("tutorial.html")
        webbrowser.open("file://" + tutorial_file)
        print("Tutorial HTML file opened in your web browser.")


    # Prompt the user if they want to use a custom voice ID
    use_custom_voice = input("Do you want to use a custom voice ID? (yes/no): ").strip().lower()

    if use_custom_voice == "yes":
        voice_id = input("Please enter your voice ID: ").strip()

        while len(voice_id) < 14:
              print("Invalid voice ID. It must have at least fourteen characters.")
              use_default_voice = input("Do you want to use the default voice ID? (yes/no): ").strip().lower()
              if use_default_voice == "yes":
                 voice_id = "wCnRUw99XgecKmVCLkeY"
                 break
              else:
                 voice_id = input("Please enter your voice ID: ").strip()
    else:
            voice_id = "wCnRUw99XgecKmVCLkeY"

    #print("Voice ID used:", voice_id)

    
    # Read OpenAI key from file
  
    # Print validity information

    # unnecessary for now

    #folder for animations, prompt text
    folder_name = output_folder_maker()
    source_dir = "./font"
    
    move_fonts_to_directory(source_dir, folder_name)
    os.chdir(folder_name)
    # Audio record
    record_audio()
    #Whisper transcription;
    transcript = whisper_transcription()
    #affirmation generation
    nightly_txt = night_transcript_maker(transcript, str(openai_key)) 
    
    # Filename
    input_string = text_maker(nightly_txt) 
    def remove_whitespace(input_string):
      return input_string.replace(" ", "").replace("\t", "").replace("\n", "")
    
    thumbnail_text = remove_whitespace(input_string)

    meditate_text = meditate_affirmations(nightly_txt, str(openai_key))
    filename_full = f"sleep_audio_{thumbnail_text}.mp3"
    filename_meditate = f"daily_meditation_{thumbnail_text}.mp3"
    #  affirmation audio generation; 20 seconds between each

    eleven_labs_voice_generation(meditate_text, filename_meditate)
    # video_t..itle = title_maker(text_content)
    # '11' hr audio
    tape_choice = input("Do you want a full tape w/ meditation or just meditation? (1 for full, 2 for meditation)")
    if tape_choice == '1':
      print('Got it! This might take a while... press Enter if anything seems stuck')
      eleven_labs_voice_generation(nightly_txt, filename_full)
      filename_full += '_final_output.mp3'
      if input('Want to loop for 10 hours? (yes/no)') == "yes":
        looped_audio_filename = audio_looper(filename_full, 11*60)
      else:
         looped_audio_filename = "looped_" + filename_full
    elif tape_choice == '2':
      print('Got it')
    else: 
      print('Invalid choice. Restart app for full tape, continuing with meditation for now.')
    # 20 min meditation from tape
    filename_meditate+= '_final_output.mp3'
    looped_audio_filename = audio_looper(filename_meditate, 20)
    # stable ai prompts
    
    visual_prompts = affirmation_visualizer(meditate_text, folder_name)
    print('prompts done')
    prompt_refiner()
    textfilepath = './output_text_visual_refined.txt'
    # stable ai creations
    sanitized_prompts=process_prompts_from_file(textfilepath)
    target_directory = os.getcwd()

    user_input = input("Do you want a normal image slideshow meditation or one with sensory visuals? (Type 'yes' or 'no'): ")

    if 'yes' in user_input.lower():
        visual_images = visualization_image_output_sensory(sanitized_prompts)
        print('Opening video creator')
        rename_images_in_folder_sensory()
        choice='y'
    elif 'no' in user_input.lower():
        visual_images = visualization_image_output(sanitized_prompts)
        print('Opening video creator')
        rename_images_in_folder()
        choice='n'
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

    make_slideshow(looped_audio_filename)
    if choice == 'y':
      sensory_video_path = sensory_path()
      two_videos_overlay(str(sensory_video_path), "Harmonize_Meditation.mp4", "Harmonize_Meditation_Sensory.mp4")

    meditating_check = input("Ready to perform a manual nervous system override before adopting a new belief system? (yes/no): ").strip().lower()

    if meditating_check == "yes":
        print("Performing manual nervous system override... This will take five minutes.")
        print("You will feel very calm and ready to take on a new belief system.")
        print("Opening the video...")
        time.sleep(5)  # Sleep for five seconds
        webbrowser.open("https://www.youtube.com/watch?v=ZEFRczhpmJA")
        print("Enjoy your meditation!")
    elif meditating_check == "no":
        print("No problem! Let's continue.")
    else:
        print("Invalid input. Please respond with 'yes' or 'no'.")

    sleep_tape_check = input("Did you produce your nightly sleep tape? (yes/no): ").strip().lower()

    if sleep_tape_check == "yes":
        print("Play this video on at a low volume where it's not too loud to keep you up,")
        print("but you can still hear the words.\n")
        
        print("Although the nighttime sleeping method has not been scientifically proven yet,")
        print("many users have found it makes big changes to sleep with affirmations on at night,")
        print("believing that their subconscious mind can process it while asleep.")
        print("If you want to stick to what's purely scientifically proven,")
        print("stick to daytime meditations which bring confident ideas about yourself into your awareness,")
        print("and you'll find yourself embodying those beliefs in times of distress.")
    elif sleep_tape_check == "no":
        print("That's totally fine! You can still benefit from other methods.")

        print("\nAlthough the nighttime sleeping method has not been scientifically proven yet,")
        print("many users have found it makes big changes to sleep with affirmations on at night,")
        print("believing that their subconscious mind can process it while asleep.")
        print("If you want to stick to what's purely scientifically proven,")
        print("stick to daytime meditations which bring confident ideas about yourself into your awareness,")
        print("and you'll find yourself embodying those beliefs in times of distress.")

    if input("Want your video to be animated? It can take a while but it's worth it. (y/n)") == "y":
    # URL of the webpage you want to open
      time.sleep(4)
      url = "https://colab.research.google.com/drive/139Pmgv6PoPrplwk_6oqWky8VB98SFfFo"
      import webbrowser
      # Open the URL in the default web browser
      webbrowser.open(url)
      animation_tutorial_file = os.path.abspath("animation_tutorial.html")
      webbrowser.open("file://" + animation_tutorial_file)
      print("Tutorial HTML file opened in your web browser.")

        # Infinite loop to prompt the user until "completed" is entered
      while True:
          user_input = input("Enter 'completed' once your videos are in your computers normal downloads folder: ")
          if user_input.lower() == "completed":
              # Call the function to move files to the target directory
              target_directory2 = './'
              moved_files = move_files_to_directory(target_directory2)
              print("Files moved:", moved_files)
              combined_clip = create_combined_clip(looped_audio_filename)
              combined_clip.write_videofile("harmonize_meditation.mp4", codec="libx264", audio_codec="aac", bitrate='1000k')
              import os

  # Get the current working directory
              cwd = os.getcwd()

              # Open File Explorer to the current working directory
              os.startfile(cwd)
              if choice == 'y':
                sensory_video_path = sensory_path()
                two_videos_overlay(str(sensory_video_path), "Harmonize_Meditation.mp4", "Harmonize_Meditation_Sensory.mp4")

              break  # Break out of the loop once "completed" is entered
          else:
              print("c() enter 'completed' to proceed once your videos are in your computers normal downloads folder.")
      
    print("Enjoy your day!")


    
    # animations
    #animations = image_to_video(visual_images)
    # Subtitled meditation (Optional)
  #   merge_audio_with_video_and_add_subtitles("./" + looped_audio_filename, "./input/sensory.mp4", str(filename + "_meditation"), timestamp)
    #youtube api upload
    # open audio file
