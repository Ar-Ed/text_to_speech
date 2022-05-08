import tkinter as tk

from utils import text_to_speech

# Create Window
window = tk.Tk()
window.title("text to speech")
window.geometry("600x400")

entry = tk.Entry()
# call text_to_speech on button press
button = tk.Button(text="Enter", command=lambda: text_to_speech(entry))

entry.pack()
button.pack()

window.mainloop()
