def read_and_write_file():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read from: ")
        
        # Open the file for reading
        with open(filename, 'r') as data:
            content = data.readlines()
        
        # Modify the content (e.g., adding line numbers)
        modified_content = [
            f"Line {index + 1}: {line}" for index, line in enumerate(content)
        ]
        
        # Create a new file to write the modified content
        output_filename = f"modified_{filename}"
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()
