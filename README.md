Folder Synchronization and File Management Tool
Overview
This Python script is designed to provide basic file management and synchronization between two folders. The script allows users to create, copy, and remove files in a source folder while maintaining synchronization with a destination folder. The operations and synchronization activities are logged for future reference.

Features
File Creation: Allows users to create text files in the source folder.
File Copying: Copies a specified file from the source folder to any user-specified destination.
File Removal: Removes a specified file from the source folder.
Folder Synchronization: Automatically synchronizes files between the source and destination folders every 30 seconds, ensuring that any changes are mirrored.
Logging: Logs all file operations and synchronization activities to a history_file.txt file.
Requirements
Python 3.x
shutil, os, datetime, filecmp, time, threading, queue modules (these are part of the Python standard library)
Setup
Source Folder: The source folder where files will be managed is set as ./Folder1.
Destination Folder: The destination folder where files will be synchronized is set as ./Copy_Folder1.
How to Use
Running the Script:

Execute the script in your Python environment. The synchronization process will start automatically, running in the background.
The menu will appear, providing the following options:
Menu Options:

Create File: Prompts for a file name and creates an empty text file in the source folder.
Copy File: Copies a specified file from the source folder to a user-defined destination folder.
Remove File: Deletes a specified file from the source folder.
Quit: Exits the program and stops the synchronization process.
Synchronization:

The script automatically synchronizes the contents of ./Folder1 with ./Copy_Folder1 every 30 seconds. Files that are new or modified in the source folder are copied to the destination folder, and files deleted in the source are also deleted in the destination.
Logs:

All operations and synchronization events are logged in the history_file.txt file. Logs include a timestamp and a description of the event.
