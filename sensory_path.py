import os

def sensory_path():
    # Get the current working directory
    current_dir = os.getcwd()

    # Navigate to the parent directory
    parent_dir = os.path.dirname(current_dir)
    
    try:
        # Construct the path to the file in the parent directory
        file_path = os.path.join(parent_dir, 'sensory_visuals.mp4')

        # Check if the file exists
        if os.path.isfile(file_path):
            return file_path
        else:
            return None
        
        # Navigate back to the current working directory
        os.chdir(current_dir)

    except FileNotFoundError:
        print("Error: Parent directory not found.")
        return None
    except PermissionError:
        print("Error: Permission denied.")
        return None
