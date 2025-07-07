import torchaudio
from chatterbox.tts import ChatterboxTTS
from datetime import datetime

class VoiceGenerator:

    def __init__(self):
        self.name = 1
        self.model = ChatterboxTTS.from_pretrained(device="cpu")

    def generate_audio(self, text):
        AUDIO_PROMPT_PATH="Audio/Sample/mandisa_voice.wav"
        wav = self.model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
        current_datetime = datetime.now()
        filename = "Audio/Output/Audio_"+current_datetime.strftime("%Y_%m_%d_%H_%M_%S") + ".wav"
        torchaudio.save(filename, wav, self.model.sr)
        
        return filename