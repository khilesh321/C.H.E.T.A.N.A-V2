from groq import Groq
# from ListenAndSpeak import speak
from Features.SpeakHotword import speak_for_hotword
from rich import print

def execute(prompt):
    if prompt == "none" or prompt == "None" : return
    client = Groq(api_key="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")
    completion = client.chat.completions.create(
    model="llama3-groq-8b-8192-tool-use-preview",
    messages=[
        {
            "role": "system",
            "content": "response should be short and concise if not mentioned in prompt."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
    # response = ''
    # for chunk in completion:
        
    #     response += chunk.choices[0].delta.content or ""
    # speak_for_hotword(response)
    # return response
    response = ''
    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content is not None:
            print(f"[#FF69B4]{content}[/#FF69B4]", end="")
            response += content
    print("\n")
    speak_for_hotword(response)
        
        
        

if __name__ == "__main__":
    (execute("tell me about cristiano ronaldo"))