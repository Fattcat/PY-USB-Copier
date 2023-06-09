# NECESSARYYYY MODULESS FOR USEEE :DD
import os
import shutil
import time

# Destination folder on the Desktop
output_folder = os.path.expanduser("~/Desktop/USBs-Output")

# PYTHON - USB COPIER Version : 1.0.0
# DATE 9.6.2023 SLOVAKIA

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Infinite loop to continuously scan for USB devices every 3 seconds
while True:
    # Get a list of all possible drive letters
    drive_letters = [chr(letter) + ":" for letter in range(65, 91)]

    # Iterate over each drive letter
    for drive_letter in drive_letters:
        usb_path = os.path.join(drive_letter)

        # Check if the drive is ready (exists)
        if os.path.exists(usb_path):
            usb_folder = os.path.join(output_folder, os.path.basename(usb_path))

            # Create a subfolder for the USB device
            os.makedirs(usb_folder, exist_ok=True)

            # Copy all files from the USB device to the subfolder
            for root, dirs, files in os.walk(usb_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    shutil.copy2(file_path, usb_folder)

            print(f"Files from USB {usb_path} have been copied to the 'USBs-Output' folder on the Desktop.")

    time.sleep(3)  # Wait for 3 seconds before scanning again
