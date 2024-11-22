file = open('readWriteFile.txt', 'r') # reading the file readMe in the directory

print (file.read())

createNewDoc = open('newFile.txt', 'w')

createNewDoc.write('This is a new file.''\nI love creating codes with python.''\nit is a modified version of this file (readWriteFile.txt)')

try:
    # Open the existing file and read its content
    with open('readWriteFile.txt', 'r') as file:
        print("Content of 'readWriteFile.txt':")
        print(file.read())
    
    # Create a new file and write modified content
    with open('newFile.txt', 'w') as createNewDoc:
        createNewDoc.write(
            "This is a new file.\n"
            "I love creating codes with Python.\n"
            "It is a modified version of this file (readWriteFile.txt)."
        )
    print("New file 'newFile.txt' has been created successfully!")
    
    # Asking the user for another file to read
    user_file = input('Enter the required file name: ')
    
    with open(user_file, 'r') as user_open_file:
        print(f"Content of '{user_file}':")
        print(user_open_file.read())
    
except FileNotFoundError:
    print(f"Error: The file '{user_file}' was not found in the directory.")
except IOError:
    print("Error: There was an issue accessing the file.")
finally:
    print('Thank you for trusting us!')

