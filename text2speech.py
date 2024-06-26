# Python3 code goes here Creating J.A.R.V.I.S. powered by GROQ and Python
#  URL: https://www.youtube.com/watch?v=HQ-wAw88X1I
import os
from deepgram import DeepgramClient, SpeakOptions

SPEAK_OPTIONS = {"text": "Hello, how can I help you today?"}
filename = "output.wav"

def text2speech(text):
    try:
        SPEECH_OPTIONS = {"text": text}
        deepgram = DeepgramClient(api_key=os.getenv("DG_API_KEY"))
        
        options = SpeakOptions(
            model="aura-asteria-en",
            encoding="linear16",
            container="wav"
        )

        response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
        return filename
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    text2speech("This is a test")