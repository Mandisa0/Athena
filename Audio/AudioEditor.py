from pydub import AudioSegment
from datetime import datetime

class AudioEditor:

    def __init__(self):
        self.name = 1
        
    def join_audio_files(self, audio_files):
        combined = AudioSegment.empty()
        for file in audio_files:
            audio_segment = AudioSegment.from_file(file)
            combined += audio_segment
            current_datetime = datetime.now()
        
        combined.export("Audio/Output/Combined_Audio"+current_datetime.strftime("%Y_%m_%d_%H_%M_%S")+".wav", format="wav")
        return combined