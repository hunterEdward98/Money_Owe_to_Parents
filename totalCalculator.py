
# Python program for reading 
# from file 
  
import re
  
h = open('tabDetails.txt', 'r') 
  
# Reading from the file 
content = h.readlines() 

# Varaible for storing the sum 
a = 0
  
# Iterating through the content 
# Of the file 
for line in content: 
        # Checking for the digit in  
        # the string 
        a+= int(re.search(r'\d+', line).group())
              

myfile = "path/test.xml"
myfile = open("total.txt", "r+")
myfile.truncate(0)
myfile.close
myfile = open("total.txt", "a")
myfile.write(str(a))
myfile.close


