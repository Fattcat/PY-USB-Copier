# PYTHON - USB COPIER Version : 1.0.0
# DATE 9.6.2023 SLOVAKIA

import os
import shutil
import time
import psutil

# Destination folder on the Desktop
output_folder = os.path.expanduser("~/Desktop/USBs-Output")

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List of USB drive letters to scan
usb_drive_letters = ["E:", "H:", "Kingston:", "D:"]

# Infinite loop to continuously scan and copy USB devices every 3 seconds
while True:
    connected_drives = []

    for drive_letter in usb_drive_letters:
        # Check if the drive letter is currently available
        if os.path.exists(drive_letter):
            connected_drives.append(drive_letter)
    
    if connected_drives:
        for drive_letter in connected_drives:
            usb_path = os.path.join(drive_letter)
            usb_folder = os.path.join(output_folder, drive_letter)

            # Create a subfolder for the USB device
            os.makedirs(usb_folder, exist_ok=True)

            # Copy all files from the USB device to the subfolder
            for root, dirs, files in os.walk(usb_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    new_file_path = os.path.join(usb_folder, file)

                    # Generate a new file name if the file already exists
                    counter = 1
                    while os.path.exists(new_file_path):
                        file_name, file_ext = os.path.splitext(file)
                        new_file_name = f"{file_name}_{counter}{file_ext}"
                        new_file_path = os.path.join(usb_folder, new_file_name)
                        counter += 1

                    shutil.copy2(file_path, new_file_path)

            print(f"Files from USB {drive_letter} have been copied to the 'USBs-Output' folder on the Desktop.")

    time.sleep(3)  # Wait for 3 seconds before scanning again
