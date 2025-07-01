import Audio.VoiceGenerator as VoiceGenerator
import Web.WebScraper as WebScraper

audio = VoiceGenerator.VoiceGenerator()
web = WebScraper.WebScraper('https://www.bbc.com/news/articles/cp9005z1pljo')
web_content = web.fetch_content().split('.')

for content in web_content:
    audio.generate_audio(content)