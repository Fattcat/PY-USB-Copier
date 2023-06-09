# NECESSARYYYY MODULESS FOR USEEE :DD
import os
import shutil
from time import sleep

# PYTHON - USB COPIER Version : 1.0.0
# DATE 9.6.2023 SLOVAKIA

while True:
    # Destination folder on the Desktop PLEASE CHANGE it !
    output_folder = os.path.expanduser("~/Desktop/USBs-Output")

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of connected USB devices
    usb_devices = [drive for drive in os.listdir("E:\\") if os.path.isdir(os.path.join("E:\\", drive))]

    # Iterate over each USB device
    for usb_device in usb_devices:
        usb_folder = os.path.join(output_folder, usb_device)

        # Create a subfolder for the USB device
        os.makedirs(usb_folder, exist_ok=True)

        # Copy all files from the USB device to the subfolder
        usb_path = os.path.join("E:\\", usb_device)
        for root, dirs, files in os.walk(usb_path):
            for file in files:
                file_path = os.path.join(root, file)
                shutil.copy2(file_path, usb_folder)

    print("All files from connected USB devices have been copied to the 'USBs-Output' folder on the Desktop.")
    sleep(3)
