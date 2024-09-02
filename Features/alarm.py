import pyttsx3
import datetime
import os 
from Features.SpeakHotword import speak


extractedtime = open("E:\\Chetana_Final\\texts\\Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("E:\\Chetana_Final\\texts\\Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            os.startfile(r"E:\Chetana_Final\Stuff\music.mp3")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)
