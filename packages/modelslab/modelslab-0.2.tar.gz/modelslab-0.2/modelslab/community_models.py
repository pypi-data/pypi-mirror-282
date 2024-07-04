import requests
import json

class CommunityModels:
    def __init__(self):
        self.base_url = "https://modelslab.com/api/v6/images"

    def txt2img(self, key, model_id, prompt, negative_prompt, width, height, samples, num_inference_steps, safety_checker, enhance_prompt, seed, guidance_scale, multi_lingual, panorama, self_attention, upscale, embeddings_model, lora_model, tomesd, clip_skip, use_karras_sigmas, vae, lora_strength, scheduler, webhook, track_id):
        url = f"{self.base_url}/text2img"
        payload = json.dumps({
            "key": key,
            "model_id": model_id,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "samples": samples,
            "num_inference_steps": num_inference_steps,
            "safety_checker": safety_checker,
            "enhance_prompt": enhance_prompt,
            "seed": seed,
            "guidance_scale": guidance_scale,
            "multi_lingual": multi_lingual,
            "panorama": panorama,
            "self_attention": self_attention,
            "upscale": upscale,
            "embeddings_model": embeddings_model,
            "lora_model": lora_model,
            "tomesd": tomesd,
            "clip_skip": clip_skip,
            "use_karras_sigmas": use_karras_sigmas,
            "vae": vae,
            "lora_strength": lora_strength,
            "scheduler": scheduler,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def lora(self, key, model_id, prompt, negative_prompt, width, height, samples, num_inference_steps, safety_checker, enhance_prompt, seed, guidance_scale, multi_lingual, panorama, self_attention, upscale, embeddings_model, lora_model, lora_strength, scheduler, webhook, track_id):
        url = f"{self.base_url}/text2img"
        payload = json.dumps({
            "key": key,
            "model_id": model_id,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "samples": samples,
            "num_inference_steps": num_inference_steps,
            "safety_checker": safety_checker,
            "enhance_prompt": enhance_prompt,
            "seed": seed,
            "guidance_scale": guidance_scale,
            "multi_lingual": multi_lingual,
            "panorama": panorama,
            "self_attention": self_attention,
            "upscale": upscale,
            "embeddings_model": embeddings_model,
            "lora_model": lora_model,
            "lora_strength": lora_strength,
            "scheduler": scheduler,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def lora_multi(self, key, model_id, prompt, negative_prompt, width, height, samples, num_inference_steps, safety_checker, enhance_prompt, seed, guidance_scale, multi_lingual, panorama, self_attention, upscale, embeddings_model, lora_model, lora_strength, scheduler, webhook, track_id):
        url = f"{self.base_url}/text2img"
        payload = json.dumps({
            "key": key,
            "model_id": model_id,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "samples": samples,
            "num_inference_steps": num_inference_steps,
            "safety_checker": safety_checker,
            "enhance_prompt": enhance_prompt,
            "seed": seed,
            "guidance_scale": guidance_scale,
            "multi_lingual": multi_lingual,
            "panorama": panorama,
            "self_attention": self_attention,
            "upscale": upscale,
            "embeddings_model": embeddings_model,
            "lora_model": lora_model,
            "lora_strength": lora_strength,
            "scheduler": scheduler,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def img2img(self, key, model_id, prompt, negative_prompt, init_image, width, height, samples, num_inference_steps, safety_checker, enhance_prompt, guidance_scale, strength, scheduler, seed, lora_model, tomesd, use_karras_sigmas, vae, lora_strength, embeddings_model, webhook, track_id):
        url = f"{self.base_url}/img2img"
        payload = json.dumps({
            "key": key,
            "model_id": model_id,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "init_image": init_image,
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

    def inpaint(self, key, model_id, prompt, negative_prompt, init_image, mask_image, width, height, samples, steps, safety_checker, enhance_prompt, guidance_scale, strength, scheduler, lora_model, tomesd, use_karras_sigmas, vae, lora_strength, embeddings_model, seed, webhook, track_id):
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
            "steps": steps,
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

    def fetch_queued(self, key, request_id):
        url = f"{self.base_url}/fetch"
        payload = json.dumps({
            "key": key,
            "request_id": request_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def reload_model(self, key, model_id):
        url = f"{self.base_url}/model_reload"
        payload = json.dumps({
            "key": key,
            "model_id": model_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text
