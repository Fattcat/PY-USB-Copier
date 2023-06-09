import os
import shutil

# Destination folder on the Desktop
output_folder = os.path.expanduser("E:\USBs-Output")

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get a list of connected USB devices
usb_devices = [drive for drive in os.listdir("/media") if os.path.isdir(os.path.join("/media", drive))]

# Iterate over each USB device
for usb_device in usb_devices:
    usb_folder = os.path.join(output_folder, usb_device)

    # Create a subfolder for the USB device
    os.makedirs(usb_folder, exist_ok=True)

    # Copy all files from the USB device to the subfolder
    usb_path = os.path.join("/media", usb_device)
    for root, dirs, files in os.walk(usb_path):
        for file in files:
            file_path = os.path.join(root, file)
            shutil.copy2(file_path, usb_folder)

print("All files from connected USB devices have been copied to the 'USBs-Output' folder on the Desktop.")
