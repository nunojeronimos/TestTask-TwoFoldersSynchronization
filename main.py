import os
import datetime
import shutil
from filecmp import cmp
import time
import threading
from queue import Queue

# Define the source and destination folders for synchronization
source_folder = './Folder1'
destination_folder = './Copy_Folder1'

# Initialize a Queue to store log messages, which will be processed later
log_queue = Queue()

# Function to log operations with timestamps
def log_operations(message):
    log_file = 'history_file.txt'  # Name of the log file
    # Get the current timestamp in a specific format
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Format the log message with timestamp
    log_message = f'[{timestamp}] {message}'

    # Open the log file in append mode and write the log message
    with open(log_file, 'a') as file:
        file.write(log_message + '\n')
    
    # Add the log message to the queue for later display
    log_queue.put(log_message)

# Function to display logs from the queue
def display_logs():
    # Print each log message in the queue until it's empty
    while not log_queue.empty():
        print(log_queue.get())

# Function to synchronize files between the source and destination folders
def sync_folders(source, destination):
    # Walk through all directories and files in the source folder
    for root, dirs, files in os.walk(source):
        # Get the relative path of the current directory
        rel_path = os.path.relpath(root, source)
        # Determine the corresponding directory in the destination folder
        dest_dir = os.path.join(destination, rel_path)

        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Iterate over all files in the current directory
        for file in files:
            # Construct full file paths for the source and destination files
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)    

            # Check if the destination file doesn't exist or is different from the source file
            if not os.path.exists(dest_file) or not cmp(src_file, dest_file, shallow=False):
                # Copy the file to the destination folder
                shutil.copy2(src_file, dest_file)
                # Log the synchronization operation
                log_operations(f'File synchronized: {src_file} to {dest_file}')

    # Walk through all directories and files in the destination folder
    for root, dirs, files in os.walk(destination):
        # Get the relative path of the current directory
        rel_path = os.path.relpath(root, destination)
        # Determine the corresponding directory in the source folder
        src_dir = os.path.join(source, rel_path)

        # Iterate over all files in the current directory
        for file in files:
            # Construct full file paths for the source and destination files
            src_file = os.path.join(src_dir, file)
            dest_file = os.path.join(root, file)

            # If the source file doesn't exist, remove it from the destination
            if not os.path.exists(src_file):
                os.remove(dest_file)
                # Log the file removal operation
                log_operations(f'File removed from destination: {dest_file}')

# Function to display a menu and handle user operations
def menu():
    while True:
        # Display menu options to the user
        print('')
        print ('******Menu******')
        print ('*1) Create File*')
        print ('*2) Copy File  *')
        print ('*3) Remove File*')
        print ('*4) Quit       *')
        print ('****************')

        # Get user input for menu choice
        choice = input("Enter Choice: ")
        name = ''
        folder_path = './Folder1'  # Define the folder path for file operations

        if (choice == '1'):
            # Option 1: Create a new file
            file_name = input('File name: ')
            file_path = os.path.join(folder_path,  file_name + '.txt')
            # Create the file and log the creation
            with open(file_path, 'a') as file:
                log_operations(f'File created at {file_path}')
        
        elif (choice == '2'):
            # Option 2: Copy an existing file to a new location
            file_name = input('Enter the file name you want to copy: ')
            destination = input('Enter the folder to where you want to copy the file: ')
            source_path = os.path.join(folder_path, file_name + '.txt')
            destination_path = os.path.join(destination, file_name + '-copy.txt')

            # Check if the source file exists
            if os.path.exists(source_path):
                try:
                    # Copy the file to the destination and log the operation
                    shutil.copy(source_path, destination_path)
                    log_operations(f'File copied from {source_path} to {destination_path}')
                except Exception as e:
                    # Log any errors encountered during the copy operation
                    log_operations(f'Failed to copy file: {str(e)}')
            else:
                # Log if the source file does not exist
                log_operations(f'Source file does not exist: {source_path}')

        elif (choice == '3'):
            # Option 3: Remove an existing file
            file_name = input('File Name you Want to Remove: ')
            file_path = os.path.join(folder_path, file_name + '.txt')
            # Check if the file exists before attempting to remove it
            if os.path.exists(file_path):
                os.remove(file_path)
                # Log the file removal operation
                log_operations(f'File removed: {file_path}')
            else:
                # Log if the file does not exist
                log_operations('File does not exist.')

        elif (choice == '4'):
            # Option 4: Quit the program
            log_operations('Program closed\n')
            break

        else:
            # Log invalid menu option selections
            log_operations('Invalid Option. Please Try Again')

        # Display any pending logs after user interaction
        display_logs()

# Function to start the synchronization process in the background
def start_synchronization():
    while True:
        # Synchronize the source and destination folders
        sync_folders(source_folder, destination_folder)
        time.sleep(30)  # Wait for 30 seconds before the next sync

# Run the synchronization and menu concurrently
sync_thread = threading.Thread(target=start_synchronization)
sync_thread.daemon = True  # Allow the thread to exit when the main program exits
sync_thread.start()

menu()  # Start the menu loop
