import requests
import json
from .helper import BaseHelper

class EPGeneral:
    def __init__(self):
        self.base_url = "https://modelslab.com/api/v1/enterprise"

    def update_s3(self, key, deploy_type, public_url, region_name, endpoint_url, aws_access_key_id, aws_secret_access_key, image_directory):
        url = f"{self.base_url}/update_s3"
        payload = json.dumps({
            "key": key,
            "deploy_type": deploy_type,
            "public_url": public_url,
            "region_name": region_name,
            "endpoint_url": endpoint_url,
            "aws_access_key_id": aws_access_key_id,
            "aws_secret_access_key": aws_secret_access_key,
            "image_directory": image_directory
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text
