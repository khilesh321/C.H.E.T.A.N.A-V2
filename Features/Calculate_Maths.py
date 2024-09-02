import pyttsx3
import speech_recognition
import wolframalpha
from Features.SpeakHotword import speak


# Assistant =pyttsx3.init('sapi5')
# voices = Assistant.getProperty('voices')
# print(voices)
# Assistant.setProperty('voices',voices[0].id)
# Assistant.setProperty('rate', 200 )

# def Speak(audio):
#     print("    ")
#     Assistant.say(audio)
#     print(f": {audio}")
#     Assistant.runAndWait()

def Wolfram(query):
      api_key = "LR33QE-LUP5Q99YK4"
      requester = wolframalpha.Client(api_key)
      requested = requester.query(query)

      try:
        Answer = next(requested.results).text
        return Answer
      except:
       speak("Sorry sir but the value is not answerable!")



def calc(query):
    Term = str(query)
    Term = Term.replace("ERA"," ")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("multiply","*")

    Final = str(Term)
    
    try: 
        result = Wolfram(Final)
        speak(result)

    except:
        speak("Sorry sir the query is not ansewerable!")
        
if __name__ == "__main__":
  calc("calculate 50 X 40")
