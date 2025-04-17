# File Read & Write
def modify_file(input_filename, output_filename):
    try:
        # opening the input file in read mode 
        with open(input_filename, 'r') as file:
            content = file.read()
        
        #  modifing the content. #turning everything to uppercase
        modified_content = content.upper()
        
        # Writing the modified content to the output file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"All done! File has been modified and saved to {output_filename}.")
    
    except FileNotFoundError:
        print(f"Oops! The file {input_filename} doesn't exist. Check the file name and try again.")
    except Exception as e:
        print(f"Something went wrong: {e}")


# Error Handling Lab
def get_filename_and_process():
    # Asking the user for a filename to read
    filename = input("Enter the filename you want to open: ")
    
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("Here's the content of the file:\n")
            print(content)
    
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist. Double-check the filename and try again.")
    except IOError:
        print(f"Couldn't read the file {filename}. Make sure it's not locked or damaged.")
    except Exception as e:
        print(f"Something unexpected happened: {e}")

# Example
input_file = 'names.txt'
output_file = 'modified_example.txt'
modify_file(input_file, output_file)
get_filename_and_process()
