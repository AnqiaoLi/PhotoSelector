# PhotoSelector
This repo streamlines the process of picking out the best images from a large volume of photos.

## Overview
For photography enthusiasts, managing a large volume of photos can be a daunting task. Whether you're a professional photographer sorting through shots from your latest gig, or a hobbyist reviewing snaps from your recent vacation, this script provides the simplest tools to pick out the best images from the bunch.

## Getting Started
In the interactive UI, you can choose "Skip" (skip to next image), "Save" (save current image to the target folder) or "Back" (go back to the previous image) for each image. 
Please change the source_dir to the directory that contains the photos you want to selected from, and target_dir to the directroy the directory you want to save the selected images.

## Installation Instructions

This project relies on Tkinter for the graphical user interface and PIL (Python Imaging Library), now maintained as Pillow, for image processing. Follow the steps below to set up your environment and run the script.

### Prerequisites

Ensure you have Python installed on your system. This project is tested on Python 3.6 and above. You can check your Python version by running:

```bash
python --version
```

### Setting Up

1. **Install Python and pip (if not already installed):** Python's official website provides [guidance on installation](https://www.python.org/downloads/). `pip` is included by default with Python versions 3.4 and above.

2. **Install Tkinter:** Tkinter is included with most Python installations by default. However, if you're on a Linux system, you might need to install it separately. For Ubuntu and Debian-based systems, use:

    ```bash
    sudo apt-get install python3-tk
    ```

    For other systems, please refer to your package manager or Python installation instructions.

3. **Install Pillow:** Use `pip` to install Pillow, which is the actively maintained fork of PIL, by running:

    ```bash
    pip install Pillow
    ```

### Running the Script

Once you have the prerequisites installed, you can run the script directly from the command line:

```bash
python selector.py
```


