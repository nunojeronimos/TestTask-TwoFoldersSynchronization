import os
import datetime
import shutil
from filecmp import cmp
import time
import threading
from queue import Queue

source_folder = './Folder1'
destination_folder = './Copy_Folder1'

# Queue for storing log messages
log_queue = Queue()

def log_operations(message):
    log_file = 'history_file.txt'
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f'[{timestamp}] {message}'

    with open(log_file, 'a') as file:
        file.write(log_message + '\n')
    
    log_queue.put(log_message)  # Add log message to the queue

def display_logs():
    while not log_queue.empty():
        print(log_queue.get())

def sync_folders(source, destination):
    for root, dirs, files in os.walk(source):
        rel_path = os.path.relpath(root, source)
        dest_dir = os.path.join(destination, rel_path)

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)    

            if not os.path.exists(dest_file) or not cmp(src_file, dest_file, shallow=False):
                shutil.copy2(src_file, dest_file)
                log_operations(f'File synchronized: {src_file} to {dest_file}')

    for root, dirs, files in os.walk(destination):
        rel_path = os.path.relpath(root, destination)
        src_dir = os.path.join(source, rel_path)

        for file in files:
            src_file = os.path.join(src_dir, file)
            dest_file = os.path.join(root, file)

            if not os.path.exists(src_file):
                os.remove(dest_file)
                log_operations(f'File removed from destination: {dest_file}')

def menu():
    while True:
        print('')
        print ('******Menu******')
        print ('*1) Create File*')
        print ('*2) Copy File  *')
        print ('*3) Remove File*')
        print ('*4) Quit       *')
        print ('****************')

        choice = input("Enter Choice: ")
        name = ''
        folder_path = './Folder1'

        if (choice == '1'):
            file_name = input('File name: ')
            file_path = os.path.join(folder_path,  file_name + '.txt')
            with open(file_path, 'a') as file:
                log_operations(f'File created at {file_path}')
        
        elif (choice == '2'):
            file_name = input('Enter the file name you want to copy: ')
            destination = input('Enter the folder to where you want to copy the file: ')
            source_path = os.path.join(folder_path, file_name + '.txt')
            destination_path = os.path.join(destination, file_name + '-copy.txt')

            if os.path.exists(source_path):
                try:
                    shutil.copy(source_path, destination_path)
                    log_operations(f'File copied from {source_path} to {destination_path}')
                except Exception as e:
                    log_operations(f'Failed to copy file: {str(e)}')
            else:
                log_operations(f'Source file does not exist: {source_path}')

        elif (choice == '3'):
            file_name = input('File Name you Want to Remove: ')
            file_path = os.path.join(folder_path, file_name + '.txt')
            if os.path.exists(file_path):
                os.remove(file_path)
                log_operations(f'File removed: {file_path}')
            else:
                log_operations('File does not exist.')

        elif (choice == '4'):
            log_operations('Programme closed\n')
            break

        else:
            log_operations('Invalid Option. Please Try Again')

        display_logs()  # Display any pending logs after user interaction

# Start the synchronization process in the background
def start_synchronization():
    while True:
        sync_folders(source_folder, destination_folder)
        time.sleep(30)  # Wait for 30 seconds before next sync

# Run the synchronization and menu concurrently
sync_thread = threading.Thread(target=start_synchronization)
sync_thread.daemon = True  # Allow the thread to exit when the main program exits
sync_thread.start()

menu()  # Start the menu loop
