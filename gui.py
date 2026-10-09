import tkinter as tk
from pdf_batch import batch_replace_pdf_text

#allows user to specify file paths for input and output, and allows users to customize target and replacement text.

def on_button_press():
    source_file = entry1.get()
    dest_file = entry2.get()
    original_text = entry3.get()
    replacement_text = entry4.get()
    font_size = entry5.get()
    text_mapping = {original_text : replacement_text}
    
    batch_replace_pdf_text(source_file, dest_file, text_mapping, font_size)
    print(f"button pressed entries are: {source_file} and {dest_file}")
    print(f"original and replacement text are {text_mapping}")

#need to modify so it's easier for users to select files and select font size and type
root = tk.Tk()

tk.Label(root, text="Source File").grid(row=0, column=0)
tk.Label(root, text="Destination File").grid(row=1, column=0)
tk.Label(root, text="Original Text").grid(row=2, column=0)
tk.Label(root, text="Replacement Text").grid(row=3, column=0)
tk.Label(root, text="Font Size").grid(row=4, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)
entry5 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)
entry5.grid(row=4, column=1)

#calls our method on_button_press and places entry data into the params of batch_replace_pdf_text
submit_button = tk.Button(root, text="Submit", command=on_button_press).grid(row=5, column=0)


root.mainloop()