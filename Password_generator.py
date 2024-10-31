import string
import random

def gen():
    s1= string.ascii_uppercase
    #print(s1)        #prints all letters with upper case
    
    s2= string.ascii_lowercase
    #print(s2)        #prints all letters with lower case
    
    s3= string.digits
    #print(s3)        #prints all the numbers(0-9)
    
    s4= string.punctuation
    #print(s4)        #prints all special keys like (!@#$%^&*)
    
    passlen = int(input("Enter The Pasword length: \n"))
    #takes the input from the user- abt the length of the passkey , should be generated
    
    s = [] #defining variable 's' as a List
    
    s.extend(list(s1))    #store the value of s1 into s
    s.extend(list(s2))    #store the value of s2 into s
    s.extend(list(s3))    #store the value of s3 into s
    s.extend(list(s4))    #store the value of s4 into s
    #print(s)             #stores all the values of s1,s2,s3,s4 in s and prints
    
    random.shuffle(s)     #shuffles all the value of s in the list
    #print(s)             #shuffled values in list 's' are printed
    
    pas = ("".join(s[0:passlen]))
    #this randomly generates the sequence of passkey according to the len given
    
    print(pas)
    #this prints our pass key
    #everytime it generates differenet different passkeys even for the same length given again.
    
gen() 