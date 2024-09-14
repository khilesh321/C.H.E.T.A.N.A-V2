import pyttsx3
import datetime
from Features.SpeakHotword import speak
from Features.Messages import ask_msg
import random
# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# engine.setProperty("rate",200)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon,sir")

    else:
        speak("Good Evening,sir")

    # msg = random.choice(ask_msg)
    # speak(msg)
    speak("Please tell me, How can I help you ?")

if __name__ == "__main__":
    greetMe()

