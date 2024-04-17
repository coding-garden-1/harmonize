import cv2
import subprocess

def two_videos_overlay(video1_path, video2_path, output_path):
    # Load the videos
    video1 = cv2.VideoCapture(video1_path)
    video2 = cv2.VideoCapture(video2_path)

    # Get the frame rate of the videos
    fps1 = video1.get(cv2.CAP_PROP_FPS)
    fps2 = video2.get(cv2.CAP_PROP_FPS)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter(output_path, fourcc, fps1, (int(video1.get(3)), int(video1.get(4))))

    # Initialize variables
    frame_count = 0
    overlay_duration = 6 * fps1
    overlay_interval = 25 * fps1
    overlay_frame_count = 0

    # FFmpeg command to keep audio from both videos
    ffmpeg_cmd = f'ffmpeg -i {video1_path} -i {video2_path} -filter_complex "[0:v] [1:v] overlay=enable=\'lt(mod(t\,25),6*25)\' [outv]; [0:a] [1:a] amix=inputs=2:dropout_transition=0 [outa]" -map "[outv]" -map "[outa]" {output_path}'

    # Main loop to process frames and overlay videos
    while True:
        ret1, frame1 = video1.read()
        ret2, frame2 = video2.read()

        if not ret1 or not ret2:
            break

        frame_count += 1
        overlay_frame_count += 1

        if overlay_frame_count <= overlay_duration:
            # Resize frame2 to match the dimensions of frame1
            frame2_resized = cv2.resize(frame2, (frame1.shape[1], frame1.shape[0]))

            # Remove alpha channel from frame2
            if frame2_resized.shape[2] == 4:  # Check if frame2 has alpha channel
                frame2_resized = frame2_resized[:, :, :3]  # Remove alpha channel

            # Overlay the second video onto the first
            combined_frame = cv2.addWeighted(frame1, 1, frame2_resized, 1.0, 0)
            output.write(combined_frame)
        else:
            output.write(frame1)

        # Toggle overlay every overlay_interval frames
        if overlay_frame_count >= overlay_interval:
            overlay_frame_count = 0

    # Release video objects and close output
    video1.release()
    video2.release()
    output.release()
    cv2.destroyAllWindows()

    # Run FFmpeg command to keep audio from both videos
    subprocess.run(ffmpeg_cmd, shell=True)

# Example usage:
# two_videos_overlay('video1.mp4', 'video2.mp4', 'output.mp4')
