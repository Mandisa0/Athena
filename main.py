#uvicorn main:app --reload
#uvicorn main:app --host 0.0.0.0 --port 5000 --reload
from fastapi import FastAPI
import Audio.VoiceGenerator as VoiceGenerator
import Web.WebScraper as WebScraper
import Audio.AudioEditor as AudioEditor
import os

app = FastAPI()
script_root = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
print(script_root)
#https://www.nasa.gov/blogs/spacestation/2025/07/03/progress-cargo-craft-launches-to-station-for-saturday-delivery/

@app.get("/generate")
def generate(url: str):
    
    try:
        audio = VoiceGenerator.VoiceGenerator()
        audio_editor = AudioEditor.AudioEditor()
        web = WebScraper.WebScraper(f"{url}", parent_attr='data-content-type', parent_attr_value='blog-entry')
        web_content = web.fetch_content().split('.')
        filenames = []

        for content in web_content:
            filenames.append(audio.generate_audio(content))

        generate_file_path = audio_editor.join_audio_files(filenames)

        for file in filenames:
            os.remove(file)
        
        return {"output": f"{script_root}/{generate_file_path}"}
    
    except Exception as e:
        return {"error": str(e)}