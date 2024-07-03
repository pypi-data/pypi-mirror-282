import os
import json
from eternalblue.diarization import Diarization
from eternalblue.transcription import Transcription
from eternalblue.utils import OUTPUT_PATH


def create_directories():
    base_dir = os.path.join(os.path.dirname(__file__), 'public')
    sub_dirs = ['audios', 'outputs', 'transcriptions']

    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    for sub_dir in sub_dirs:
        dir_path = os.path.join(base_dir, sub_dir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


class EternalBlue:
    def __init__(self, hg_token: str, language: str, model: str = "openai/whisper-large-v3"):
        self.hg_token = hg_token
        self.language = language
        self.model = model
        create_directories()

    def diarize(self, audio_path: str, num_speakers=2):
        diarizer = Diarization(self.hg_token)
        audio_name = diarizer.diarize(audio_path, num_speakers)
        if audio_name is not None:
            transcriptor = Transcription(self.model)
            output_json = transcriptor.generate_transcription(audio_path, audio_name, self.language)
            with open(output_json, 'r', encoding='utf-8') as arquivo:
                pure_json = json.load(arquivo)
            os.remove(output_json)
            os.remove(OUTPUT_PATH + f"/{audio_name}")
            return pure_json
