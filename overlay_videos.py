import cv2
def two_videos_overlay():
    # Load the videos
    video1 = cv2.VideoCapture('video1.mp4')
    video2 = cv2.VideoCapture('video2.mp4')

    # Get the frame rate of the videos
    fps1 = video1.get(cv2.CAP_PROP_FPS)
    fps2 = video2.get(cv2.CAP_PROP_FPS)


    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter('output.mp4', fourcc, fps1, (int(video1.get(3)), int(video1.get(4))))

    # Loop through frames of video1 and overlay frames of video2
    while True:
        ret1, frame1 = video1.read()
        ret2, frame2 = video2.read()

        if not ret1 or not ret2:
            break

        # Resize frame2 to match the dimensions of frame1
        frame2_resized = cv2.resize(frame2, (frame1.shape[1], frame1.shape[0]))

        # Convert frame2 to grayscale
        frame2_gray = cv2.cvtColor(frame2_resized, cv2.COLOR_BGR2GRAY)

        # Create a mask by thresholding frame2
        _, mask = cv2.threshold(frame2_gray, 1, 255, cv2.THRESH_BINARY)

        # Invert the mask
        mask_inv = cv2.bitwise_not(mask)

        # Extract regions from frames
        frame1_bg = cv2.bitwise_and(frame1, frame1, mask=mask_inv)
        frame2_fg = cv2.bitwise_and(frame2_resized, frame2_resized, mask=mask)

        # Combine the frames
        combined_frame = cv2.add(frame1_bg, frame2_fg)
        output.write(combined_frame)

    # Release video objects and close output
    video1.release()
    video2.release()
    output.release()
    cv2.destroyAllWindows()
