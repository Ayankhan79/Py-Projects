# Install BeautifulSoup4(bs4) using the pip command (if not already installed)
#pip install bs4
#this package is for extracting the Data From Html Pages


# Import the necessary libraries
import requests
#requests: This library is used to make HTTP requests to websites or APIs.
# It helps in fetching the HTML content of a web page.

from bs4 import BeautifulSoup
#BeautifulSoup: A Python library used for parsing HTML and XML documents.
# It helps in navigating and searching the structure of these documents


#Creating a Variablee Named - Search
# in which we'll be passing the query that is to be searched on google
search ='Weather in Kundapura'

#we are making another variable , in which we'll be passing
# link of the google search page and 
# pass the search variable in the f string...
#what itll do is redirect to the google search page and search for 'weather in Kundapura'
url = f"https://www.google.com/search?&q={search}"

# another variable 'r' in which we are requesting google
# to send the request
r = requests.get(url)


# we are creating a variable named 's' , in which 
# s is being assigned the result of parsing an HTML document 
# (stored in r.text) using the BeautifulSoup library
#This line creates a BeautifulSoup object s that allows you to interact with the HTML content 
# (i.e., extract data, search elements, or navigate the HTML structure).
#---->
#Basically,  Parsing the HTML content using BeautifulSoup
s = BeautifulSoup(r.text, "html.parser")


# Print the extracted text, which should contain the relevant weather information
# Extract the weather information from the relevant <div> tag
update = s.find("div", class_="BNeawe").text
#Using the s.find() method, the script locates the first <div> tag with the class BNeawe,
# which typically contains weather information in Google's search results. 
# The .text attribute is used to extract the text from the HTML element.
#and it is stored in variable "update"

# Print the extracted weather information
print("Weather Update: ",update)

