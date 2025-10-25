import os
import shutil

# Define the source and destination folders
source_folder = "/path/to/source/folder"
destination_folder = "/path/to/destination/folder"

def move_jpg_files():
    # Check if the source and destination folders exist
    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        return
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print("Destination folder created.")

    # Get a list of all .jpg files in the source folder
    jpg_files = [file for file in os.listdir(source_folder) if file.endswith(".jpg")]

    # Move each .jpg file to the destination folder
    for file in jpg_files:
        source_file = os.path.join(source_folder, file)
        destination_file = os.path.join(destination_folder, file)
        shutil.move(source_file, destination_file)
        print(f"Moved {file} to {destination_folder}")

    print("All .jpg files have been moved.")

if __name__ == "__main__":
    move_jpg_files()
