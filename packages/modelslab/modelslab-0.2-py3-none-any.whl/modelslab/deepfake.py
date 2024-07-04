import requests
import json
from .helper import BaseHelper

class Deepfake:
    def __init__(self):
        self.base_url = "https://modelslab.com/api/v6/deepfake"

    def single_face_swap(self, key, init_image, target_image, webhook=None, track_id=None):
        url = f"{self.base_url}/single_face_swap"
        payload = json.dumps({
            "key": key,
            "init_image": init_image,
            "target_image": target_image,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def multiple_face_swap(self, key, init_image, target_image, webhook=None, track_id=None):
        url = f"{self.base_url}/multiple_face_swap"
        payload = json.dumps({
            "key": key,
            "init_image": init_image,
            "target_image": target_image,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def single_video_swap(self, key, init_image, init_video, webhook=None, track_id=None):
        url = f"{self.base_url}/single_video_swap"
        payload = json.dumps({
            "key": key,
            "init_image": init_image,
            "init_video": init_video,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def specific_video_swap(self, key, init_video, init_image, reference_frame_number, webhook=None, track_id=None):
        url = f"{self.base_url}/specific_video_swap"
        payload = json.dumps({
            "key": key,
            "init_video": init_video,
            "init_image": init_image,
            "reference_frame_number": reference_frame_number,
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
