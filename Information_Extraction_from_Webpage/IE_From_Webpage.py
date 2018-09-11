
#regular expression package to match patterns
import re;
from Tkinter import *
import tkSimpleDialog
import tkMessageBox
"""
 This printList function is find pattern from input file data and write into output file.
 argument list:
     1. pattern -> which patter looking for into text file 'Pattern'
     2. fileData -> input file text data 'String'
     3. fileOutput -> file object for writing output 'File'
     4. nameofList -> pattern is related to which context 'String'
"""
def printList(pattern,fileData,fileOutput,nameofList):
    list= pattern.findall(fileData);

    if(len(list)>0):
        # print on console
        print "List of "+nameofList+":";
        output="-----%s-----" %(nameofList)
        output+="\n %s. " %(list)
        
        tkMessageBox.showinfo("Results",output)
        # write in output file
        fileOutput.write("List of "+nameofList+":\n");
        for x in range(0,len(list)):
            print "   %d. %s"%(x+1,list[x]);
            
            fileOutput.write("   %d. %s\n"%(x+1,list[x]));
    else:
            print "No "+nameofList+" found";
            output="-----No %s-----" %(nameofList)
            tkMessageBox.showinfo("Results",output)
            fileOutput.write("No "+nameofList+" found");
   
    fileOutput.write("\n");
    
# Program execution begins from Here

import urllib
from bs4 import BeautifulSoup

root=Tk()
w=Label(root, text="My Program")
w.pack()
 
tkMessageBox.showinfo("Welcome","Information Extraction From Webpage....!!!!!")

url=tkSimpleDialog.askstring("Url","Enter url..!!!!")


#url = "https://www.nitt.edu/home/academics/contact_details/"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())

# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

#file= open("/home/triloki/Documents/OutputText1.txt","w")
#file.write(text)
#print(text.encode('utf-8'))
# read file first, read mode only
#fileInput = open("/home/triloki/Documents/InputText.txt","r");

fileData = text

# open output file, write mode
# this will erase old output file if available
fileOutput = open("/home/triloki/Desktop/Final NLC Project/OutputText.txt","w");


# 10 digit phone number regex
# recognizes example
# 1. 9898772506
# we can also define other regular expression
#phonePattern = re.compile("(\d{3} \d{4} \d{4})");
phonePattern = re.compile("\d{10}");

# Search for phone number in file and print it
printList( phonePattern, fileData, fileOutput, "Phone Number");



# web url regex
# recognizes examples
# 1. webaddress.com 
# 2. https://www.google.com
# 3. http://www.web-url.com?id=10
# 4. https://www.codecademy.com/learn/all
urlPattern = re.compile("[a-zA-Z0-9+:/%?=-]{2,}\.[a-zA-Z0-9./%?=-]+");

# Search for urls in file
printList( urlPattern, fileData, fileOutput, "Web Links");

# email address regex
# recognizes examples
# 1. something@gmail.com
# 2. something@google.co.in
emailPattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z][.a-zA-z]*\.[a-zA-Z]{2,}");


# Search for Email in file
printList( emailPattern, fileData, fileOutput, "Email Address");


# date regex
# recognises examples 
# 1. 11/12/2017
# 2. 11-12-2017
# 3. 11-12-'17
datePattern = re.compile("\d{1,2}[-|/]\d{1,2}[-|/][']?\d{2,4}");

# Search for date in file
printList( datePattern, fileData, fileOutput, "Date");

# fileInput.close();
fileOutput.close();
