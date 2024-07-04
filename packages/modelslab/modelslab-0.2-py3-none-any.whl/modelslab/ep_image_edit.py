import requests
import json
from .helper import BaseHelper

class EPImageEdit:
    def __init__(self):
        self.base_url = "https://modelslab.com/api/v1/enterprise/image_editing"

    def outpaint(self, key, seed, width, height, prompt, image, negative_prompt, height_translation_per_step, width_translation_per_step, num_inference_steps, as_video=False, num_interpolation_steps=32, walk_type=None, webhook=None, track_id=None):
        url = f"{self.base_url}/outpaint"
        payload = json.dumps({
            "key": key,
            "seed": seed,
            "width": width,
            "height": height,
            "prompt": prompt,
            "image": image,
            "negative_prompt": negative_prompt,
            "height_translation_per_step": height_translation_per_step,
            "width_translation_per_step": width_translation_per_step,
            "num_inference_steps": num_inference_steps,
            "as_video": as_video,
            "num_interpolation_steps": num_interpolation_steps,
            "walk_type": walk_type,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def blip_diffusion(self, key, seed, task, prompt, condition_image, condition_subject, target_subject, guidance_scale, steps, height, width, webhook=None, track_id=None):
        url = f"{self.base_url}/blip_diffusion"
        payload = json.dumps({
            "key": key,
            "seed": seed,
            "task": task,
            "prompt": prompt,
            "condition_image": condition_image,
            "condition_subject": condition_subject,
            "target_subject": target_subject,
            "guidance_scale": guidance_scale,
            "steps": steps,
            "height": height,
            "width": width,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def magic_mix(self, key, prompt, height, width, image, kmax, kmin, mix_factor, samples, negative_prompt, seed, steps, webhook=None, track_id=None):
        url = f"{self.base_url}/magic_mix"
        payload = json.dumps({
            "key": key,
            "prompt": prompt,
            "height": height,
            "width": width,
            "image": image,
            "kmax": kmax,
            "kmin": kmin,
            "mix_factor": mix_factor,
            "samples": samples,
            "negative_prompt": negative_prompt,
            "seed": seed,
            "steps": steps,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def removebg_mask(self, key, seed, image, post_process_mask=False, only_mask=False, alpha_matting=False, webhook=None, track_id=None):
        url = f"{self.base_url}/removebg_mask"
        payload = json.dumps({
            "key": key,
            "seed": seed,
            "image": image,
            "post_process_mask": post_process_mask,
            "only_mask": only_mask,
            "alpha_matting": alpha_matting,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def multi_view(self, key, seed, image, prompt, width, height, num_inference_steps, guidance_scale, temp="no", webhook=None, track_id=None):
        url = f"{self.base_url}/multiview"
        payload = json.dumps({
            "key": key,
            "seed": seed,
            "image": image,
            "prompt": prompt,
            "width": width,
            "height": height,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "temp": temp,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def fashion(self, key, prompt, negative_prompt, init_image, cloth_image, cloth_type, height, width, guidance_scale, num_inference_steps, seed=None, temp="no", webhook=None, track_id=None):
        url = f"{self.base_url}/fashion"
        payload = json.dumps({
            "key": key,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "init_image": init_image,
            "cloth_image": cloth_image,
            "cloth_type": cloth_type,
            "height": height,
            "width": width,
            "guidance_scale": guidance_scale,
            "num_inference_steps": num_inference_steps,
            "seed": seed,
            "temp": temp,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def face_gen(self, key, prompt, negative_prompt, face_image, width, height, samples, num_inference_steps, safety_checker=False, base64=False, seed=None, guidance_scale=7.5, webhook=None, track_id=None):
        url = f"{self.base_url}/face_gen"
        payload = json.dumps({
            "key": key,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "face_image": face_image,
            "width": width,
            "height": height,
            "samples": samples,
            "num_inference_steps": num_inference_steps,
            "safety_checker": safety_checker,
            "base64": base64,
            "seed": seed,
            "guidance_scale": guidance_scale,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def fetched_queue(self, key, id):
        url = f"{self.base_url}/fetch/{id}"
        payload = json.dumps({"key": key})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def head_shot(self, key, prompt, negative_prompt, face_image, width, height, samples, num_inference_steps, safety_checker=False, base64=False, seed=None, guidance_scale=7.5, webhook=None, track_id=None):
        url = f"{self.base_url}/head_shot"
        payload = json.dumps({
            "key": key,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "face_image": face_image,
            "width": width,
            "height": height,
            "samples": samples,
            "num_inference_steps": num_inference_steps,
            "safety_checker": safety_checker,
            "base64": base64,
            "seed": seed,
            "guidance_scale": guidance_scale,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def restart_server(self, key):
        url = f"{self.base_url}/restart_server"
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

    def relighting(self, key, init_image, lighting, prompt, height, width, samples, base64=False, webhook=None, track_id=None):
        url = f"{self.base_url}/relighting"
        payload = json.dumps({
            "key": key,
            "init_image": init_image,
            "lighting": lighting,
            "prompt": prompt,
            "height": height,
            "width": width,
            "samples": samples,
            "base64": base64,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text
