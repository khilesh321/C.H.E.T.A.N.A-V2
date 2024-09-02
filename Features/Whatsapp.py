import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime
from Features.SpeakHotword import speak

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 1)).strftime("%M"))

def sendMessage():
    speak("Who do you want to message?")
    a = int(input('''Person 1 - 1
    Person 2 - 2'''))
    if a == 1:
        speak("Whats the message?")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+919763534104",message,time_hour=strTime,time_min=update) #Enter The number here instead of +91000
    elif a==2:
        pass
    
if __name__ == "__main__":
    sendMessage()

