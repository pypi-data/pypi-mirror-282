import requests
import json
from .helper import BaseHelper

class Miscs:
    def __init__(self):
        self.base_url = "https://modelslab.com/api/v3"

    def base64_crop(self, key, image, crop="true"):
        url = f"{self.base_url}/base64_crop"
        payload = json.dumps({
            "key": key,
            "image": image,
            "crop": crop
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def delete_image(self, key, request_id):
        url = f"{self.base_url}/delete_image"
        payload = json.dumps({
            "key": key,
            "request_id": request_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def finetune_list(self, key):
        url = f"{self.base_url}/finetune_list"
        payload = json.dumps({"key": key})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def dreambooth_model_list(self, key):
        url = f"{self.base_url}/dreambooth/model_list"
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

    def buy_dreambooth_model(self, key, quantity):
        url = f"{self.base_url}/dreambooth/buy_model"
        payload = json.dumps({
            "key": key,
            "quantity": quantity
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def buy_subscription(self, key, plan_name):
        url = f"{self.base_url}/buy_subscription"
        payload = json.dumps({
            "key": key,
            "plan_name": plan_name
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def cancel_subscription(self, key, key_to_cancel):
        url = f"{self.base_url}/cancel_subscription"
        payload = json.dumps({
            "key": key,
            "key_to_cancel": key_to_cancel
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def nsfw_image_check(self, key, init_image):
        url = f"{self.base_url}/nsfw_image_check"
        payload = json.dumps({
            "key": key,
            "init_image": init_image
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def load_model(self, key, url, model_id, revision, force_load, model_category, model_format, model_visibility, model_name, model_image, hf_upload):
        url = f"{self.base_url}/load_model"
        payload = json.dumps({
            "key": key,
            "url": url,
            "model_id": model_id,
            "revision": revision,
            "force_load": force_load,
            "model_category": model_category,
            "model_format": model_format,
            "model_visibility": model_visibility,
            "model_name": model_name,
            "model_image": model_image,
            "hf_upload": hf_upload
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def interior(self, key, init_image, prompt, num_inference_steps, base64, guidance_scale):
        url = f"{self.base_url}/interior"
        payload = json.dumps({
            "key": key,
            "init_image": init_image,
            "prompt": prompt,
            "num_inference_steps": num_inference_steps,
            "base64": base64,
            "guidance_scale": guidance_scale
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text
