import time
import pyautogui

#######################################################################################################
'''

def screenshot():
    time.sleep(5);                          #5Secs#whenever we call this function , it should wait for sometime and then take a click;
    img = pyautogui.screenshot('test.png');    #itll take ss and save it as test.png 
    img.show();                              #after clicking itll show the pic once
    
screenshot();                                      #to run the function

#but here problem is its again and again updating the test.png file , losing the data of previous pic (overwritten)

'''

####################################################################################################

'''
#updated code:

def screenshot():
    name = int(round(time.time() * 1000)) #converting random numbers into integers by rounding it and saving it as a variable 'name'
    name = 'C:/Users/ayxnk/Desktop/python/screenshots data/{}.png'.format(name)  #itll save the pic with the random number generated.png 
    #->itll save the pic in a particular folder, as the path given
    time.sleep(5); #5Secs#whenever we call this function , it should wait for sometime and then take a click;
    img = pyautogui.screenshot(name); #itll take ss and save it as test.png 
    img.show();  #after clicking itll show the pic once
    
screenshot(); #to run the function

'''

###################################################################################################

'''
->now it is creating seperate pics for every pics or clicks taken

->now if we want our pic/clicks to be saved in one folder then,
create folder, copy its path and paste that...
->name = '......................{}.png'.format(name)
path will be in "\" slashes, turn them into "/" ...

'''

##########################################################################################################

#->now we are going to Add GUI to this screenshot pgm/application

#->we will want to import a library, which is a built-in module in py

import tkinter as tk #we dont have to write the fullform everytime i.e tkinter, instead we can use tk

def screenshot():
    name = int(round(time.time() * 1000)) #converting random numbers into integers by rounding it and saving it as a variable 'name'
    name = 'C:/Users/ayxnk/Desktop/python/screenshots data/{}.png'.format(name)  #itll save the pic with the random number generated.png 
    #->itll save the pic in a particular folder, as the path given
    '''
    time.sleep(5); #5Secs#whenever we call this function , it should wait for sometime and then take a click;
    -> as we have button , we do not need timer, but its all your wish to keep it or not.
    '''
    img = pyautogui.screenshot(name); #itll take ss and save it as test.png 
    img.show();  #after clicking itll show the pic once
    
    '''
screenshot(); #to run the function
#we have removed function call from here
    '''

root = tk.Tk()      
#root is your main application window/This creates the main window (or root window) of your application.

root.title("Screenshot Application")
#adds a title to the window for better user experience

frame = tk.Frame()    
#This creates a Frame widget, which is a container within the root window.
#A Frame is used to group and organize other widgets (like buttons, labels, etc.) inside it. 
# It's especially useful for laying out the interface more effectively.


frame.pack()         
#The pack() method is a geometry manager in tkinter that organizes widgets in blocks before placing them in the parent widget (in this case, root by default).
#When you call frame.pack(), the frame is placed inside the window and arranged in a certain order (default is top to bottom).
#You can also customize its placement with additional parameters, such as side, padx, and pady.


button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot
)
#The first button is created inside the frame, labeled "Take Screenshot". 
#The command=screenshot tells tkinter to execute the screenshot function when this button is clicked.

button.pack(side=tk.LEFT)      
##The button is placed on the left side of the frame using pack(side=tk.LEFT).
#this will place my button at the left of the screen


close = tk.Button(
    frame,
    text="QUIT",
    command=quit
)
#The second button, labeled "QUIT", will close the application when clicked, as command=quit is assigned to it.

close.pack(side=tk.LEFT)
#This button is also positioned on the left side of the frame, right next to the "Take Screenshot" button.



root.mainloop()
#This starts the tkinter main event loop, which keeps the window active and responsive until it's closed or the quit button is pressed.

