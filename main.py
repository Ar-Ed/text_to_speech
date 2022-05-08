import os
import tkinter as tk

from gtts import gTTS
from playsound import playsound

FILE_NAME = "recording.mp3"

def text_to_speech(entry):
   tts = gTTS(entry.get())
   tts.save(FILE_NAME)

   playsound(FILE_NAME)
   os.remove(FILE_NAME)


window = tk.Tk()
window.title("text to speech")
window.geometry("600x400")

entry = tk.Entry()
button = tk.Button(text="Enter", command=lambda: text_to_speech(entry))

entry.pack()
button.pack()

window.mainloop()


