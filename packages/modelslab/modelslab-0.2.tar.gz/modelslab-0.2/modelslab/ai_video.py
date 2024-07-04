import requests
import json
from .helper import BaseHelper

class AIVideo:
    def __init__(self):
        self.base_url = "https://modelslab.com/api/v6/video"

    def open_sora(self, key, prompt, height, width, num_frames, fps, webhook=None, track_id=None):
        url = f"{self.base_url}/open_sora"
        payload = json.dumps({
            "key": key,
            "prompt": prompt,
            "height": height,
            "width": width,
            "num_frames": num_frames,
            "fps": fps,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def scene_creator(self, key, prompts, prompt_durations, animations, negative_prompt, height, width, temp="yes"):
        url = f"{self.base_url}/scene_creator"
        payload = json.dumps({
            "key": key,
            "prompts": prompts,
            "prompt_durations": prompt_durations,
            "animations": animations,
            "negative_prompt": negative_prompt,
            "height": height,
            "width": width,
            "temp": temp
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def text2video(self, key, model_id, prompt, negative_prompt, height, width, num_frames, num_inference_steps, guidance_scale, upscale_height, upscale_width, upscale_strength, upscale_guidance_scale, upscale_num_inference_steps, output_type, webhook=None, track_id=None):
        url = f"{self.base_url}/text2video"
        payload = json.dumps({
            "key": key,
            "model_id": model_id,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "height": height,
            "width": width,
            "num_frames": num_frames,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "upscale_height": upscale_height,
            "upscale_width": upscale_width,
            "upscale_strength": upscale_strength,
            "upscale_guidance_scale": upscale_guidance_scale,
            "upscale_num_inference_steps": upscale_num_inference_steps,
            "output_type": output_type,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def img2video(self, key, model_id, init_image, height, width, num_frames, num_inference_steps, min_guidance_scale, max_guidance_scale, motion_bucket_id, noise_aug_strength, base64=False, webhook=None, track_id=None):
        url = f"{self.base_url}/img2video"
        payload = json.dumps({
            "key": key,
            "model_id": model_id,
            "init_image": init_image,
            "height": height,
            "width": width,
            "num_frames": num_frames,
            "num_inference_steps": num_inference_steps,
            "min_guidance_scale": min_guidance_scale,
            "max_guidance_scale": max_guidance_scale,
            "motion_bucket_id": motion_bucket_id,
            "noise_aug_strength": noise_aug_strength,
            "base64": base64,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def fetch_queued(self, key, id):
        url = f"{self.base_url}/fetch/{id}"
        payload = json.dumps({"key": key})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def system_details(self, key):
        url = f"{self.base_url}/system_details"
        payload = json.dumps({"key": key})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def restart_server(self, key):
        url = f"{self.base_url}/restart_server"
        payload = json.dumps({"key": key})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def update_server(self, key):
        url = f"{self.base_url}/update_server"
        payload = json.dumps({"key": key})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def clear_cache(self, key):
        url = f"{self.base_url}/clear_cache"
        payload = json.dumps({"key": key})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text
