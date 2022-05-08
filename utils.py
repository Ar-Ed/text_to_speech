import os

from gtts import gTTS
from playsound import playsound


FILE_NAME = "recording.mp3"

def text_to_speech(entry):
   tts = gTTS(entry.get()) # text -> speech
   tts.save(FILE_NAME)     # save speech to mp3

   playsound(FILE_NAME)    # play mp3
   os.remove(FILE_NAME)    # delete mp3
