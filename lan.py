import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Function to perform translation
def translate_text():
    translator = Translator()
    src_language = src_lang_combobox.get()
    dest_language = dest_lang_combobox.get()
    text_to_translate = src_text.get("1.0", "end-1c")  # Get text from source text box
    
    # Perform translation
    translated = translator.translate(text_to_translate, src=src_language, dest=dest_language)
    result_text.delete(1.0, "end")  # Clear previous result
    result_text.insert("1.0", translated.text)  # Insert translated text

# Create the main window
root = tk.Tk()
root.title("Language Translator")

# Set the window size
root.geometry("500x500")

# Source Language label and combobox
src_lang_label = tk.Label(root, text="Source Language")
src_lang_label.pack(pady=10)

# Create combobox for source language
src_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()))
src_lang_combobox.set("english")  # Default value
src_lang_combobox.pack(pady=10)

# Textbox to input text to translate
src_text_label = tk.Label(root, text="Enter Text:")
src_text_label.pack(pady=10)

src_text = tk.Text(root, height=5, width=40)
src_text.pack(pady=10)

# Destination Language label and combobox
dest_lang_label = tk.Label(root, text="Destination Language")
dest_lang_label.pack(pady=10)

# Create combobox for destination language
dest_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()))
dest_lang_combobox.set("spanish")  # Default value
dest_lang_combobox.pack(pady=10)

# Button to trigger translation
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=20)

# Result textbox to show translated text
result_label = tk.Label(root, text="Translated Text:")
result_label.pack(pady=10)

result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=10)

# Run the GUI
root.mainloop()
