from groq import Groq
from Features.SpeakHotword import speak_for_hotword
from rich import print

class ChatHistory:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        self.history.extend([
    {
        "role": "system",
        "content": "response should be short and concise if not mentioned in prompt."
    },
    {
        "role": role,
        "content": content
    }
])

    def get_history(self):
        return self.history

def execute(prompt, chat_history):
    if prompt == "none" or prompt == "None" : return
    client = Groq(api_key="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")
    chat_history.add_message("user", prompt)
    messages = chat_history.get_history()
    completion = client.chat.completions.create(
        model="llama3-groq-8b-8192-tool-use-preview",
        messages=messages,
        temperature=1,
        max_tokens=1024,
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
    chat_history.add_message("assistant", response)
    # speak_for_hotword(response)

if __name__ == "__main__":
    chat_history = ChatHistory()
    while True:
        prompt = input("User: ")
        execute(prompt, chat_history)