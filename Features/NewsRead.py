import requests
import json
import pyttsx3

from Features.SpeakHotword import speak, takeCommand

def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=baee5999bc0e4173b084713b00e1f170",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=baee5999bc0e4173b084713b00e1f170",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=baee5999bc0e4173b084713b00e1f170",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=baee5999bc0e4173b084713b00e1f170",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=baee5999bc0e4173b084713b00e1f170",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=baee5999bc0e4173b084713b00e1f170"
    }
    a = ""
    content = None
    url = None
    print("Which type of news, business, health, technology, sports, entertainment, science")
    speak("Which type of news", PRINT=False)
    field = takeCommand()
    # field = input("Enter: ")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            news = requests.get(url).text
            news = json.loads(news)

            arts = news["articles"]
            
    stop_funtion_on = True
    first = True
    while stop_funtion_on:
        for articles in arts:
            article = articles["title"]
            if first :
                speak("Here is the first news.\n"+article)
                first = False
            else :
                speak(article)
            news_url = articles["url"]
            print(f"For more info visit: {news_url}")

            speak("Would you want to continue next news?")
            # a = input("Enter:").strip().lower()
            a = takeCommand().lower()
            a = a.replace("one", '1')
            a = a.replace("two", '2')
            a = a.replace("too", '2')
            a = a.replace("to", '2')
            if "yes" in str(a):
                pass
            elif "no" in str(a):
                speak("Okay, That's all")
                stop_funtion_on = False
                break
    return

if __name__ == '__main__':
    latestnews()
