import requests
import json
from .helper import BaseHelper

class EPTxt2Img:
    def __init__(self):
        self.base_url = "https://modelslab.com/api/v1/enterprise/txt2img"

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

    def schedulers_list(self, key):
        url = f"{self.base_url}/schedulers_list"
        payload = json.dumps({"key": key})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def load_model_v2(self, key, url, model_id, model_category, model_format, webhook, revision):
        url = f"{self.base_url}/load_model_v2"
        payload = json.dumps({
            "key": key,
            "url": url,
            "model_id": model_id,
            "model_category": model_category,
            "model_format": model_format,
            "webhook": webhook,
            "revision": revision
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def load_model(self, key, url, model_id, model_type, from_safetensors, webhook, revision, upcast_attention):
        url = f"{self.base_url}/load_model"
        payload = json.dumps({
            "key": key,
            "url": url,
            "model_id": model_id,
            "model_type": model_type,
            "from_safetensors": from_safetensors,
            "webhook": webhook,
            "revision": revision,
            "upcast_attention": upcast_attention
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def verify_model(self, key, model_id):
        url = f"{self.base_url}/verify_model"
        payload = json.dumps({
            "key": key,
            "model_id": model_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def get_all_models(self, key):
        url = f"{self.base_url}/get_all_models"
        payload = json.dumps({"key": key})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def delete_model(self, key, model_id):
        url = f"{self.base_url}/delete_model"
        payload = json.dumps({
            "key": key,
            "model_id": model_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def controlnet(self, key, controlnet_model, controlnet_type, model_id, auto_hint, guess_mode, prompt, negative_prompt, init_image, mask_image, width, height, samples, scheduler, num_inference_steps, safety_checker, enhance_prompt, guidance_scale, strength, seed, webhook, track_id):
        url = f"{self.base_url}/controlnet"
        payload = json.dumps({
            "key": key,
            "controlnet_model": controlnet_model,
            "controlnet_type": controlnet_type,
            "model_id": model_id,
            "auto_hint": auto_hint,
            "guess_mode": guess_mode,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "init_image": init_image,
            "mask_image": mask_image,
            "width": width,
            "height": height,
            "samples": samples,
            "num_inference_steps": num_inference_steps,
            "safety_checker": safety_checker,
            "enhance_prompt": enhance_prompt,
            "guidance_scale": guidance_scale,
            "strength": strength,
            "scheduler": scheduler,
            "lora_model": lora_model,
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

    def inpaint(self, key, model_id, prompt, negative_prompt, init_image, mask_image, width, height, samples, num_inference_steps, safety_checker, enhance_prompt, guidance_scale, strength, scheduler, seed, lora_model, tomesd, use_karras_sigmas, vae, lora_strength, embeddings_model, webhook, track_id):
        url = f"{self.base_url}/inpaint"
        payload = json.dumps({
            "key": key,
            "model_id": model_id,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "init_image": init_image,
            "mask_image": mask_image,
            "width": width,
            "height": height,
            "samples": samples,
            "num_inference_steps": num_inference_steps,
            "safety_checker": safety_checker,
            "enhance_prompt": enhance_prompt,
            "guidance_scale": guidance_scale,
            "strength": strength,
            "scheduler": scheduler,
            "seed": seed,
            "lora_model": lora_model,
            "tomesd": tomesd,
            "use_karras_sigmas": use_karras_sigmas,
            "vae": vae,
            "lora_strength": lora_strength,
            "embeddings_model": embeddings_model,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def super_resolution(self, key, url, scale, webhook, face_enhance):
        url = f"{self.base_url}/super_resolution"
        payload = json.dumps({
            "key": key,
            "url": url,
            "scale": scale,
            "webhook": webhook,
            "face_enhance": face_enhance
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def upload_image(self, key, base64_image, image_type):
        url = f"{self.base_url}/upload_image"
        payload = json.dumps({
            "key": key,
            "base64_image": base64_image,
            "image_type": image_type
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def sync_models(self, key, sync_key):
        url = f"{self.base_url}/sync_models"
        payload = json.dumps({
            "key": key,
            "sync_key": sync_key
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def load_vae(self, key, webhook, vae_id, vae_url, vae_type):
        url = f"{self.base_url}/load_vae"
        payload = json.dumps({
            "key": key,
            "webhook": webhook,
            "vae_id": vae_id,
            "vae_url": vae_url,
            "vae_type": vae_type
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

    def fetch_queued(self, key, request_id):
        url = f"{self.base_url}/fetch"
        payload = json.dumps({
            "key": key,
            "request_id": request_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

     
