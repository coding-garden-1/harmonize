import os
def process_prompts_from_file(file_path):
    
    """
    Process prompts from a text file and return a sanitized list of filenames.
    
    Parameters:
        file_path (str): Path to the text file containing prompts.
    
    Returns:
        list: List of sanitized filenames.
    """
    def sanitize_filename(filename):
        """
        Sanitizes a filename by removing invalid characters.
        
        Parameters:
            filename (str): The original filename.
        
        Returns:
            str: The sanitized filename.
        """
        invalid_chars = '\\/:*?"<>|'
        sanitized_filename = ''.join(c for c in filename if c not in invalid_chars)
        return sanitized_filename

    # Read the content of the file
    with open(file_path, 'r') as file:
        image_prompts = file.readlines()

    # Sanitize each prompt to create filenames
    sanitized_filenames = [sanitize_filename(prompt.strip()) for prompt in image_prompts]

    return sanitized_filenames  # Return the list of sanitized filenames
