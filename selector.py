import os
from tkinter import Tk, Button, Label, Frame, messagebox
from PIL import Image, ImageTk

# Paths
source_dir = '/home/anqiao/Pictures/singapore'
target_dir = '/home/anqiao/Pictures/singapore_s'

# Function to extract the numerical part from the filename
def extract_number(filename):
    base = os.path.basename(filename)  # Extract the basename (in case of full paths)
    number_part = base.split('_')[1].split('.')[0]  # Split by underscore and dot, then take the number part
    return int(number_part)

# Fetch all jpg files from the source directory
images = [img for img in os.listdir(source_dir) if img.endswith('.JPG')]

# Sort the list using the extract_number function as the key
images = sorted(images, key=extract_number)

# Initialize the index to track the current image
current_image_index = 0
last_window_size = (0, 0)
current_window_size = (0, 0)

########################################################
# #########################Buttons######################
# Function to save image and load next
def save_image():
    global current_image_index
    if current_image_index < len(images):
        source_path = os.path.join(source_dir, images[current_image_index])
        target_path = os.path.join(target_dir, images[current_image_index])
        os.rename(source_path, target_path)
    move_to_next_image()

# Function to skip to the next image
def skip_image():
    move_to_next_image()

# Function to move to the next image, used by both save_image and skip_image
def move_to_next_image():
    global current_image_index
    if current_image_index < len(images) - 1:
        current_image_index += 1
        load_image()
    else:
        messagebox.showwarning("End of List", "You have reached the last image.")


def back_image():
    global current_image_index
    if current_image_index > 0:
        current_image_index -= 1
    else:
        messagebox.showwarning("End of List", "You have reached the first image.")
    load_image()

#############################################
################### Resize ##################
def on_resize(event):
    # Resize and display the current image to fit the resized window
    global last_window_size, current_window_size
    current_window_size = (window.winfo_width(), window.winfo_height())
    if current_window_size != last_window_size:
        print("resize")
        print("last", last_window_size)
        print("current", current_window_size)
        last_window_size = current_window_size
        load_image()

# Function to load and display the current image
def load_image(init = False):
    global last_window_size, current_window_size
    if current_image_index < len(images):
        img_path = os.path.join(source_dir, images[current_image_index])
        img = Image.open(img_path)
        if init:
            img.thumbnail((800, 600))  # Initial thumbnail size
        else:            
            img.thumbnail((current_window_size[0]-102, current_window_size[1]-43))  # Resize to fit the window
        img_display = ImageTk.PhotoImage(img)
        label.config(image=img_display)
        label.image = img_display 
    else:
        window.quit()

# Set up the tkinter GUI window
window = Tk()
window.title('Image Selector')
window.geometry('800x600')

# Frame for image display
image_frame = Frame(window)
image_frame.pack()

# Label for displaying images
label = Label(image_frame)
label.pack()

# Frame for buttons
button_frame = Frame(window)
button_frame.pack()

# Buttons for saving and skipping images
back_button = Button(button_frame, text="Back", command=back_image)
back_button.pack(side='left', padx=5, pady=5)

save_button = Button(button_frame, text="Yes", command=save_image)
save_button.pack(side='left', padx=5, pady=5)

skip_button = Button(button_frame, text="Skip", command=skip_image)
skip_button.pack(side='left', padx=5, pady=5)
# Load the first image
load_image(init=True)
last_window_size = (window.winfo_width(), window.winfo_height())
current_window_size = (window.winfo_width(), window.winfo_height())

# Bind the resize event
window.bind('<Configure>', on_resize)

# Start the GUI event loop
window.mainloop()

