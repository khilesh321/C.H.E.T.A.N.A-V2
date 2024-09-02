import pyttsx3
import speech_recognition
from rich import print
from Features.RPrint import rprint

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
rate = engine.setProperty("rate",185)



def speak(audio,PRINT=True):
    engine.say(audio)
    if PRINT:
        print(f'C.H.E.T.A.N.A : {audio}')
    engine.runAndWait()
    
def speak_welcome():
    audio1 = "I'm Cognitive Helper for Efficient Task Automation and Navigate Assistance."
    # audio2 = "Welcome sir, I'm Cognitive Helper for Efficient Task Automation and Navigate Assistance.(C.H.E.T.A.N.A)"
    engine.say("Welcome sir, "+ audio1)
    print(f"[blue]{audio1} (C.H.E.T.A.N.A)[/blue]")
    # rprint(audio2,'white')
    engine.runAndWait()
    
    
def passCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        rprint("Listening...",'green')
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,timeout=None)
        

    try:
        rprint("Understanding...",'yellow')
        query = r.recognize_google(audio,language='en-in')
        query = query.replace("Chetna","Chetana")
        query = query.replace("chetna","Chetana")
        print(f"You Said: [green]{query}[/green]")
    except Exception as e:
        # print(" " * 20, end="\r", flush=True)
        # print("[white]Say that again...[/white]",end="\r",flush=True)
        rprint("Say that again...",'white')
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






# # -------------------------------Deep Voices--------------------------
# from NetHyTech_DeepTTS import speak

# a = "aura-asteria-en" # Sophia (Female US English
# b = "aura-luna-en" # Emily (Female US English) 
# c = "aura-stella-en" # Rachel (Female US English)
# d = "aura-athena-en" # Eliza (Female UK English)
# e = "aura-hera-en" # Pam  (Female US English) 
# f = "aura-orion-en" # Kevin  (Male US English) 
# g = "aura-arcas-en" # Jeff (Male US English) 
# h = "aura-perseus-en" # Alex (Male US English) 
# i = "aura-angus-en" # Rory (Male Irish English) 
# j = "aura-orpheus-en" # John (Male US English) 
# k = "aura-helios-en" # Pete (Male UK English) 
# l = "aura-zeus-en" # James (Male US English) 

# speak("Welcome sir, I'm CHETANA",a)


if __name__ == '__main__':
    # while True:
    #     takeCommand()
    speak("Hello, sir how can i assist you?")
    
    


