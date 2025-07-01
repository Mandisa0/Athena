import torchaudio
from chatterbox.tts import ChatterboxTTS
from datetime import datetime

class VoiceGenerator:

    def __init__(self):
        self.name = 1
        self.model = ChatterboxTTS.from_pretrained(device="cpu")

    def generate_audio(self, text):
        # print('Im loaded')
        # wav_data = self.model.generate(text)
        # torchaudio.save("Audio/Output/test-1.wav", wav_data, self.model.sr)

        # If you want to synthesize with a different voice, specify the audio prompt
        AUDIO_PROMPT_PATH="Apiesdoring Drive.wav"
        wav = self.model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
        current_datetime = datetime.now()
        filename = "Audio/Output/Audio_"+current_datetime.strftime("%Y_%m_%d_%H_%M_%S") + ".wav"
        print(filename)
        torchaudio.save(filename, wav, self.model.sr)