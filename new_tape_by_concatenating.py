
import pydub
from pydub import AudioSegment
from main import filename
from openai_transcription import text_content
import time

def concatenating_with_previous():
    user_input = input("Do you want to generate on top of an existing affirmation tape? (yes/no): ").lower()

    if user_input == 'yes':
        # Load existing file
        existing_file = AudioSegment.from_file("previous.mp3", format="mp3")

        # Your code for generating a new affirmation tape
        new_timestamp = time.strftime("%Y%m%d%H%M%S")
        new_description = text_content[:20].replace(" ", "_")  # Take the first 20 characters and replace spaces with underscores
        new_filename = f"final_output_{new_description}_{new_timestamp}_2.mp3"

        # Assuming you have the new_filename as the second audio file
        # Replace this with your actual code to generate the new tape
        newpart = AudioSegment.from_file(filename, format="mp3")

        # Concatenate the existing file with the new tape
        final_output = existing_file + newpart

        # Save the final output
        final_output.export(new_filename, format="mp3")
        print(f"Final output saved as: {new_filename}")

    else:
        print("No new generation requested.")
    return new_filename
concatenating_with_previous()
