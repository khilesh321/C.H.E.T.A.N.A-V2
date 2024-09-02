import pyttsx3
import speech_recognition
from rich import print
from Features.RPrint import rprint
from threading import Thread
import pygame
from Features.print_with_time import print_time

id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", id)
rate = engine.setProperty('rate',160)

is_Hot_Word = False
hot_word_detc_is_ON = False

def speak(audio,PRINT=True):
    engine.say(audio)
    if PRINT:
        Thread(target=print_time,args=(audio,)).start()
    engine.runAndWait()
    
def speak_instant(audio,PRINT=True):
    engine.say(audio)
    if PRINT:
        print(f'C.H.E.T.A.N.A : {audio}')
    engine.runAndWait()
    

def speak_for_hotword(audio):
    global is_Hot_Word,hot_word_detc_is_ON
    
    hot_word_detc_is_ON = True
    Thread(target=hotword_detect).start()
    # print(f'C.H.E.T.A.N.A : {audio}')
    engine.save_to_file(audio, "data.wav")
    engine.runAndWait()
    
    try:
        pygame.mixer.init()
        pygame.mixer_music.load(r"data.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            if is_Hot_Word:
                is_Hot_Word = False
                break
    except Exception as e:
        print(e)
    finally:
        hot_word_detc_is_ON = False
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    
    

def hotword_detect():
    global is_Hot_Word, hot_word_detc_is_ON
    while True:
        if hot_word_detc_is_ON:
            user_input = takeCommand_hotword(PRINT=False).lower()
            if "stop chetana" in user_input or 'stop stop' in user_input or 'stop' in user_input:
                is_Hot_Word = True
                hot_word_detc_is_ON = False
                return
        else:
            return

def speak_welcome():
    audio1 = "I'm Cognitive Helper for Efficient Task Automation and Navigate Assistance."
    # print(f"[blue]{audio1} (C.H.E.T.A.N.A)[/blue]")
    # engine.runAndWait()
    
    engine.say("Welcome sir, " + audio1)
    Thread(target=print_time,args=(audio1,"blue")).start()
    engine.runAndWait()
    

def passCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        rprint("Listening...", 'green')
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=None)

    try:
        rprint("Understanding...", 'yellow')
        query = r.recognize_google(audio, language='en-in')
        query = query.replace("Chetna", "Chetana")
        query = query.replace("chetna", "Chetana")
        print(f"You Said: [green]{query}[/green]")
    except Exception as e:
        rprint("Say that again...", 'white')
        return "None"
    return query

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        # r.adjust_for_ambient_noise(source)
        # print(" " * 20, end="\r", flush=True)
        # print("[green]Listening.....[/green]",end="\r",flush=True)
        
        rprint("Listening...",'green')
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source,timeout=None)
        
        # r.dynamic_energy_threshold = False #when user is calm then microphone sense this energy but we declare it as false becz no need of that now...
        # r.energy_threshold = 300
        # r.dynamic_energy_adjustment_damping = 0.03 #less damping means voice is accesible from far of mic
        # r.dynamic_energy_ratio = 1.9
        # r.pause_threshold = 0.4 #depends on speed of speech of user more slow means more pause_thresold value
        # r.operation_timeout = None #time of timeout when it stops listening
        # r.pause_threshold = 0.2
        # r.non_speaking_duration = 0.3
        # audio = r.listen(source,timeout=None)
        


    try:
        # print(" " * 20, end="\r", flush=True)
        # print("[yellow]Understanding...[/yellow]",end="\r",flush=True)
        rprint("Understanding...",'yellow')
        query  = r.recognize_google(audio,language='en-in')
        query = query.replace("Chetna","Chetana")
        query = query.replace("chetna","Chetana")
        query = query.replace("Akhilesh","Khilesh")
        query = query.replace("khilesh","Khilesh")
        print(" " * 100, end="\r", flush=True)
        print(f"You Said: [green]{query}[/green]")
    except Exception as e:
        # print(" " * 20, end="\r", flush=True)
        # print("[white]Say that again...[/white]",end="\r",flush=True)
        rprint("Say that again...",'white')
        return "None"
    return query

def takeCommand_hotword(PRINT=True):
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        rprint("Listening...", 'green')
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source, timeout=None)

    try:
        rprint("Understanding...", 'yellow')
        query = r.recognize_google(audio, language='en-in')
        query = query.replace("Chetna", "Chetana")
        query = query.replace("chetna", "Chetana")
        query = query.replace("Akhilesh", "Khilesh")
        query = query.replace("khilesh", "Khilesh")
        print(" " * 100, end="\r", flush=True)
        if PRINT:
            print(f"You Said: [green]{query}[/green]")
    except Exception as e:
        return "None"
    return query

if __name__ == '__main__':
    # hot_word_detc_is_ON = True
    # hotword_detect()
    speak("hello sir, how can i assist you")
    takeCommand()