import tkinter as tk

import utils

# Create Window
window = tk.Tk()
window.title("text to speech")
window.geometry("600x400")

# Checkbox and checkbox variables
is_save = tk.BooleanVar()
is_speak = tk.BooleanVar()
is_file = tk.BooleanVar()

cb_save = tk.Checkbutton(text="Save", variable=is_save)
cb_speak = tk.Checkbutton(text="Speak", variable=is_speak)
cb_file = tk.Checkbutton(text="File Input", variable=is_file)


# Entries and Button
input_label = tk.Label(text="Input")
input = tk.Entry()

output_label = tk.Label(text="Output File Name")
output_name_entry = tk.Entry()

button = tk.Button(text="Enter", 
command=lambda: utils.handle_entry(
   input.get(), is_save.get(), is_speak.get(), is_file.get(), output_name_entry.get()))


cb_file.pack()
cb_save.pack()
cb_speak.pack()
input_label.pack()
input.pack()
output_label.pack()
output_name_entry.pack()
button.pack()

window.mainloop()
