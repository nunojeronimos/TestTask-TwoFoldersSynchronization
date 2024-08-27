# Folder Synchronization and File Management Script

This Python script synchronizes two folders, allows for basic file operations such as creating, copying, and removing files, and logs all operations in a history file. The synchronization process runs continuously in the background, ensuring the destination folder is always an up-to-date copy of the source folder.

## Features

- **Automatic Folder Synchronization:** 
  - Monitors and syncs the `source_folder` with the `destination_folder` every 30 seconds.
  - Copies new or modified files from the source to the destination.
  - Removes files from the destination if they no longer exist in the source.

- **File Management Menu:** 
  - **Create File:** Creates a new `.txt` file in the source folder.
  - **Copy File:** Copies a file from the source folder to a specified destination, adding a `-copy` suffix to the filename.
  - **Remove File:** Deletes a file from the source folder.

- **Logging:** 
  - All operations (creation, copying, removal, and synchronization) are logged with a timestamp in `history_file.txt`.
  - Logs are displayed on the console after each operation.

## Getting Started

### Prerequisites

- Python 3.x
- `shutil`, `os`, `datetime`, `filecmp`, `threading`, and `queue` modules (these are part of the Python Standard Library).

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Run the script:
    ```bash
    python your_script_name.py
    ```

### Usage

1. **Menu Options:**
   - The script provides a menu with options to create, copy, and remove files.
   - The menu runs in a loop, allowing for continuous interaction until the user chooses to quit.

2. **Synchronization:**
   - The script continuously synchronizes the source folder (`./Folder1`) with the destination folder (`./Copy_Folder1`) every 30 seconds.
   - This runs in a background thread, independent of the menu operations.

3. **Logs:**
   - All operations are logged in `history_file.txt` located in the script's directory.
   - Logs include timestamps and details about the operation.

### Customization

- **Change Folders:** 
  - Modify the `source_folder` and `destination_folder` variables at the beginning of the script to sync different folders.
  
- **Sync Interval:** 
  - Adjust the `time.sleep(30)` in the `start_synchronization` function to change the synchronization interval.

### Example

- **Creating a file:**
  - From the menu, select `1) Create File`, enter the desired filename, and the file will be created in `./Folder1`.

- **Copying a file:**
  - Select `2) Copy File`, enter the file name to copy, and specify the destination folder. The file will be copied with a `-copy` suffix.

- **Removing a file:**
  - Select `3) Remove File`, enter the filename, and the file will be removed from `./Folder1`.

## Acknowledgements

This script uses Python's built-in libraries for file management, threading, and logging.

