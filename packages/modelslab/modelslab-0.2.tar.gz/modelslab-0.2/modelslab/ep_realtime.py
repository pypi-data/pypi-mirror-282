import requests
import json
from .helper import BaseHelper

class EPRealtime:
    def __init__(self):
        self.base_url = "https://modelslab.com/api/v1/enterprise/realtime"

    def text2img(self, key, prompt, negative_prompt, width, height, safety_checker, seed=None, samples=1, base64=False, webhook=None, track_id=None):
        url = f"{self.base_url}/text2img"
        payload = json.dumps({
            "key": key,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "safety_checker": safety_checker,
            "seed": seed,
            "samples": samples,
            "base64": base64,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def img2img(self, key, prompt, negative_prompt, init_image, width, height, samples=1, temp=False, safety_checker=False, strength=0.7, seed=None, webhook=None, track_id=None):
        url = f"{self.base_url}/img2img"
        payload = json.dumps({
            "key": key,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "init_image": init_image,
            "width": width,
            "height": height,
            "samples": samples,
            "temp": temp,
            "safety_checker": safety_checker,
            "strength": strength,
            "seed": seed,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def inpaint(self, key, prompt, negative_prompt, init_image, mask_image, width, height, samples=1, safety_checker=False, strength=0.7, base64=False, seed=None, webhook=None, track_id=None):
        url = f"{self.base_url}/inpaint"
        payload = json.dumps({
            "key": key,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "init_image": init_image,
            "mask_image": mask_image,
            "width": width,
            "height": height,
            "samples": samples,
            "safety_checker": safety_checker,
            "strength": strength,
            "base64": base64,
            "seed": seed,
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
