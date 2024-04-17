import os

def rename_images_in_folder():
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif']  # List of common image extensions

    # Get a list of all files in the folder
    files = os.listdir("./")
    print(str(files))
    folder_path = "./"

    # Filter out only the image files
    image_files = [file for file in files if os.path.splitext(file)[1].lower() in image_extensions]

    # Rename each image file in the folder
    renamed_files = []
    for i, image_file in enumerate(image_files):
        original_path = os.path.join(folder_path, image_file)
        new_path = os.path.join(folder_path, "image" + str(i) + os.path.splitext(image_file)[1])
        os.rename(original_path, new_path)
        renamed_files.append(new_path)  # Append the renamed file path to the list

    return renamed_files

if __name__ == "__main__":
    print(rename_images_in_folder())
