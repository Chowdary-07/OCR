# Required Libraries
from PIL import Image
import pytesseract as tess
import tkinter as tk
from tkinter import filedialog
root=tk.Tk()
root.withdraw()
file_path=filedialog.askopenfilename()
print(file_path)
im=Image.open(file_path)
text=tess.image_to_string(im)
print(text)
