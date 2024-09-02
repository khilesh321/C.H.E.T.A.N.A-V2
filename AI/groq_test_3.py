from groq import Groq
from Features.SpeakHotword import speak_for_hotword, takeCommand
from rich import print

class ChatHistory:
    def __init__(self):
        self.history = []

    def add_message_detailed(self, role, content):
        self.history.append({
            "role": role,
            "content": content
        })

    def add_message_concise(self, role, content):
        self.history.append({
            "role": "system",
            "content": "response should be short and concise if not mentioned in prompt."
        })
        self.history.append({
            "role": role,
            "content": content
        })

    def add_message(self, role, content):
        self.add_message_concise(role, content)

    def get_history(self):
        return self.history

def execute(prompt, chat_history):
    if prompt.lower() in ["none", ""]:
        return

    client = Groq(api_key="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")

    # Check if the prompt contains the keyword "detailed"
    if "detailed" in prompt.lower() or "detail" in prompt.lower():
        chat_history.add_message_detailed("user", prompt)
        messages = chat_history.get_history()

        # If the keyword is present, pass a different set of parameters to control the response length
        completion = client.chat.completions.create(
            model="llama3-groq-8b-8192-tool-use-preview",
            messages=messages,
            temperature=1,
            max_tokens=2048,
            top_p=1,
            stream=True,
            stop=None,
        )
    else:
        chat_history.add_message_concise("user", prompt)
        messages = chat_history.get_history()

        # If the keyword is not present, pass the default parameters for a concise response
        completion = client.chat.completions.create(
            model="llama3-groq-8b-8192-tool-use-preview",
            messages=messages,
            temperature=1,
            max_tokens=128,
            top_p=1,
            stream=True,
            stop=None,
        )

    response = ''
    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content is not None:
            print(f"[#FF69B4]{content}[/#FF69B4]", end="")
            response += content
    print("\n")
    speak_for_hotword(response)
    chat_history.add_message("assistant", response)

if __name__ == "__main__":
    while True:
        chat_history = ChatHistory()
        while True:
            prompt = takeCommand()
            execute(prompt, chat_history)