import pyttsx3
import speech_recognition as sr
import random
from Features.SpeakHotword import speak,takeCommand

def game_play():
    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("You Say First...")
    i = 0
    Me_score = 0
    Com_score = 0
    while(i<5):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score --> Your :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Com_score += 1
                print(f"Score --> Your :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Me_score += 1
                print(f"Score --> Your :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score --> Your :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score --> Your :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Com_score += 1
                print(f"Score --> Your :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score --> Your :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score --> Your :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                print(f"Score --> Your :- {Me_score} : COM :- {Com_score}")
        i += 1
    
    speak(f"FINAL SCORE --> Your :- {Me_score} : COM :- {Com_score}")
    

            

