from moviepy.editor import AudioFileClip, VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
import time

def merge_audio_with_video_and_add_subtitles(looped_audio_filename, existing_video_filename, output_filename, timestamp):
    # Load the final audio file
    final_audio = AudioFileClip(looped_audio_filename)
    
    # Load the existing video file
    existing_video = VideoFileClip(existing_video_filename)

    # Set the start time of final_audio to match the start time of existing_video
    final_audio = final_audio.set_start(existing_video.start)

    # Set the volume level for the video (adjust as needed)
    video_volume = 0.1  # 10%
    existing_video = existing_video.volumex(video_volume)

    # Concatenate video clips to loop for 20 minutes
    total_duration = 0
    concatenated_clips = []
    while total_duration < 1200:  # 20 minutes in seconds
        concatenated_clips.append(existing_video)
        total_duration += existing_video.duration
    final_clip = concatenate_videoclips(concatenated_clips, method="compose")

    # Merge the audio with the repeated video
    final_clip = final_clip.set_audio(final_audio)

    # Create timestamp for the output filename
    timestamp = time.strftime("%Y%m%d%H%M%S")

    # Write the merged video to a new file
    merged_filename = f"sensory_meditation_{timestamp}.mp4"
    final_clip.write_videofile(merged_filename, codec="libx264", audio_codec="aac", bitrate='1000k')

    print(f"Merged video saved as: {merged_filename}")

    # Add subtitles to the merged video
    sub_audio = open(looped_audio_filename, "rb")
    subtitles = client.audio.transcriptions.create(
        model="whisper-1", 
        file=sub_audio,
        response_format="srt"
    )
    print('Subtitles generated')
    subtitle_clips = [TextClip(subtitle, fontsize=72, color='white', bg_color='black').set_pos(('center', 'top')).set_duration(final_clip.duration)
                      for subtitle in subtitles.split('\n') if subtitle.strip()]

    video_with_subtitles = CompositeVideoClip([final_clip, *subtitle_clips])

    # Write the final video with subtitles to a new file
    subtitled_filename = f"sensory_meditation_with_subtitles_{timestamp}.mp4"
    video_with_subtitles.write_videofile(subtitled_filename, codec="libx264", audio_codec="aac", bitrate='100k')

    print(f"Video with subtitles saved as: {subtitled_filename}")

# Example usage
merge_audio_with_video_and_add_subtitles("looped_audio.mp3", "existing_video.mp4", "output.mp4", "timestamp")
