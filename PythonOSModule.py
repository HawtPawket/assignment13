# Task 1: Directory Inspector:

# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.

# Code Example:
#    import os

#    def list_directory_contents(path):
        # List and print all files and subdirectories in the given path
# Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories.



import os

def listDirectoryContents(path):
    files = []
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                files.append(entry.name)
    except FileNotFoundError:
        print(f"Error: '{path}' does not exist.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Contents of directory:")
        for file in files:
            print(file)

if __name__ == "__main__":
    directoryPath = input("Enter the directory path to view its contents: ")
listDirectoryContents(directoryPath)