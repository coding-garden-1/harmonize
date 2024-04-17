import gradio as gr
import random
import time  # Importing the time module for sleep functionality
device = "cuda"  # Assuming CUDA is being used
version = "svd-xt-1-1"  # Assuming version is a constant
from google.colab import files

def infer(input_path: str, resize_image: bool, n_frames: int, n_steps: int, seed: str, decoding_t: int, fps_id: int, motion_bucket_id: int, cond_aug: float, skip_filter: bool = False) -> str:
    if seed == "random":
        seed = random.randint(0, 2**32)
    if version == "svd-xt-1-1":
        if fps_id != 6:
            print("[WARNING] svd-xt-1-1 was fine-tuned in fixed conditioning (`fps_id=6`, `motion_bucket_id=127`)! The performance may vary compared to SVD 1.0.")
        if motion_bucket_id != 127:
            print("[WARNING] svd-xt-1-1 was fine-tuned in fixed conditioning (`fps_id=6`, `motion_bucket_id=127`)! The performance may vary compared to SVD 1.0.")
    seed = int(seed)
    # Call your sample function here or replace it with appropriate logic
    output_paths = sample(
        input_path=input_path,
        resize_image=resize_image,
        num_frames=n_frames,
        num_steps=n_steps,
        fps_id=fps_id,
        motion_bucket_id=motion_bucket_id,
        cond_aug=cond_aug,
        seed=seed,
        decoding_t=decoding_t,
        device=device,
        skip_filter=skip_filter,
    )
    return output_paths[0]

# No need to prompt user to upload images when loading from current directory

# Iterate over images from image0.png to image6.png
for i in range(7):  
    file_path = f"./image{i}.png"  # Construct file path with prefix "./"
    print("File path:", file_path)
    # Command-line input gathering
    input_path = file_path
    resize_image = True
    n_frames = 25
    n_steps = 30
    seed = 6
    decoding_t = 2
    fps_id = 6
    motion_bucket_id = 127
    cond_aug = 0.02
    skip_filter = True

    # Call infer function with command-line inputs
    output_path = infer(
        input_path=file_path,
        resize_image=resize_image,
        n_frames=n_frames,
        n_steps=n_steps,
        seed=seed,
        decoding_t=decoding_t,
        fps_id=fps_id,
        motion_bucket_id=motion_bucket_id,
        cond_aug=cond_aug,
        skip_filter=skip_filter,
    )
    print("Output video path:", output_path)

    # Introduce a 5-minute delay before processing the next file
    if i < 6:
        print("Waiting for 5 minutes before processing the next file...")
        time.sleep(55)  # 300 seconds = 5 minutes
