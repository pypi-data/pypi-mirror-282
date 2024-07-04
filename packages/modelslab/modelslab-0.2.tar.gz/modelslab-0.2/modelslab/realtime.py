import requests
import json
from .helper import BaseHelper

class RealTime(BaseHelper):
   
    def __init__(self):
      super().__init__()
<<<<<<< HEAD
      self.route = "v6/realtime"


    def text2img(self, key, prompt, negative_prompt=None, width=512, height=512, safety_checker=False, seed=None, samples=1, base64=False, webhook=None, track_id=None):
        url = f"{self.base_url}/{self.route}/text2img" 
=======
      self.route = f"{self.base_url}/v6/realtime"


    def text2img(self, key, prompt, negative_prompt=None, width=512, height=512, safety_checker=False, seed=None, samples=1, base64=False, webhook=None, track_id=None):
        url = f"{self.route}/text2img" 
>>>>>>> 3a32d04ecbee63db344d85a0533c561d80777832
        payload = {
            "key": key,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": str(width),
            "height": str(height),
            "safety_checker": safety_checker,
            "seed": seed,
            "samples": samples,
            "base64": base64,
            "webhook": webhook,
            "track_id": track_id
        }

<<<<<<< HEAD
       
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))

        return response.text
    
    def img2img():
        pass
=======
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        return response.text
    
    def img2img(self, key, init_image, prompt, negative_prompt=None, width=512, height=512, samples=1, temp= False, safety_checker=False, base64=False, enhance_style=None, enhance_prompt=False, strength = 0.7, seed=None, webhook=None, trace_id=None):
        url = f"{self.route}/img2img"
        payload= {
            "key": key,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "init_image": init_image,
            "width": width,
            "height": height,
            "samples": samples,
            "base64": base64,
            "temp": temp,
            "safety_checker": safety_checker,
            "strength":strength,
            "enhance_prompt": enhance_prompt,
            "enhance_style" : enhance_style,
            "seed": seed,
            "webhook": webhook,
            "track_id": trace_id
            }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text
    

    def inpaint(self, key, init_image, mask_image, prompt, negative_prompt=None, width=512, height=512, enhance_prompt=False, enhance_style =None, safety_checker=False, strength=0.7, base64=False, samples=1, seed=None, webhook=None, track_id=None):
        url = f"{self.route}/inpaint"
        payload = {
            "key": key,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "init_image": init_image,
            "mask_image":  mask_image,
            "width": width,
            "height": height,
            "samples": samples,
            "safety_checker": safety_checker,
            "strength": strength,
            "base64": base64,
            "seed": seed,
            "webhook": webhook,
            "track_id": track_id
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text
    
    
    def fetch(self, key, fetch_id):
        url= f"{self.route}/fetch/{fetch_id}"
        payload = {
            "key": key
        }
        response = requests.post(url=url, headers=self.headers, data=json.dumps(payload))
        return response.text

>>>>>>> 3a32d04ecbee63db344d85a0533c561d80777832

