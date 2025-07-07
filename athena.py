import Audio.VoiceGenerator as VoiceGenerator
import Web.WebScraper as WebScraper
import Audio.AudioEditor as AudioEditor
import os

audio = VoiceGenerator.VoiceGenerator()
audio_editor = AudioEditor.AudioEditor()
web = WebScraper.WebScraper('https://www.nasa.gov/blogs/spacestation/2025/07/03/progress-cargo-craft-launches-to-station-for-saturday-delivery/', parent_attr='data-content-type', parent_attr_value='blog-entry')
web_content = web.fetch_content().split('.')
filenames = []

for content in web_content:
    filenames.append(audio.generate_audio(content))

audio_editor.join_audio_files(filenames)

for file in filenames:
    os.remove(file)