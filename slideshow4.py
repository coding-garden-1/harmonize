import cv2
import os
def make_slideshow(looped_audio_filename):
    # Define the folder names containing the images
       # Get the current working directory
    cwd = os.getcwd()

# Get a list of all files and folders in the current working directory
    items = os.listdir(cwd)

# Filter out only the directories
    folders = [item for item in items if os.path.isdir(os.path.join(cwd, item))]
    folder_names = []
    print("Folders in current working directory:")
    for folder in folders:
        print(folder)
        folder_names += folder     

    if type(folder_names) == 'str': 
        print(str(folder_names))
    # Create a video writer object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 30  # frames per second
    duration = 20  # in seconds
    repeat = 20 * 60  # repeat the video 20 times to make 20 minutes
    output_video = 'output_video.mp4'
    video_writer = cv2.VideoWriter(output_video, fourcc, fps, (0, 0))

    for folder_name in folder_names:
        # Get list of images in the folder
        image_files = os.listdir(folder_name)
        print(image_files)
        image_files.sort()  # Ensure images are sorted in the correct order

        # Read and write each image to the video
        for image_file in image_files:
            image_path = os.path.join(folder_name, image_file)
            print(image_path)
            image = cv2.imread(image_path)

            if image is not None:
                # Get image dimensions
                height, width, _ = image.shape

                # Resize video writer if necessary
                if video_writer.isOpened() and (video_writer.get(3) != width or video_writer.get(4) != height):
                    video_writer.release()
                    video_writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

                # Write the image to the video for the specified duration
                for _ in range(fps * duration // len(image_files)):
                    video_writer.write(image)
                    print('writing an image to file..')
    # Repeat the video
    for _ in range(repeat):
        video_writer.write(image)
        print('repeating video')
    # Release the video writer object
    video_writer.release()
    print('video writer released')
    print('doing ffmpeg..')
    os.system(f'ffmpeg -i {output_video} -i {looped_audio_filename} -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 output_video_with_audio.mp4')
