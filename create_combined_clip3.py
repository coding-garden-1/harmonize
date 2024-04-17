from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

def create_combined_clip(folder_path, start_index, end_index, duration):
    clips = []
    for i in range(start_index, end_index + 1):
        try:
            # Load video clip
            clip = VideoFileClip(f"{folder_path}/{str(i).zfill(6)}.mp4")
            # Create a clip that plays forwards and then backwards
            mirrored_clip = clip.fx(vfx.time_mirror)
            # Set duration to 25 seconds
            clipped_mirrored_clip = mirrored_clip.subclip(0, duration)
            clips.append(clipped_mirrored_clip)
        except IndexError as e:
            print(f"Error: Index out of range for clip {i}")
            print(e)

    # Concatenate clips
    final_clip = concatenate_videoclips(clips)

    # Add fade in and fade out effects
    final_clip = final_clip.fadein(1).fadeout(1)

    return final_clip

# Example usage
folder_path = "video_clips_folder"
start_index = 0
end_index = 6
duration = 25
combined_clip = create_combined_clip(folder_path, start_index, end_index, duration)
combined_clip.write_videofile("combined_video.mp4", codec="libx264", audio_codec="aac", bitrate='1000k')
