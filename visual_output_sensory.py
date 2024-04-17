import os
import subprocess
import datetime
from image_folder_maker import image_folder_maker
import os
from PIL import Image


def visualization_image_output_sensory(image_prompts):
    # Create a new folder for this execution
    # Set environment variables
    os.environ["STABILITY_HOST"] = "grpc.stability.ai:443"
    os.environ["STABILITY_KEY"] = "sk-3G2XCkYoceBdSG9sN0PWnmkyN9VabSB9x2gU5Syz2MxkA7q8"
    print("Current working directory:", os.getcwd())
    current_directory = os.getcwd()
    os.system(f'explorer "{current_directory}"')
    # Change directory to the newly created folder

    # Read the content of the file
     
    generated_files = []  # Initialize an empty list to store generated filenames
    
    # Execute commands
    for i, prompt in enumerate(image_prompts):
        subprocess.run(prompt.strip(), shell=True)

        folder_name_1 = f"image_{2*i + 1}"
 
        os.makedirs(folder_name_1, exist_ok=True)
 



        # Create first blank black image
        image_name_1 = f"image.png"
        image_path_1 = os.path.join(folder_name_1, image_name_1)
        width, height = 800, 600
        blank_image_1 = Image.new("RGB", (width, height), color="black")
        blank_image_1.save(image_path_1)
  # Append generated filename to the list

    return generated_files  # Return the list of generated filenames and folder name
