# NECESSARYYYY MODULESS FOR USEEE :DD

# PYTHON - USB COPIER Version : 1.0.0
# DATE 9.6.2023 SLOVAKIA

import os
import shutil
import time

# Destination folder on the Desktop
output_folder = os.path.expanduser("~/Desktop/USBs-Output")

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List of USB drive letters to scan
usb_drive_letters = ["E:", "H:", "Kingston:", "D:"]

# Infinite loop to continuously scan and copy USB devices every 3 seconds
while True:
    for drive_letter in usb_drive_letters:
        usb_path = os.path.join(drive_letter)

        # Check if the USB drive is ready (exists)
        if os.path.exists(usb_path):
            usb_folder = os.path.join(output_folder, drive_letter)

            # Create a subfolder for the USB device
            os.makedirs(usb_folder, exist_ok=True)

            # Copy all files from the USB device to the subfolder
            for root, dirs, files in os.walk(usb_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    shutil.copy2(file_path, usb_folder)

            print(f"Files from USB {drive_letter} have been copied to the 'USBs-Output' folder on the Desktop.")

    time.sleep(3)  # Wait for 3 seconds before scanning again
