import tkinter as tk
from PIL import Image, ImageTk

#Setup
root = tk.Tk()
root.title("Remote Filmmaking Software")
root.geometry('1000x700')
root.configure(background='black')
root.resizable(False, False)

#Title 
image = Image.open("UI/assets/remotefilmcontrols.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo, borderwidth=0)
label.pack()


class LiveFeed():
    def __init__(self, window, cap, image):
        self.window = window
        self.cap = cap
        self.width = 960
        self.height = 540
        self.interval = 1000 # Interval in ms to get the latest frame
        # Create canvas for image
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack()
        # Update image on canvas
        self.update_image(image)

    def update_image(self, image):
        # Get the latest frame and convert image format
        self.image = image # to RGB
        self.image = Image.fromarray(self.image) # to PIL format
        self.image = ImageTk.PhotoImage(self.image) # to ImageTk format
        # Update image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        # Repeat every 'interval' ms
        self.window.after(self.interval, self.update_image(image))

    