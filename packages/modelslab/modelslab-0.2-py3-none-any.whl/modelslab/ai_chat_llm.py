import requests
import json
from .helper import BaseHelper

class AIChatLLM:
    def __init__(self):
        self.base_url = "https://modelslab.com/api/v1/chat_llm"

    def chat(self, key, model_id, system_prompt, prompt, max_new_tokens, do_sample, temperature, top_k, top_p, no_repeat_ngram_size, seed, temp, webhook, track_id):
        url = f"{self.base_url}/chat"
        payload = json.dumps({
            "key": key,
            "model_id": model_id,
            "system_prompt": system_prompt,
            "prompt": prompt,
            "max_new_tokens": max_new_tokens,
            "do_sample": do_sample,
            "temperature": temperature,
            "top_k": top_k,
            "top_p": top_p,
            "no_repeat_ngram_size": no_repeat_ngram_size,
            "seed": seed,
            "temp": temp,
            "webhook": webhook,
            "track_id": track_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def get_chat(self, key, chat_id, temp):
        url = f"{self.base_url}/get_chat"
        payload = json.dumps({
            "key": key,
            "chat_id": chat_id,
            "temp": temp
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def get_queued_response(self, key, chat_id):
        url = f"{self.base_url}/get_queued_response"
        payload = json.dumps({
            "key": key,
            "chat_id": chat_id
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def uncensored_chat(self, key, messages, max_tokens):
        url = f"{self.base_url}/uncensored_chat"
        payload = json.dumps({
            "key": key,
            "messages": messages,
            "max_tokens": max_tokens
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        return response.text
