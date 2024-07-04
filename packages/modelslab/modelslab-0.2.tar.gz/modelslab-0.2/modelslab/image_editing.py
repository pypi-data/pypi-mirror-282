import requests
import json
from .helper import BaseHelper

class ImageEditing(BaseHelper):
    def __init__(self):
        super().__init__()
        self.route = "https://modelslab.com/api/v1/image_editing"
        self.headers = {'Content-Type': 'application/json'}

    def super_resolution(self, key, image_url, scale=3, face_enhance=False, webhook=None, track_id=None):
        url = f"{self.route}/super_resolution"
        payload = {
            "key": key,
            "url": image_url,
            "scale": scale,
            "face_enhance": face_enhance,
            "webhook": webhook,
            "track_id": track_id
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def outpaint(self, key, image, prompt, negative_prompt=None, width=512, height=512, as_video=False, seed=1234, webhook=None, track_id=None, height_translation_per_step=64, width_translation_per_step=64, num_inference_steps=15, num_interpolation_steps=32, walk_type=["back", "back", "left","left","up", "up"]):
        url = f"{self.route}/outpaint"
        payload = {
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
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def magic_mix(self, key, image, prompt, negative_prompt=None, width=768, height=768, kmax=0.5, kmin=0.3, samples=1, seed=1829183163, mix_factor=0.5, steps=20, webhook=None, track_id=None):
        url = f"{self.route}/magic_mix"
        payload = {
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
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def depth2img(self, key, init_image, prompt):
        url = f"{self.route}/depth2img"
        payload = {
            "key": key,
            "init_image": init_image,
            "prompt": prompt
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def img_mixer(self, key, init_image, prompt, negative_prompt, width=800, height=600, seed=12345, init_image_weights="0.5,0.7", guidance_scale=10, steps=40, samples=1, webhook=None, track_id=None):
        url = f"{self.route}/img_mixer"
        payload = {
            "key": key,
            "seed": seed,
            "init_image": init_image,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "init_image_weights": init_image_weights,
            "width": width,
            "height": height,
            "guidance_scale": guidance_scale,
            "steps": steps,
            "samples": samples,
            "webhook": webhook,
            "track_id": track_id
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def pix2pix(self, key, init_image, prompt, image_guidance_scale=1, steps=40, guidance_scale=7):
        url = f"{self.route}/pix2pix"
        payload = {
            "key": key,
            "init_image": init_image,
            "prompt": prompt,
            "image_guidance_scale": image_guidance_scale,
            "steps": steps,
            "guidance_scale": guidance_scale
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def removebg(self, key, image, post_process_mask=False, seed=12345, only_mask=False, alpha_matting=False, webhook=None, track_id=None):
        url = f"{self.route}/removebg_mask"
        payload = {
            "key": key,
            "seed": seed,
            "image": image,
            "post_process_mask": post_process_mask,
            "only_mask": only_mask,
            "alpha_matting": alpha_matting,
            "webhook": webhook,
            "track_id": track_id
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def mixture_canvas(self, key, image, prompt, strength=None, guidance_scale=None, base64=None, num_inference_steps=None, mix_factor=None, pos_y2=None, pos_y1=None, pos_x1=None, pos_x2=None, webhook=None, track_id=None):
        url = f"{self.route}/mixture_canvas"
        payload = {
            "key": key,
            "image": image,
            "prompt": prompt,
            "strength": strength,
            "guidance_scale": guidance_scale,
            "num_inference_steps": num_inference_steps,
            'pos_y1': pos_y1,
            'pos_y2': pos_y2,
            'pos_x1': pos_x1,
            'pos_x2': pos_x2,
            "base64": base64,
            "mix_factor": mix_factor,
            "webhook": webhook,
            "track_id": track_id
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def multiview(self, key, image, prompt, width=640, height=960, seed=12345, num_inference_steps=50, guidance_scale=4, temp=False, base64=False, webhook=None, track_id=None):
        url = f"{self.route}/multiview"
        payload = {
            "key": key,
            "seed": seed,
            "image": image,
            "prompt": prompt,
            "width": width,
            "height": height,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "temp": temp,
            "base64": base64,
            "webhook": webhook,
            "track_id": track_id
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def fashion(self, key, init_image, prompt, cloth_image, cloth_type, negative_prompt=None, width=512, height=512, guidance_scale=7.5, num_inference_steps=21, seed=None, temp=False, webhook=None, track_id=None):
        url = f"{self.route}/fashion"
        payload = {
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
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def img_to_text(self, key, init_image, webhook=None, track_id=None):
        url = f"{self.route}/img_to_text"
        payload = {
            "key": key,
            "init_image": init_image,
            "webhook": webhook,
            "track_id": track_id
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def face_gen(self, key, face_image, prompt, negative_prompt=None, width=512, height=512, samples=1, num_inference_steps=21, base64=False, safety_checker=False, safety_checker_type=None, s_scale=None, seed=None, guidance_scale=7.5, webhook=None, track_id=None):
        url = f"{self.route}/face_gen"
        payload = {
            "key": key,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "face_image": face_image,
            "width": width,
            "height": height,
            "samples": samples,
            "num_inference_steps": num_inference_steps,
            "safety_checker": safety_checker,
            "safety_checker_type": safety_checker_type,
            "s_scale": s_scale,
            "base64": base64,
            "seed": seed,
            "guidance_scale": guidance_scale,
            "webhook": webhook,
            "track_id": track_id
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def head_shot(self, key, face_image, prompt, negative_prompt=None, width=512, height=512, samples=1, num_inference_steps=21, base64=False, safety_checker=False, safety_checker_type=None, s_scale=None, seed=None, guidance_scale=7.5, webhook=None, track_id=None):
        url = f"{self.route}/head_shot"
        payload = {
            "key": key,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "face_image": face_image,
            "width": width,
            "height": height,
            "samples": samples,
            "num_inference_steps": num_inference_steps,
            "safety_checker": safety_checker,
            "safety_checker_type": safety_checker_type,
            "s_scale": s_scale,
            "base64": base64,
            "seed": seed,
            "guidance_scale": guidance_scale,
            "webhook": webhook,
            "track_id": track_id
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def inf_edit(self, key, init_image, prompt, source_prompt, source_blend, target_blend, num_inference_steps=15, width=512, height=512, source_blend_thresh=0.8, target_blend_thresh=0.2, strength=0, cross_replace_steps=1, self_replace_steps=1, base64=False, webhook=None, track_id=None):
        url = f"{self.route}/inf_edit"
        payload = {
            "key": key,
            "prompt": prompt,
            "source_prompt": source_prompt,
            "target_blend": target_blend,
            "init_image": init_image,
            "num_inference_steps": num_inference_steps,
            "height": height,
            "width": width,
            "source_blend_thresh": source_blend_thresh,
            "target_blend_thresh": target_blend_thresh,
            "strength": strength,
            "source_blend": source_blend,
            "cross_replace_steps": cross_replace_steps,
            "self_replace_steps": self_replace_steps,
            "base64": base64,
            "webhook": webhook,
            "track_id": track_id
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def inpaint(self, key, init_image, mask_image, prompt, negative_prompt, width=512, height=512, samples=1, num_inference_steps=30, safety_checker=False, enhance_prompt="no", guidance_scale=5, strength=0.7, base64=False, seed=None, webhook=None, track_id=None):
        url = f"{self.route}/inpaint"
        payload = {
            "key": key,
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
            "base64": base64,
            "seed": seed,
            "webhook": webhook,
            "track_id": track_id
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def relight(self, key, init_image, prompt, lighting, negative_prompt=None, width=512, height=512, guidance_scale=7, highres_scale=1.5, lowres_denoise=0.9, highres_denoise=0.5, samples=1, num_inference_steps=20, base64=False, seed=None, webhook=None, track_id=None):
        url = f"{self.route}/relighting"
        payload = {
            "key": key,
            "init_image": init_image,
            "negative_prompt": negative_prompt,
            "lighting": lighting,
            "prompt": prompt,
            "height": height,
            "width": width,
            "samples": samples,
            "guidance_scale": guidance_scale,
            "highres_scale": highres_scale,
            "lowres_denoise": lowres_denoise,
            "highres_denoise": highres_denoise,
            "num_inference_steps": num_inference_steps,
            "seed": seed,
            "base64": base64,
            "webhook": webhook,
            "track_id": track_id
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

    def fetch(self, key, fetch_id):
        endpoint = f"fetch/{fetch_id}"
        url = f"{self.route}/{endpoint}"
        payload = {
            "key": key
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text
