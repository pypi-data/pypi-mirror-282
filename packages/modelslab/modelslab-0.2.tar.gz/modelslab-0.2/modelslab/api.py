import requests
import json
from .controlnet import ControlNet
from .miscs import Miscs
from .ai_video import AIVideo
from .deepfake import Deepfake
from .ep_general import EPGeneral
from .ep_realtime import EPRealtime
from .ep_image_edit import EPImageEdit
from .ep_video import EPVideo
from .image_editing import ImageEditing
from .ai_voice_and_audio import AIVoiceAndAudio
from .ai_chat_llm import AIChatLLM
from .ep_txt2img import EPTxt2Img
from .ep_voice_cloning import EPVoiceCloning
from .community_models import CommunityModels
from .train_model import TrainModel
from .text_to_3d import TextTo3D

class ModelsLab:
    def __init__(self):
        self.controlnet = ControlNet()
        self.miscs = Miscs()
        self.ai_video = AIVideo()
        self.deepfake = Deepfake()
        self.ep_general = EPGeneral()
        self.ep_realtime = EPRealtime()
        self.ep_image_edit = EPImageEdit()
        self.ep_video = EPVideo()
        self.image_editing = ImageEditing()
        self.ai_voice_and_audio = AIVoiceAndAudio()
        self.ai_chat_llm = AIChatLLM()
        self.ep_txt2img = EPTxt2Img()
        self.ep_voice_cloning = EPVoiceCloning()
        self.community_models = CommunityModels()
        self.train_model = TrainModel()
        self.text_to_3d = TextTo3D()
