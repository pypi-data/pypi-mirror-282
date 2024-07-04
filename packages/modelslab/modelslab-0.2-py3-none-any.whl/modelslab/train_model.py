import requests
import json
from .helper import BaseHelper

class TrainModel:
    def __init__(self):
        self.base_url = "https://modelslab.com/api/v3"

    def lora_training(self, key, instance_prompt, class_prompt, base_model_type, negative_prompt, images, seed, training_type, max_train_steps, lora_type, webhook=None):
        url = f"{self.base_url}/lora_fine_tune"
        payload = json.dumps({
            "key": key,
            "instance_prompt": instance_prompt,
            "class_prompt": class_prompt,
            "base_model_type": base_model_type,
            "negative_prompt": negative_prompt,
            "images": images,
            "seed": seed,
            "training_type": training_type,
            "max_train_steps": max_train_steps,
            "lora_type": lora_type,
            "webhook": webhook
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def fetch_queued(self, key, training_id):
        url = f"{self.base_url}/fine_tune_status/{training_id}"
        payload = json.dumps({
            "key": key
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def finetune_list(self, key):
        url = f"{self.base_url}/finetune_list"
        payload = json.dumps({
            "key": key
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def delete_training(self, key, training_id):
        url = f"{self.base_url}/finetune/delete/{training_id}"
        payload = json.dumps({
            "key": key
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def cancel_training(self, key, training_id):
        url = f"{self.base_url}/cancle_training/{training_id}"
        payload = json.dumps({
            "key": key
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def base64_crop(self, key, image, crop):
        url = f"{self.base_url}/base64_crop"
        payload = json.dumps({
            "key": key,
            "image": image,
            "crop": crop
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text
