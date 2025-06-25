import torchaudio
from chatterbox.tts import ChatterboxTTS

class VoiceGenerator:

    def __init__(self):
        self.name = 1
        self.model = ChatterboxTTS.from_pretrained(device="cpu")

    def generate_audio(self, text):
        print('Im loaded')
        wav_data = self.model.generate(text)
        torchaudio.save("Audio/Output/test-1.wav", wav_data, self.model.sr)

        # If you want to synthesize with a different voice, specify the audio prompt
        #AUDIO_PROMPT_PATH="YOUR_FILE.wav"
        #wav = model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
        #ta.save("test-2.wav", wav, model.sr)