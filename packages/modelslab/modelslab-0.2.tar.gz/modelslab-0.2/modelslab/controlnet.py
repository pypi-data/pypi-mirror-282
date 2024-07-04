import requests
import json
from .helper import BaseHelper

class ControlNet(BaseHelper):
    def __init__(self):
        super().__init__()
        self.route = "v5/controlnet"

    def controlnet_main(self, key, controlnet_type, controlnet_model, model_id, init_image, mask_image=None, control_image=None, auto_hint="yes", width="512", height="512", prompt="", negative_prompt="", guess_mode=None, use_karras_sigmas="yes", algorithm_type=None, safety_checker_type=None, tomesd="yes", vae=None, embeddings=None, lora_strength=None, upscale=None, instant_response=None, strength=1, guidance_scale=7.5, samples="1", safety_checker=None, num_inference_steps="31", controlnet_conditioning_scale=0.4, track_id=None, scheduler="EulerDiscreteScheduler", base64=None, clip_skip="1", temp=None, seed=None, webhook=None):
        url = f"{self.base_url}/{self.route}"
        payload = json.dumps({
            "key": key,
            "controlnet_type": controlnet_type,
            "controlnet_model": controlnet_model,
            "model_id": model_id,
            "init_image": init_image,
            "mask_image": mask_image,
            "control_image": control_image,
            "auto_hint": auto_hint,
            "width": width,
            "height": height,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "guess_mode": guess_mode,
            "use_karras_sigmas": use_karras_sigmas,
            "algorithm_type": algorithm_type,
            "safety_checker_type": safety_checker_type,
            "tomesd": tomesd,
            "vae": vae,
            "embeddings": embeddings,
            "lora_strength": lora_strength,
            "upscale": upscale,
            "instant_response": instant_response,
            "strength": strength,
            "guidance_scale": guidance_scale,
            "samples": samples,
            "safety_checker": safety_checker,
            "num_inference_steps": num_inference_steps,
            "controlnet_conditioning_scale": controlnet_conditioning_scale,
            "track_id": track_id,
            "scheduler": scheduler,
            "base64": base64,
            "clip_skip": clip_skip,
            "temp": temp,
            "seed": seed,
            "webhook": webhook
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def controlnet_multi(self, key, controlnet_model, controlnet_type, model_id, auto_hint="yes", guess_mode="yes", prompt="", negative_prompt=None, control_image=None, init_image=None, mask_image=None, width="512", height="512", samples="1", scheduler="UniPCMultistepScheduler", num_inference_steps="30", safety_checker="no", enhance_prompt="yes", guidance_scale=7.5, controlnet_conditioning_scale=0.7, strength=0.55, lora_model=None, clip_skip="2", tomesd="yes", use_karras_sigmas="yes", vae=None, lora_strength=None, embeddings_model=None, seed=None, webhook=None, track_id=None):
        url = f"{self.base_url}/{self.route}"
        payload = json.dumps({
            "key": key,
            "controlnet_model": controlnet_model,
            "controlnet_type": controlnet_type,
            "model_id": model_id,
            "auto_hint": auto_hint,
            "guess_mode": guess_mode,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "control_image": control_image,
            "init_image": init_image,
            "mask_image": mask_image,
            "width": width,
            "height": height,
            "samples": samples,
            "scheduler": scheduler,
            "num_inference_steps": num_inference_steps,
            "safety_checker": safety_checker,
            "enhance_prompt": enhance_prompt,
            "guidance_scale": guidance_scale,
            "controlnet_conditioning_scale": controlnet_conditioning_scale,
            "strength": strength,
            "lora_model": lora_model,
            "clip_skip": clip_skip,
            "tomesd": tomesd,
            "use_karras_sigmas": use_karras_sigmas,
            "vae": vae,
            "lora_strength": lora_strength,
            "embeddings_model": embeddings_model,
            "seed": seed,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text
