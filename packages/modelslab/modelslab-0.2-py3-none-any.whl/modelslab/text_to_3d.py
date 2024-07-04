import requests
import json
from .helper import BaseHelper

class TextTo3D:
    def __init__(self):
        self.base_url = "https://modelslab.com/api/v3"

    def txt_to_3d(self, key, prompt, guidance_scale, steps, frame_size, output_type, webhook=None, track_id=None):
        url = f"{self.base_url}/txt_to_3d"
        payload = json.dumps({
            "key": key,
            "prompt": prompt,
            "guidance_scale": guidance_scale,
            "steps": steps,
            "frame_size": frame_size,
            "output_type": output_type,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def img_to_3d(self, key, image, guidance_scale, steps, frame_size, batch_size, seed, safety_checker, seconds, webhook=None, track_id=None):
        url = f"{self.base_url}/img_to_3d"
        payload = json.dumps({
            "key": key,
            "image": image,
            "guidance_scale": guidance_scale,
            "steps": steps,
            "frame_size": frame_size,
            "batch_size": batch_size,
            "seed": seed,
            "safety_checker": safety_checker,
            "seconds": seconds,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text
