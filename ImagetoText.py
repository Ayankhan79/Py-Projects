#Requirements:

#1. google tesseract at UB Mannheim 
#and download the file wrt your PC's config.
#install it 

#2. pip install tesseract

#3. pip install pytesseract

################################################################################

import pytesseract 
#pytesseract is used to interact with the Tesseract OCR engine.

import os
#Useful for handling File Paths

from PIL import Image
#Used for Loading a Image


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# The tesseract_cmd is set to the location where the Tesseract OCR exe(executable) is installed on your machine.
# This line ensures the script knows where to find the Tesseract engine.

def convert():
#The convert function 
# opens an image file, 
# processes it using pytesseract to extract text, 
# and prints the text to the console.

    try:
        
        img = Image.open('img.jpg')
    # Open the image file (replace 'img.jpg' with the actual image file path)
    #and stores it in a variable named 'img'
    
        text = pytesseract.image_to_string(img)
    #we use pytesseract to extract text from given image,
    #then store it in variable 'text'
    
        print(text)
    #prints the variable 'text'

    except FileNotFoundError:
        #If any other error occurs, print the error message.
        print("Error: The Specified image file was not found.")

    except Exception as e:
        # If any other error occurs, print the error message.
        print(f"An error Occured: {e}")


convert()
#calling the Function to Execute the program from 
#image to text

#########################################################################################
