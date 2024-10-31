## First, install the pyshorteners library
#pip install pyshorteners
#This installs the pyshorteners package,
# which provides an easy-to-use interface for shortening URLs 
# using various shortening services (e.g., TinyURL, Bit.ly, etc.).

import pyshorteners
# Import the pyshorteners library for URL shortening.
#This imports the pyshorteners module so that you can use its functionality in your Python script.

url= input("Enter URL :  \n")
#This prompts the user to input a URL 
# and stores it as a string in the variable 'url'.

shortened_url = pyshorteners.Shortener().tinyurl.short(url)
#pyshorteners.Shortener() : creates an instance of the Shortener class.
#.tinyurl : accesses the TinyURL shortening service.
#.short(url) : shortens the URL provided by the user.

print("URL After Shortening :- ", shortened_url )
#This prints the shortened URL 
# returned from TinyURL 
# after it has been processed.

#Overall: The program will now shorten any URL provided by the user and display it.

