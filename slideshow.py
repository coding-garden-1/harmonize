import cv2
import os
from PIL import Image
def make_slideshow(looped_audio_filename):
    def create_video(image_folder, video_name='output_video.mp4', fps=1, duration=10):
        images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]

        temp_dir = os.path.join(image_folder, "temp_images")
        os.makedirs(temp_dir, exist_ok=True)

        print("Saving images to the temporary directory:")
        for image in images:
            img = Image.open(os.path.join(image_folder, image))
            img.save(os.path.join(temp_dir, image))
            print(os.path.join(temp_dir, image))

        frame = cv2.imread(os.path.join(temp_dir, images[0]))
        height, width, layers = frame.shape

        # Explicitly set the FPS when creating the VideoFileClip
        video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        print("Creating video with the following images:")
        for image in images:
            for _ in range(int(fps * duration)):
                video.write(cv2.imread(os.path.join(temp_dir, image)))
            print(os.path.join(temp_dir, image))

        print("Video creation completed.")
        cv2.destroyAllWindows()
        video.release()

        for image in images:
            os.remove(os.path.join(temp_dir, image))
        os.rmdir(temp_dir)

    from datetime import datetime
    import os
    # ...

    def slideshow_videos():
        current_timestamp_formatted = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Adjusted format for a valid filename
        cwd = os.getcwd()  # Get the current working directory
        folders = [folder for folder in os.listdir(cwd) if os.path.isdir(folder)]

        for i, folder in enumerate(folders):
            filename = f"output_Image" + str(i) + '.mp4'
            create_video(folder, filename, fps=1)  # Pass the 'fps' parameter here  

# ...



    import os
    from moviepy.editor import VideoFileClip, concatenate_videoclips
    cwd = os.getcwd()
    def video_concatenator(directory=str(cwd)):
    
        files = os.listdir(directory)
        
        # Filter out only the video files
        video_files = [file for file in files if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".mov")]
        
        # Sort the video files alphabetically
        video_files.sort()
        
        # Create a list to store video clips
        video_clips = []
        
        # Iterate through each video file, create VideoFileClip objects, and append them to the list
        for file in video_files:
            video_clip = VideoFileClip(os.path.join(directory, file))
            for clip in video_clips:
                print(directory)
                # Extract metadata including the title


                # Check if the title key exists in the metadata
                print(f"Clip Duration: {clip.duration} seconds")
                

                # Get frames per second (FPS) information
            

                # Extract metadata including the title
               

            video_clips.append(video_clip)
        print('concatenating all video clips...')
        print(video_clips)
        if video_clips:
            final_clip = concatenate_videoclips(video_clips)
        else:
            print("No video clips to concatenate.")
            return

        # Concatenate all video clips
        print('fps is')
        fpsyay = 1
        print(fpsyay)
        # Write the concatenated video to a file with a specified FPS
        output_file = os.path.join(directory, "concatenated_video.mp4")
        final_clip.write_videofile(output_file, fps=fpsyay)  # Set a valid FPS value
        
        # Close all the video clips
        for clip in video_clips:
            clip.close()
        
        # Close the final clip
        final_clip.close()
        
        print(f"Concatenation complete! Concatenated video saved as {output_file}")


    # Example usage:
    # video_concatenator() # Concatenates videos in the current directory
    # video_concatenator("/path/to/directory") # Concatenates videos in the specified directory

    from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip

    def repeat_video(input_video, output_video, audio_file=None, target_duration=20*60):
        """
        Repeats the input video until its duration reaches the target duration (default 20 minutes).
        
        Parameters:
        - input_video: str, path to the input video file.
        - output_video: str, path to save the output video file.
        - audio_file: str or None, path to the audio file to be used as the audio track (default None).
        - target_duration: int, target duration in seconds (default 20*60 seconds).
        """
        clip = VideoFileClip(input_video)
        original_duration = clip.duration
        num_repeats = int(target_duration / original_duration)
        remaining_duration = target_duration - original_duration * num_repeats

        repeated_clips = [clip] * num_repeats
        if remaining_duration > 0:
            repeated_clips.append(clip.subclip(0, remaining_duration))

        final_clip = concatenate_videoclips(repeated_clips)

        if audio_file is not None:
            audio = AudioFileClip(audio_file)
            final_clip = final_clip.set_audio(audio)

        final_clip.write_videofile(output_video)






    
    slideshow_videos()
    video_concatenator()
    input_video = "concatenated_video.mp4"
    output_video = "Harmonize_Meditation.mp4"
    background_audio = looped_audio_filename
    repeat_video(input_video, output_video, background_audio)