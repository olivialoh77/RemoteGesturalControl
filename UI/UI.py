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
label.grid()

# Create a frame
app = tk.Frame(root, bg="white")
app.grid()
# Create a label in the frame
lmain = tk.Label(app)
lmain.grid()

# function for video streaming
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 


#video_stream()
#root.mainloop()