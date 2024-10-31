########################################################################################

#Type1:

########################################################################################
'''

#text to speech only during running program

#pip install pyttsx3
#itll help us convert text to speech using python,windows system
#pyttsx3: A Python text-to-speech conversion library

#pip install pywin32
#it is dependency for pyttsx3 module
#pywin32: A required dependency for pyttsx3 on Windows.

import pyttsx3

# Get user input for text to be converted to speech
data = input('Enter the text that to you want to convert to speech: \n')

# Initialize the TTS engine (TTS-Text To Speech)
engine = pyttsx3.init()

# Pass the text to the speech engine
engine.say(data)

# Run the speech conversion and play the audio
engine.runAndWait()

'''
######################################################################################

#Type2:

######################################################################################
'''

#text to speech and save as .mp3 or .wav
#here it will save the file in the sam e directory , where our script is running

#pip install pydub
#pip install ffmpeg
#pydub: Provides a simple Python interface for manipulating audio files.
#ffmpeg: Does the heavy lifting of encoding and decoding audio ,
# that pydub cannot natively handle (e.g., .mp3 conversion).

import pyttsx3

# Get user input for the text to be converted to speech
data = input('Enter the text that you want to convert to speech: \n')

# Initialize the TTS engine
engine = pyttsx3.init()

# Pass the text to the speech engine
# Save the speech as an audio file (wav format)
engine.save_to_file(data, 'output_audio.wav')

# Run the speech conversion and save the file
engine.runAndWait()

print("Speech has been saved as 'output_audio.wav'")

'''
#######################################################################################

#Type3:

#######################################################################################



#from pydub import AudioSegment

# Convert wav to mp3 and save in a specific directory
#sound = AudioSegment.from_wav("output_audio.wav")

# Specify the full path for saving the file
#sound.export(r"C:\Users\YourUsername\Desktop\output_audio.mp3", format="mp3")

#print("Speech has been saved as 'output_audio.mp3' on your Desktop")


########################################################################################

#Text to speech , selecting the voice by indexing:

import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# List available voices
voices = engine.getProperty('voices')

# Print available voices
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} - {voice.languages}")

# Set the desired voice (change the index as needed)
engine.setProperty('voice', voices[0].id)  # Change index for desired voice

# Get user input for the text to be converted to speech
data = input('Enter the text that you want to convert to speech: \n')

# Pass the text to the speech engine
engine.say(data)

# Run the speech conversion
engine.runAndWait()


############################################################################################
