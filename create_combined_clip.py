import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip

def create_combined_clip(audio_file_path=None):
    clips = []
    
    start_index = 0
    end_index = 6
    duration = 25
    loop_duration = 20 * 60  # 20 minutes in seconds

    while sum([clip.duration for clip in clips]) < loop_duration:
        for i in range(start_index, end_index + 1):
            try:
                # Load video clip
                folder_path = "./"  # Update with the path to your folder containing video clips
                original_clip = VideoFileClip(f"{folder_path}/{str(i).zfill(6)}.mp4")
                # Create a mirrored version of the clip
                mirrored_clip = original_clip.fx(vfx.time_mirror)
                total_duration = 0
                
                # Iterate until the duration reaches loop_duration
                while total_duration < duration and sum([clip.duration for clip in clips]) < loop_duration:
                    pair_duration = min(original_clip.duration, duration - total_duration)
                    # Add the original and mirrored clips to the list
                    clips.extend([original_clip.subclip(0, pair_duration), mirrored_clip.subclip(0, pair_duration)])
                    total_duration += pair_duration * 2  # Each pair adds twice the duration

            except IndexError as e:
                print(f"Error: Index out of range for clip {i}")
                print(e)

    # Concatenate all clips in the list
    final_clip = concatenate_videoclips(clips)

    # If an audio file is provided, add it to the final video
    if audio_file_path and os.path.exists(audio_file_path):
        audio_clip = AudioFileClip(audio_file_path)
        final_clip = final_clip.set_audio(audio_clip)

    # Export the final clip to a video file in the current working directory
    final_clip.write_videofile("looped_video.mp4", fps=24)

  # Update with the path to your audio file
