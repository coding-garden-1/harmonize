from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

def create_combined_clip(folder_path, start_index, end_index, duration):
    clips = []
    pair_duration = duration / (end_index - start_index + 1)  # Duration for each pair
    pair_count = 0

    for i in range(start_index, end_index + 1):
        try:
            # Load video clip
            original_clip = VideoFileClip(f"{folder_path}/{str(i).zfill(6)}.mp4")
            # Create a mirrored version of the clip
            mirrored_clip = original_clip.fx(vfx.time_mirror)
            # Add the original and mirrored clips to the list
            clips.extend([original_clip, mirrored_clip])
            pair_count += 1

            # Break if all pairs are added or if the total duration reaches the desired duration
            if pair_count == (end_index - start_index + 1) or pair_duration * pair_count >= duration:
                break

        except IndexError as e:
            print(f"Error: Index out of range for clip {i}")
            print(e)

    # Concatenate all clips in the list
    final_clip = concatenate_videoclips(clips)
    
    # Resize the final clip to match the desired duration
    final_clip = final_clip.set_duration(duration)

    return final_clip

# Example usage
folder_path = "video_clips_folder"
start_index = 0
end_index = 6
duration = 25
combined_clip = create_combined_clip(folder_path, start_index, end_index, duration)
combined_clip.write_videofile("combined_video.mp4", codec="libx264", audio_codec="aac", bitrate='1000k')
