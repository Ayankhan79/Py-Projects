import webbrowser as wb

#The `webbrowser` library in Python is used to open URLs in a web browser directly from Python scripts.
# It allows you to automate web-based tasks, such as
# opening websites, 
# and works with the default browser or specified browsers
# like Chrome or Firefox. 
# It's cross-platform and simple to use for tasks like launching web applications 
# or automating repetitive browsing tasks.

def webauto():

    #you can add path to it , in which browser you want it to open...
    '''
    -->Chrome_path='XXXXXXXXX %s'
    '''
    #XXXXXXXXX-->copy the path of your browser from the file manager.


    #If you Want to Open Your Code/Text editor...
    #do as followed:
    '''
    #-> Code_path='C:XXX\\xxx\\ccc\\ddd.exe'
    '''
    #->#specifying the Code path from the file manager and copy it (i.e .exe form)
    
    '''
    #-> os.startfile(Code_path)
    '''
    #->This line will Start/Open the Particular editor You've Mentioned in the path.


    # List of URLs to be opened
   URLS = (
        "https://web.whatsapp.com/",
        "https://www.youtube.com/",
        "https://www.udemy.com/",
        "https://chatgpt.com/"
   )
   
  #URL List: The URLs are stored in a tuple URLS, 
  #and each one is opened using the wb.open() function.
   
   for url in URLS:
    #Loop: The for loop goes through each URL in the list and prints a message before opening it in the default browser.
    # Loop through each URL in the list 
    # and open it in the default browser
       
       print("Opening: " + url)
       # Print the URL being opened for clarity
       
       wb.open(url)
       # Opens the URL in the default web browser
       #wb.open(url): This function opens the specified URL in the user's default web browser


        
        #If you're using the Chrome_path method Then, in the for loop:
        '''
        -> wb.get(Chrome_path).open(url)
        '''

webauto()

##This is For Default Browser##
