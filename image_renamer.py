import os

def rename_images_in_folder():
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif']  # List of common image extensions

    # Get a list of all files in the folder
    files = os.listdir("./")
    folder_path = "./"

    # Filter out only the image files
    image_files = [file for file in files if os.path.splitext(file)[1].lower() in image_extensions]

    # Create a folder and move each image file into its own folder named "image"
    for i, image_file in enumerate(image_files):
        image_folder = f"image_{i}"
        os.makedirs(image_folder, exist_ok=True)
        original_path = os.path.join(folder_path, image_file)
        new_path = os.path.join(folder_path, image_folder, "image.png")
        os.rename(original_path, new_path)

    return ["image.png" for _ in range(len(image_files))]  # Return the list of generated filenames
