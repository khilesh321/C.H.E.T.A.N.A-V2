from hugchat import hugchat
from ListenAndSpeak import speak
import random

wait_msg = [
    "Alright, just a moment, sir.",
    "Okay, give me a second, sir.",
    "One second, sir.",
    "Just a moment, sir.",
    "Hold on a second, sir.",
    "I'll be right back, sir.",
    "Wait a moment, sir.",
    "Just give me a moment, sir.",
    "Okay, hold on, sir.",
    "Just a second, sir.",
    "Give me a moment, sir.",
    "Okay, just a minute, sir.",
    "Hold tight, sir.",
    "Hang on, sir.",
    "One moment, sir.",
    "Please wait a second, sir.",
    "I'll be right with you, sir.",
    "Just hold on for a moment, sir.",
    "Okay, one moment, sir.",
    "Let me just check, sir.",
    "Okay, hold up a second, sir.",
    "Wait for a moment, sir.",
    "Just hang on, sir.",
    "Hold on a bit, sir.",
    "Give me a quick second, sir.",
    "Okay, just a moment, sir.",
    "Please hold on, sir.",
    "Wait a minute, sir.",
    "Just a minute, sir.",
    "Hang tight, sir.",
    "Give me a second, sir.",
    "One moment, please, sir.",
    "Wait up, sir.",
    "Just hold on a second, sir.",
    "Okay, give me a moment, sir.",
    "Hold on for a bit, sir.",
    "I'll be back in a second, sir.",
    "Just a quick moment, sir.",
    "Please wait a bit, sir.",
    "Okay, give me a second, sir."
]

def chatBot(query):
    if query == "none" : return
    speak(f"{random.choice(wait_msg)}")
    user_input = query +". Give response in few words(length of response should be between 5 to 45 words)"
    # print("user : "+user_input)
    chatbot = hugchat.ChatBot(cookie_path="E:\\Chetana_Final\\cookies.json")
    if "change topic" in query :
        id = chatbot.new_conversation()
        chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    speak(response)
    return response

if __name__ == "__main__" :
    query = "what are you doing"
    chatBot(query)