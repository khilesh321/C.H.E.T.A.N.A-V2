import requests
import io
from PIL import Image
from Features.SpeakHotword import speak, takeCommand

def generate_image(prompt):
    try:
        speak("Wait for a minute...")
        prompt = prompt.replace("generate image of ", "").replace("generate image ", "")
        API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                response.raise_for_status()  # Raise an exception for HTTP errors
                return response.content
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred!!")
                return None
            except requests.exceptions.RequestException as req_err:
                print(f"Request error occurred!!")
                return None

        image_bytes = query({
            "inputs": prompt,
        })

        if image_bytes is None:
            speak("Failed to generate image. Please try again.")
            return

        image = Image.open(io.BytesIO(image_bytes))
        speak('Here is your requested image...')
        image.show()

        while True:
            query = takeCommand().lower()
            if 'close' in query:
                import pyautogui
                pyautogui.hotkey('ctrl', 'w')
                break
                # image.close()

    except Exception as e:
        print(f"Sorry, An error occurred: {e}")
        speak(f"Sorry, An error occurred.")
        

if __name__ == '__main__':
    generate_image("generate image of beautiful lady whose age is 18 years")