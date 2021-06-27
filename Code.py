import tkinter as tk
import pytesseract as tess
import PIL
import cv2
tess.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'

""" Dialog Box"""
from tkinter import filedialog
root=tk.Tk()
root.withdraw()
file_path=filedialog.askopenfilename()
print("Image selected from"+file_path)  # file path for image`
image_file=PIL.Image.open(file_path)
#image_file.show()

""" converting any image to jpg format """
convert_image=image_file.convert('RGB')
convert_image.save('converted.jpg') # converted image stores with this file name

converted_image_path='C:/Users/Wolverine/Desktop/sorting visualizer/OCR/converted.jpg'

""" OCR Engine"""
ocr_text=tess.image_to_string(converted_image_path)
print(ocr_text)

""" Preprocessing for Tesseract"""

preprocessing_image =PIL.Image.open(converted_image_path) #converted image is set for preprocessing image
def greyscale(preprocessing_image):
    print("Greyscale:\n",tess.image_to_string(preprocessing_image.convert('L')))
def removenoise(preprocessing_image):
    print("Remove noise:\n", tess.image_to_string(preprocessing_image.convert('1')))
greyscale(preprocessing_image)
removenoise(preprocessing_image)
