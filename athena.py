import Audio.VoiceGenerator as VoiceGenerator
import Web.WebScraper as WebScraper
import Audio.AudioEditor as AudioEditor
import os

audio = VoiceGenerator.VoiceGenerator()
audio_editor = AudioEditor.AudioEditor()
web = WebScraper.WebScraper('https://www.bbc.com/news/articles/cg4r5wylwq6o')
web_content = web.fetch_content().split('.')
filenames = []

for content in web_content:
    filenames.append(audio.generate_audio(content))

audio_editor.join_audio_files(filenames)

for file in filenames:
    os.remove(file)