import os
import threading

from gtts import gTTS
from playsound import playsound

FILE_NAME = "recording.mp3"

def handle_entry(input, is_save, is_speak, is_file):
   if is_file:
      _file_to_speech(input)
   else: 
      _text_to_speech(input)

   if is_speak:
      threading.Thread(target=lambda: _play_sound(FILE_NAME, is_save), daemon=True).start()
   
def _play_sound(file_name, is_save):
   playsound(file_name)       # play mp3
   if not is_save:
      os.remove(file_name)    # delete mp3


def _file_to_speech(file_name):
   with open(file_name, "r") as file:
      tts = gTTS(file.read()) # text -> speech
      tts.save(FILE_NAME)     # save speech to mp3

def _text_to_speech(text):
   tts = gTTS(text)           # text -> speech
   tts.save(FILE_NAME)        # save speech to mp3
