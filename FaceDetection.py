import cv2
# Import the OpenCV library

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Load the pre-trained Haar Cascade classifier for face detection


def detect():
    
    cap = cv2.VideoCapture(0)
    # Initialize the webcam feed (0 typically refers to the default webcam)
    
    while True:
    # Infinite loop to continuously capture frames from the webcam
    
        # Read a frame from the webcam
        _,img = cap.read()
        # The first value is a boolean indicating if the frame was read correctly
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Convert the image to grayscale (face detection usually works better in grayscale)
        
        face = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Detect faces in the grayscale image
        # 'detectMultiScale' detects objects at different scales (sizes)
        # Parameters:
        # - gray: the image to process (in grayscale)
        # - 1.1: scale factor (image is reduced by 10% at each scale)
        # - 4: minimum number of neighbors each rectangle should have to retain it
        
        # Loop over all detected faces
        for (x, y, w, h) in face:
            
            cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0), 2)
            # Draw a rectangle around each face in the original image
             # Parameters:
            # - img: the original image
            # - (x, y): top-left corner of the rectangle
            # - (x + w, y + h): bottom-right corner of the rectangle
            # - (0, 255, 0): color of the rectangle (green in BGR format)
            # - 2: thickness of the rectangle's borders
            
            
        cv2.imshow("Face Detect", img)
        # Display the image with detected faces in a window titled "Face Detect"
        
        # Check if the 'Esc' key (ASCII code 27) is pressed
        if cv2.waitKey(1)==27:
           # Break the loop to stop face detection and close the window
            break
        
    cap.release()
    # Release the webcam feed once we exit the loop
    
detect()
# Call the face detection function
