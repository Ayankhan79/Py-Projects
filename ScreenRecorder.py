import cv2
#This imports the OpenCV library, which is used for computer vision tasks like image and video processing.

import numpy as np
#This imports the NumPy library and gives it the alias np.
# NumPy is essential for numerical operations and working with arrays,
# which is important for image processing in OpenCV.

from PIL import ImageGrab
#This imports the ImageGrab module from the Python Imaging Library (PIL).
#ImageGrab allows you to capture screenshots of the entire screen or specific areas.

import time  
# Import time for adding delay

def screenRecorder():
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Define the codec and creates a VideoWriter object to save the video
    #A codec (short for coder-decoder) is a software or hardware component that encodes (compresses) and decodes (decompresses) digital data.
    # Codecs are essential in handling audio and video files, enabling efficient storage, transmission, and playback.
    #Parameters: The *'XVID' syntax is unpacking the string 'XVID' into individual characters,
    # which is required by the VideoWriter_fourcc() function.
    #XVID: This is a commonly used codec for video compression.
    # It is part of the MPEG-4 standard and is widely supported.
    # Videos encoded with XVID are typically of good quality while maintaining relatively small file sizes.
    
    fps = 20.0 
    # Specify the frames per second (fps) for the video
    
    out = cv2.VideoWriter("output.avi",fourcc,fps,(1920,1080))
    #out = cv2.VideoWriter("output.avi", fourcc, 20.0, (1280, 720)) 
    # -> not working for my system, Bcuz my system resolution is different  

    #This line creates a VideoWriter object in OpenCV, which is responsible for writing video files.
    ## Change resolution if needed
    
    #"output.avi": This is the name of the output video file. 
    # The .avi extension indicates that the file will be saved in AVI format,
    # which is a popular multimedia container format that can hold both video and audio data.
    # also can be changed to .mp4 or .mkv, depending on your requirements and the codec used.
    
    #fourcc: This is the codec used for compressing the video.
    # In your previous line, fourcc was defined using cv2.VideoWriter_fourcc(*'XVID'),
    # specifying that the XVID codec will be used for encoding the video frames.
    #different codec are used for different applications, and the choice of codec can affect the quality and size of the output file. 

    #(1920, 1080): This tuple specifies the resolution of the video frames to be written.
    # In this case, the resolution is set to 1920x1080 pixels, which corresponds to Full HD (1080p).
    
    while True:
    #This creates an infinite loop that will keep running,
    # until explicitly broken (e.g., when you press the 'Esc' key).
    
        img = ImageGrab.grab()
        #This line captures a screenshot of your entire screen 
        # and stores it in the variable img.
        
        img_np = np.array(img)
        #This converts the captured image (which is in a PIL format) into a NumPy array
        # and stores it in THE variable "img_np".
        #NumPy arrays are used in OpenCV for processing images.
        
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        # Convert the color from BGR to RGB 
        # This line converts the color format of the captured image, 
        # from BGR (Blue, Green, Red) to RGB (Red, Green, Blue).
    
        # (OpenCV uses BGR by default) -but many displays and image formats use RGB, 
        # so this conversion ensures the colors look correct.
       
        
        cv2.imshow("Screen Recorder", frame)
        # Displays the frame in a window titled "Screen Recorder"
        #This displays the current frame in a window titled "Screen Recorder."
        #It allows you to see the screen capture in real-time as it is being recorded.
        
        out.write(frame)
        #This writes the current frame to the video file you created earlier (using the VideoWriter).
        #Each frame is saved in the output video file, creating a continuous recording.
        
        
    ## Exit the loop if the 'Esc' key is pressed
        if cv2.waitKey(1)==27:
            #( 27 is the ASCII code for the 'Esc' key)
            break
            #If the condition is true (i.e., the Esc key is pressed),
            # the break statement exits the loop.
        
        time.sleep(0.05)  
        # Adjust this value if needed (50 ms delay)
        
    out.release()
    #out.release():
    #This line releases the resources associated with the VideoWriter object (out).
    #It finalizes the video file and ensures that all data is properly saved.
    #Without this, the video file may not save correctly or could be corrupted.

    cv2.destroyAllWindows()
    #This function closes all OpenCV windows that were opened during the program 
    # (like the "Screen Recorder" display window).
    
# Calling the screen recorder function to start recording 
screenRecorder()
        
        
###########################################################################################
        
        
#Additional Features to Consider

#Audio Recording:
# If you want to capture audio along with video,
# consider using libraries like pyaudio
# for audio input and combining it with your video output later.

#User Interface:
# You might add a simple GUI to start/stop recording 
# or select settings (resolution, FPS) without changing the code.
