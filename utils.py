import os
import threading
from datetime import datetime

from gtts import gTTS
from playsound import playsound


def handle_entry(input, is_save, is_speak, is_file, output_name):
   if not output_name:
      # if output file name is not given use current date
      output_name = datetime.now().strftime("%H_%M_%S_%d_%m_%Y")
   output_name = output_name + ".mp3"
   
   if is_file:
      _file_to_speech(input, output_name)
   else: 
      _text_to_speech(input, output_name)

   if is_speak:
      threading.Thread(target=lambda: _play_sound(output_name, is_save), daemon=True).start()
   
def _play_sound(file_name, is_save):
   playsound(file_name)             # play mp3
   if not is_save:
      os.remove(file_name)          # delete mp3


def _file_to_speech(file_name, output_name):
   with open(file_name, "r") as file:
      tts = gTTS(file.read())       # text -> speech
      tts.save(output_name)         # save speech to mp3

def _text_to_speech(text, output_name):
   tts = gTTS(text)                 # text -> speech
   tts.save(output_name)            # save speech to mp3
