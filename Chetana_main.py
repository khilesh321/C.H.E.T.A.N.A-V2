import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from logging import root
import threading
from logging import root
import threading
import datetime

from email import message
import webbrowser
# from numpy import tile
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import pyautogui
import random
from plyer import notification
from pygame import mixer
import speedtest
from rich import print
from Features.RPrint import rprint
# from ListenAndSpeak import 
# from NetHyTech_HindiTTS import Speak as speak
# from Features.myetest2 import speak
from Features.SpeakHotword import takeCommand, speak_welcome, speak
from AI.ImageGeneration2 import generate_image
from auth.recoganize import AuthenticateFace
from AI.groq_test4 import ChatHistory,execute
chat_history = ChatHistory()

def play_video():
    from Features.VideoPlayer import play_vid
    play_vid()

def main_code():
    # import datetime
    # from email import message
    # import webbrowser
    # from numpy import tile
    # import pyttsx3
    # import speech_recognition
    # import requests
    # from bs4 import BeautifulSoup
    # import os
    # import pyautogui
    # import random
    # from plyer import notification
    # from pygame import mixer
    # import speedtest
    # from rich import print
    # from RPrint import rprint
    # from ListenAndSpeak import takeCommand,speak,speak_welcome
    
    

    for i in range(3):
        speak("Please,tell me your Password sir.")
        a = takeCommand().lower()
        a = a.replace("the password is ","")
        a = a.replace("khilesh","Khilesh")
        a = a.replace("password is ","")
        a = a.replace("Akhilesh","Khilesh")
        # a = input("Enter Password to Wake up CHETANA :- ")
        pw_file = open("E:\\Chetana_Final\\texts\\password.txt","r")
        pw = pw_file.read()
        pw_file.close()
        if (a==pw):
            speak("Get ready for Face Recognition...")
            from Features.INTRO import play_gif
            face_thread = threading.Thread(target=(AuthenticateFace))
            face_thread.start()
            play_gif()
            face_thread.join()
            
            # AuthenticateFace()
            speak('Face Recognition Successful')
            print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
            # Create a thread for playing the video
            from Features.Notification import show_notification
            threading.Thread(target=(show_notification)).start()
            vid_thread = threading.Thread(target=play_video)
            vid_thread.daemon = True  # Set as daemon thread so it exits when main thread exits
            vid_thread.start()
            
            # from Notify import activation_notify
            # activation_notify()           
            # from VideoPlayer import play_vid
            # play_vid()
            break
        elif (i==2 and a!=pw):
            exit()

        elif (a!=pw):
            print("C.H.E.T.A.N.A : [#FF0000]Password is Wrong!, Try Again.[/#FF0000]")
            

    

    # from VideoPlayer import play_vid
    # play_vid()


    # engine = pyttsx3.init("sapi5")
    # voices = engine.getProperty("voices")
    # engine.setProperty("voice", voices[1].id)
    # rate = engine.setProperty("rate",200)

    # def speak(audio):
    #     engine.say(audio)
    #     print(f'Jarvis : {audio}')
    #     engine.runAndWait()

    # def takeCommand():
    #     r = speech_recognition.Recognizer()
    #     with speech_recognition.Microphone() as source:
    #         print("[green]Listening.....[/green]",end="\r")
    #         r.pause_threshold = 0.5
    #         r.energy_threshold = 300
    #         audio = r.listen(source,timeout=None)
            
    #         # r.dynamic_energy_threshold = False #when user is calm then microphone sense this energy but we declare it as false becz no need of that now...
    #         # r.energy_threshold = 300
    #         # r.dynamic_energy_adjustment_damping = 0.03 #less damping means voice is accesible from far of mic
    #         # r.dynamic_energy_ratio = 1.9
    #         # r.pause_threshold = 0.4 #depends on speed of speech of user more slow means more pause_thresold value
    #         # r.operation_timeout = None #time of timeout when it stops listening
    #         # r.pause_threshold = 0.2
    #         # r.non_speaking_duration = 0.3
    #         # audio = r.listen(source,timeout=None)
            


    #     try:
    #         print("[yellow]Understanding...[/yellow]",end="\r")
    #         query  = r.recognize_google(audio,language='en-in')
    #         print(f"You Said: [green]{query}[/green]")
    #     except Exception as e:
    #         print("Say that again")
    #         return "None"
    #     return query

    def alarm(query):
        timehere = open("E:\\Chetana_Final\\texts\\Alarmtext.txt","a")
        timehere.write(query)
        timehere.close()
        os.startfile(r"E:\Chetana_Final\Alarm\alarm.py")


    if __name__ == "__main__":
        # from VideoPlayer import play_vid
        # play_vid()
        
        # from Listening_gif import play_gif
        # play_gif()
        # root.mainloop()

        speak_welcome()
        while True:
            query = takeCommand().lower()
            if "wake up" in query : #or "hey chetana" in query or "hey chetna" in query or "hello chetana" in query or "hello chetna" in query
                from Features.GreetMe import greetMe
                greetMe()

                while True:
                    query = takeCommand().lower()
                    if "go to sleep" in query:
                        speak("Ok sir , You can call me anytime")
                        break
                    
                    #################### --CHETANA-- #####################

                    elif "change password" in query:
                        speak("What's the new password")
                        new_pw = input("Enter the new password\n")
                        new_password = open("E:\\Chetana_Final\\texts\\password.txt","w")
                        new_password.write(new_pw)
                        new_password.close()
                        speak("Done sir")
                        speak(f"Your new password is{new_pw}")

                    elif "schedule my day" in query:
                        tasks = [] #Empty list 
                        speak("Do you want to clear old tasks (Plz speak YES or NO)")
                        query = takeCommand().lower()
                        if "yes" in query:
                            file = open("E:\\Chetana_Final\\texts\\tasks.txt","w")
                            file.write(f"")
                            file.close()
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            i = 0
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("E:\\Chetana_Final\\texts\\tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                        elif "no" in query:
                            i = 0
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("E:\\Chetana_Final\\texts\\tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()

                    elif "show my schedule" in query:
                        file = open("E:\\Chetana_Final\\texts\\tasks.txt","r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("E:\\Chetana_Final\\Stuff\\notification.mp3")
                        mixer.music.play()
                        notification.notify(
                            title = "My schedule :-",
                            message = content,
                            timeout = 15
                        )

                    elif "focus mode" in query:
                        a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                        if (a==1):
                            speak("Entering the focus mode....")
                            os.startfile("E:\\Chetana_Final\\FocusMode.py")
                            exit()

                        
                        else:
                            pass

                    elif "show my focus" in query:
                        from Features.FocusGraph import focus_graph
                        focus_graph()

                    # elif "translate" in query:
                    #     from Translator import translategl
                    #     query = query.replace("jarvis","")
                    #     query = query.replace("translate","")
                    #     translategl(query)

                    


                    elif "open" in query:   #EASY METHOD
                        query = query.replace("open","")
                        query = query.replace("jarvis","")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(1.5)
                        pyautogui.press("enter")                       
                        
                    elif "internet speed" in query:
                        wifi  = speedtest.Speedtest()
                        upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                        download_net = wifi.download()/1048576
                        print("Wifi Upload Speed is", upload_net)
                        print("Wifi download speed is ",download_net)
                        speak(f"Wifi download speed is {download_net}")
                        speak(f"Wifi Upload speed is {upload_net}")
                        

                    elif "ipl score" in query:
                        from plyer import notification  #pip install plyer
                        import requests #pip install requests
                        from bs4 import BeautifulSoup #pip install bs4
                        url = "https://www.cricbuzz.com/"
                        page = requests.get(url)
                        soup = BeautifulSoup(page.text,"html.parser")
                        team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                        team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                        team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                        team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                        a = print(f"{team1} : {team1_score}")
                        b = print(f"{team2} : {team2_score}")

                        notification.notify(
                            title = "IPL SCORE :- ",
                            message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                            timeout = 15
                        )
                    
                    elif "play a game" in query:
                        from Features.game import game_play
                        game_play()

                    elif "screenshot" in query:
                        import pyautogui #pip install pyautogui
                        im = pyautogui.screenshot()
                        im.save("ss.jpg")

                    elif "click my photo" in query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("SMILE")
                        pyautogui.press("enter")

                    
                    

                    ############################################################
                    elif "hello" in query:
                        speak("Hello sir, how are you ?")
                    elif "i am fine" in query:
                        speak("that's great, sir")
                    elif "how are you" in query:
                        speak("Perfect, sir")
                    elif "how r u" in query:
                        speak("Perfect, sir")
                    elif "thank you" in query:
                        speak("you are welcome, sir")
                    
                    elif "tired" in query:
                        speak("Playing your favourite songs, sir")
                        a = (1,2,3)
                        b = random.choice(a)
                        if b==1:
                            webbrowser.open("https://www.youtube.com/watch?v=E3jOYQGu1uw&t=1246s&ab_channel=scientificoder")
                        

                    # elif "pause" in query:
                    #     pyautogui.press("k")
                    #     # speak("video paused")
                    # elif "play" in query:
                    #     pyautogui.press("k")
                    #     # speak("video played")
                    # elif "mute" in query:
                    #     pyautogui.press("m")
                    #     # speak("video muted")
                    


                    # elif "volume up" in query:
                    #     from keyboard import volumeup
                    #     speak("Turning volume up,sir")
                    #     volumeup()
                    # elif "volume down" in query:
                    #     from keyboard import volumedown
                    #     speak("Turning volume down, sir")
                    #     volumedown()

                    elif "open" in query:
                        from Features.Open_Close_app import openappweb
                        openappweb(query)
                    elif "close" in query:
                        from Features.Open_Close_app import closeappweb
                        closeappweb(query)


                    elif "google" in query:
                        from Features.SearchNow import searchGoogle
                        searchGoogle(query)
                    elif "youtube" in query:
                        from Features.SearchNow import searchYoutube
                        query2 = searchYoutube(query)
                        from Features.Open_Close_app import closeappweb
                        closeappweb(query2)
                    elif "wikipedia" in query:
                        from Features.SearchNow import searchWikipedia
                        searchWikipedia(query)

                    
                    elif "news" in query:
                        from Features.NewsRead import latestnews
                        latestnews()

                    elif "calculate" in query:
                        # from Calculate_Maths.Cal import Wolfram
                        from Features.Calculate_Maths import calc
                        query = query.replace("calculate","")
                        query = query.replace("jarvis","")
                        calc(query)

                    elif "whatsapp" in query:
                        from Features.Whatsapp import sendMessage
                        sendMessage()

                    

                    elif "temperature" in query or "weather" in query:
                        # search = "weater in korpawli"
                        # url = f"https://www.google.com/search?q={search}"
                        # r  = requests.get(url)
                        # data = BeautifulSoup(r.text,"html.parser")
                        # temp = data.find("div", class_ = "BNeawe").text
                        # speak(f"current{search} is {temp}")
                        
                        speak('Wait for a second...')
                        from Features.weather_fore import weather_forecast2
                        weather_data = weather_forecast2()
                        if weather_data:
                            weather, temp, feels_like = weather_data
                            
                            speak(f"Weather: {weather}")
                            speak(f"Temperature: {temp}")
                            speak(f"Feels like: {feels_like}")
                        else:
                            speak("Failed to retrieve weather data")
                            
                        
                    

                    elif "set an alarm" in query:
                        print("input time example:- 10 and 10 and 10")
                        speak("Set the time")
                        a = input("Please tell the time :- ")
                        alarm(a)
                        speak("Done,sir")
                            
                    elif "the time" in query:
                        strTime = datetime.datetime.now().strftime("%H:%M")    
                        speak(f"Sir, the time is {strTime}")
                    elif "finally sleep" in query:
                        speak("Going to sleep,sir")
                        exit()

                    # elif "remember" in query or "remember that" in query:
                    #     rememberMessage = query.replace("remember that","")
                    #     rememberMessage = query.replace("jarvis","")
                    #     speak("You told me to remember that"+rememberMessage)
                    #     remember = open(r"E:\Chetana_Final\texts\Remember.txt","a")
                    #     remember.write(rememberMessage)
                    #     remember.close()
                    # elif "what do you remember" in query:
                    #     remember = open("E:\\Chetana_Final\\texts\\Remember.txt","r")
                    #     speak("You told me to remember that" + remember.read())

                    elif "shutdown system" in query:
                        speak("Are You sure you want to shutdown")
                        shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                        if shutdown == "yes":
                            os.system("shutdown /s /t 1")

                        elif shutdown == "no":
                            break
                     
                    
                    elif "generate image" in query:
                        # query = query.replace("generate image of","")
                        generate_image(query)
                        # query2 = takeCommand().lower()
                        # if 'close' in query2:
                        #     import pyautogui
                        #     pyautogui.press('ctrl', 'w')
                    
                       
                    else : 
                        # from ChatBot import chatBot
                        # chatBot(query)
                        
                        execute(query,chat_history)


                




                


 

if __name__ == "__main__":

    # Run the main code
    main_code()
    
    