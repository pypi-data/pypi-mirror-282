import requests
import json
from .helper import BaseHelper

class AIVoiceAndAudio:
    def __init__(self):
        self.base_url = "https://modelslab.com/api/v1/voice_and_audio"

    def text_to_audio(self, key, prompt, init_audio, language, webhook, track_id):
        url = f"{self.base_url}/text_to_audio"
        payload = json.dumps({
            "key": key,
            "prompt": prompt,
            "init_audio": init_audio,
            "language": language,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def voice_to_voice(self, key, init_audio, target_audio, temp, base64, webhook, track_id):
        url = f"{self.base_url}/voice_to_voice"
        payload = json.dumps({
            "key": key,
            "init_audio": init_audio,
            "target_audio": target_audio,
            "temp": temp,
            "base64": base64,
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

    def voice_cover(self, key, init_audio, model_id, pitch, rate, radius, mix, algorithm, hop_length, originality, lead_voice_volume_delta, backup_voice_volume_delta, instrument_volume_delta, reverb_size, wetness, dryness, damping, base64, temp, webhook, track_id):
        url = f"{self.base_url}/voice_cover"
        payload = json.dumps({
            "key": key,
            "init_audio": init_audio,
            "model_id": model_id,
            "pitch": pitch,
            "rate": rate,
            "radius": radius,
            "mix": mix,
            "algorithm": algorithm,
            "hop_length": hop_length,
            "originality": originality,
            "lead_voice_volume_delta": lead_voice_volume_delta,
            "backup_voice_volume_delta": backup_voice_volume_delta,
            "instrument_volume_delta": instrument_volume_delta,
            "reverb_size": reverb_size,
            "wetness": wetness,
            "dryness": dryness,
            "damping": damping,
            "base64": base64,
            "temp": temp,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def voice_upload(self, key, name, init_audio, language):
        url = f"{self.base_url}/voice_upload"
        payload = json.dumps({
            "key": key,
            "name": name,
            "init_audio": init_audio,
            "language": language
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def music_gen(self, key, prompt, init_audio, sampling_rate, base64, temp, webhook, track_id):
        url = f"{self.base_url}/music_gen"
        payload = json.dumps({
            "key": key,
            "prompt": prompt,
            "init_audio": init_audio,
            "sampling_rate": sampling_rate,
            "base64": base64,
            "temp": temp,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text
