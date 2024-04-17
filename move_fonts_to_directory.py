import os
import shutil

def move_fonts_to_directory(source_directory, destination_directory):
    """
    Copies all font files from the source directory to the destination directory.
    
    Parameters:
        source_directory (str): Path to the source directory containing font files.
        destination_directory (str): Path to the destination directory where font files will be copied.
    
    Returns:
        None
    """
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        print(f"Source directory '{source_directory}' does not exist.")
        return
    
    # Create the destination directory if it does not exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # Get a list of all files in the source directory
    files = os.listdir(source_directory)
    
    # Iterate over the files and copy font files to the destination directory
    for file in files:
        if file.endswith(('.ttf', '.otf', '.woff', '.woff2','.py','.html')):
            source_file = os.path.join(source_directory, file)
            destination_file = os.path.join(destination_directory, file)
            shutil.copy(source_file, destination_file)
