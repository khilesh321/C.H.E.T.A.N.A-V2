from tkinter import * #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow
import time
import pygame  #pip install pygame
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("600x500+1200+40")
root.title("Face Recognition")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("E:\\Chetana_Final\\Stuff\\face_recognition2.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    # i=0
    mixer.music.load("E:\\Chetana_Final\\Stuff\\face_recognition_sound.wav")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((600,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()

if __name__ == "__main__":
    play_gif()
    # root.mainloop()
