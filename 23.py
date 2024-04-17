from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

def create_combined_clip(folder_path, start_index, end_index, duration):
    clips = []
    for i in range(start_index, end_index + 1):
        # Load video clip
        clip = VideoFileClip(f"{folder_path}/{str(i).zfill(6)}.mp4")
        # Create a clip that plays forwards and then backwards
        combined_clip = concatenate_videoclips([clip, clip.fx(vfx.time_mirror)])
        # Set duration to 25 seconds
        combined_clip = combined_clip.subclip(0, duration)
        clips.append(combined_clip)

    # Add fade in and fade out effects
    clips_with_transition = []
    for i in range(len(clips)):
        clip_with_transition = clips[i].fadein(1).fadeout(1)
        clips_with_transition.append(clip_with_transition)

    # Concatenate clips with transitions if there are more than one clip
    if len(clips_with_transition) > 1:
        final_clip = concatenate_videoclips(clips_with_transition)
    else:
        final_clip = clips_with_transition[0]

    return final_clip

# Example usage
folder_path = "video_clips_folder"
start_index = 0
end_index = 6
duration = 25
combined_clip = create_combined_clip(folder_path, start_index, end_index, duration)
combined_clip.write_videofile("combined_video.mp4", codec="libx264", audio_codec="aac", bitrate='1000k')
