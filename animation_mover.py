import os
import shutil
from pathlib import Path

def move_files_to_directory(target_directory):
    """
    Move files from the downloads folder to the specified target directory.
    """
    # Get the path to the user's downloads folder
    downloads_folder = Path(os.path.expanduser("~")) / "Downloads"

    # Initialize a list to store the filenames
    filenames = []

    # Iterate through files in the downloads folder
    for file_name in os.listdir(downloads_folder):
        # Check if the file exists and is a regular file
        file_path = os.path.join(downloads_folder, file_name)
        if os.path.isfile(file_path):
            # Move the file to the target directory
            shutil.move(file_path, target_directory)
            # Add the filename to the list
            filenames.append(file_name)

    return filenames
