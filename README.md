# Bulk Image Resizer and Optimizer

## Client: Urban Outfit Snaps

### Request
Urban Outfit Snaps manages a social media page featuring high-quality city outfit photos. However, large unoptimized image files slow down the upload process. This Python script resizes all images in a folder to specific dimensions (e.g., 1080x1080) and optimizes them for faster upload while preserving quality.

## Features
- Resizes images while maintaining aspect ratio.
- Supports custom width or height adjustments.
- Processes all images in a given folder.
- Saves resized images to a specified output folder.
- Uses **PIL (Pillow)** for efficient resizing and optimization.

## Skills Used
- **Python Scripting**: Automating bulk image resizing.
- **Pillow (PIL)**: Handling image processing.
- **File Handling**: Reading from and saving to directories.

## Installation
```sh
# Clone the repository
git clone https://github.com/junecodes767/bulk-image-resizer.git
cd bulk-image-resizer



## Usage
Place the images you want to resize in the `Photos-to-adjust` folder and run the script:
```sh
python image_resizer.py
```

Example output:
```
Photo1.jpg resized
Photo2.jpg resized
Photo3.jpg resized
...
All images processed successfully.
```

### Folder Structure:
```
Bulk-Image-Resizer-Optimizer/
│── Photos-to-adjust/   # Folder containing original images
│── Modified-photos/    # Folder where resized images will be saved
│── image_resizer.py    # Script to execute the resizing process
```

## Portfolio Focus
This project highlights **automation**, **image processing**, and **file management**, showcasing expertise in efficient handling of bulk image optimization.


