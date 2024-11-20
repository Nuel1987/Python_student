import os
file = open('data.txt', 'r')

print(file.read())

#writeDoc = open('data.txt', 'w')

#writeDoc.write('Hello, this is a new content.') # write overwrites existing data

#appendDoc = open('data.txt', 'a') # append add new content

#appendDoc.write(' \n And this is an appended content.') # \n is used to append or add the text to the new line

#newDoc = open('newDoc.txt', 'w')

#newDoc.write("this is Kobby nuel learning to how to handle files that")

#createDoc = open('kobby.txt', 'w')

#createDoc.write('This is a new file.')

#os.remove('kobby.txt') # use to remove the file

try:
    file = open('data.txt', 'r') # open the file in read mode
    print(file.read())
except FileNotFoundError: # file exists
    print("File Not Found")
finally:
    print("This is Awesome")