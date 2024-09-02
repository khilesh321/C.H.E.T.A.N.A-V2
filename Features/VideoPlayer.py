import cv2
import tkinter as tk
from PIL import Image, ImageTk
from pygame import mixer
mixer.init()

# Create a Tkinter window
root = tk.Tk()
root.title("C.H.E.T.A.N.A")

# Set the GUI size to 640x480
root.geometry("640x520+1200+40")


# Keep the GUI panel on top of other windows
root.wm_attributes('-topmost', True)


# Create a label to display the video
label = tk.Label(root)
label.pack(fill="both", expand=True)  # Make the label expand to fill the GUI

# Load the video
cap = cv2.VideoCapture("E:\\Chetana_Final\\Stuff\\video.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)  # convert FPS to milliseconds
delay -= 1  # adjust the delay to make the video play smoothly

def display_frame():
    
    ret, frame = cap.read()
    if not ret:
        # Video has ended, reset to the beginning
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()
    
    # Resize the frame to a smaller size
    width, height = 640, 520  # adjust the size to your liking
    frame = cv2.resize(frame, (width, height))
    
    # Convert the frame to a Tkinter-compatible image
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(img)
    label.config(image=imgtk)
    label.image = imgtk
    # Schedule the next frame to be displayed
    root.after(delay, display_frame)

def play_vid():
    
    # Play the start sound
    mixer.music.load("E:\\Chetana_Final\\Stuff\\start_sound.mp3")
    mixer.music.play()

    # Start displaying the video
    display_frame()

    # Run the Tkinter event loop
    root.mainloop()
    
    
if __name__ == "__main__":
    play_vid()