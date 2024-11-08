#Speech To Text(Using Google API)

#pip install SpeechRecognition
# This installs the SpeechRecognition library for converting speech to text

#pip install pyaudio
# This installs the PyAudio library for working with audio input and output in Python (used for microphone access)

import pyttsx3
## Text-to-speech library 
# (imported but not used in this code)

import speech_recognition as sr
## Speech recognition library to recognize voice input

## Function to capture and recognize speech
def get():
    
    r = sr.Recognizer()
    ## Create an instance of the Recognizer class to recognize speech
    
    with sr.Microphone() as source:
    ## Use the microphone as the source for input
    
        print("Say Something....")
        ## Prompt(Commands) the user to speak
        
        audio = r.listen(source)
        ## Listens to the audio from the microphone and stores it in the variable 'audio'
        
        print('Done.')
        ## Indicate that the recording is complete

        
    try:
        text = r.recognize_google(audio)
        ## Recognize the speech using Google's speech recognition API
        
        print('you said :'+ text)
        # Print the recognized text
        
    except Exception as e:
        print(e)
        # If an error occurs during recognition,
        # print the error message

# Calling the function to initiate speech recognition        
get()

        
