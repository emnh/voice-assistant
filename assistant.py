import speech_recognition as sr
import subprocess
import whisper
from TTS.api import TTS
from playsound import playsound

# Initialize the recognizer

r = sr.Recognizer()
model = whisper.load_model("base")


# Initialize TTS

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]

# model_name = "tts_models/en/ljspeech/glow-tts"
tts = TTS(model_name)

def playText(text):
    tts.tts_to_file(text, speaker=tts.speakers[0], language=tts.languages[0], file_path="response.wav")
    #tts.tts_to_file(text, file_path="response.wav")
    playsound("response.wav")

# def enumerate_models():
#     for model_name in TTS.list_models():
#         if not '/en/' in model_name:
#             continue
#         if 'tacotron' in model_name.lower():
#             continue
#         print(model_name)
        
#         # Run TTS
#         # ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
#         # Text to speech with a numpy output
        
#         try:
#             # Init TTS
#             tts = TTS(model_name)
#             #tts.tts_to_file("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0], file_path="response.wav")
#             text = "This is a test! This is also a test!!"
#             tts.tts_to_file(text, file_path="response.wav")
#             playsound("response.wav")
#         except Exception as e:
#             print(e)
#             print("Couldn't tts")
#             pass

playText("Hello, I am your personal assistant. How can I help you?")

# Define the listen function
def listen():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    # save the audio to a file
    with open("output.wav", "wb") as f:
        f.write(audio.get_wav_data())

    try:
        text = r.recognize_whisper(audio, language="english")
        print("You said: {}".format(text))
        # Keyboard noise sounds like "Thank you." to the model
        if text.strip() != '' and text.strip() != 'Thank you.':
            playText("You said: {}".format(text))
        return text
    except:
        print("Sorry, could not recognize your voice.")
        return ""

# Main loop
while True:
    text = listen()

    if "play music" in text:
        print("Play music")
    elif "quit" in text:
        break
