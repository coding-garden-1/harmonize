import torch
from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video
from GPUtil import showUtilization as gpu_usage
import gc

def image_to_video(image_filenames):
    for imagefilename in image_filenames:
        pipe = StableVideoDiffusionPipeline.from_pretrained(
            "stabilityai/stable-video-diffusion-img2vid-xt", torch_dtype=torch.float16, variant="fp16"
        )
        #pipe.enable_model_cpu_offload()
        pipe.to(0) # Force to GPU

        # Load the conditioning image
        image = load_image(imagefilename)
        image = image.resize((1024, 576))

        generator = torch.manual_seed(42)

        # Perform GPU memory cleanup
        gc.collect()
        torch.cuda.empty_cache()
        gpu_usage()

        frames = pipe(image, decode_chunk_size=3, generator=generator, num_frames=10, motion_bucket_id=180, noise_aug_strength=0.3).frames[0]

        export_to_video(frames, str(imagefilename) + "_generated.mp4", fps=7)
