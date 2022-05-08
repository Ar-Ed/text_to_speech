import os

from gtts import gTTS
from playsound import playsound

FILE_NAME = "recording.mp3"

def handle_entry(input, is_save, is_speak, is_file):
   if is_file:
      _file_to_speech(input)
   else: 
      _text_to_speech(input)

   if is_speak:
      playsound(FILE_NAME)    # play mp3

   if not is_save:
      os.remove(FILE_NAME)    # delete mp3
   

def _file_to_speech(file_name):
   with open(file_name, "r") as file:
      tts = gTTS(file.read()) # text -> speech
      tts.save(FILE_NAME)     # save speech to mp3

def _text_to_speech(text):
   tts = gTTS(text)           # text -> speech
   tts.save(FILE_NAME)        # save speech to mp3
