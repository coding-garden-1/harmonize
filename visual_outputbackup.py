import subprocess
import os

def visualization_image_output(file_path):
    # Set environment variables
    os.environ["STABILITY_HOST"] = "grpc.stability.ai:443"
    os.environ["STABILITY_KEY"] = "sk-3G2XCkYoceBdSG9sN0PWnmkyN9VabSB9x2gU5Syz2MxkA7q8"

    # Read the content of the file
    with open(file_path, 'r') as file:
        image_prompts = file.readlines()

    generated_files = []  # Initialize an empty list to store generated filenames

    # Execute commands
    for prompt in image_prompts:
        subprocess.run(prompt.strip(), shell=True)
        generated_files.append('generation_' + file_path + '.png')  # Append generated filename to the list

    return generated_files  # Return the list of generated filenames
