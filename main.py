import audiostack
import os
from chatgpt import final
#imports the summary script from the chatgpt.py file

#Code below is edited from the audiostack API quickstart guide
"""
Hello! Welcome to the audiostack python SDK. 
"""

#gets the api key from secrets
audiostack.api_key = os.environ['APIKEY']


#adds the tts script
scriptText = final

script = audiostack.Content.Script.create(
  scriptText=scriptText,
  projectName="testingthings"
)

tts = audiostack.Speech.TTS.create(
  scriptItem=script,
  voice="bronson",
  speed= 1.0)
#Sets the voice for the TTS

mix = audiostack.Production.Mix.create(
  speechItem=tts,
  soundTemplate="time_horizon_20",
  masteringPreset="balanced"
)
print(mix)

encoder = audiostack.Delivery.Encoder.encode_mix(productionItem=mix, preset="mp3")
encoder.download(fileName="Summary")