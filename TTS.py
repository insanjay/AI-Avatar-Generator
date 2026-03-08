import os
from input_services.text_input import script
from gtts import gTTS
import pyttsx3

# pyttsx3 for speaking(optional)
engine = pyttsx3.init()

prompt = script

engine.say(prompt)
engine.runAndWait()

# gTTS for saving the file

audio_path = "saved_audio" # change if need different path
tts = gTTS(prompt)
output_path = os.path.join(audio_path, 'prompt.mp3')
tts.save(output_path)
print(f"Audio file saved to: {output_path}")