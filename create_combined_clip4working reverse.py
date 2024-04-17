from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, CompositeVideoClip

def create_combined_clip(folder_path, start_index, end_index, duration):
    clips = []
    for i in range(start_index, end_index + 1):
        try:
            # Load video clip
            original_clip = VideoFileClip(f"{folder_path}/{str(i).zfill(6)}.mp4")
            # Create a mirrored version of the clip
            mirrored_clip = original_clip.fx(vfx.time_mirror)
            # Set duration to 25 seconds
            clipped_mirrored_clip = mirrored_clip.subclip(0, duration)
            # Concatenate the original and mirrored clips
            combined_pair = concatenate_videoclips([original_clip, clipped_mirrored_clip])
            clips.append(combined_pair)
        except IndexError as e:
            print(f"Error: Index out of range for clip {i}")
            print(e)

    # Concatenate all pairs
    final_clip = concatenate_videoclips(clips)

    # Add fade in and fade out effects between pairs
    fade_in_out = CompositeVideoClip([final_clip.fadein(1), final_clip.fadeout(1)])

    return fade_in_out

# Example usage
folder_path = "video_clips_folder"
start_index = 0
end_index = 6
duration = 25
combined_clip = create_combined_clip(folder_path, start_index, end_index, duration)
combined_clip.write_videofile("combined_video.mp4", codec="libx264", audio_codec="aac", bitrate='1000k')
