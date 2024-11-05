import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

rec = sr.Recognizer()
mic = sr.Microphone()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with mic as source:
        rec.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = rec.listen(source)
        text = rec.recognize_google(audio)
        return text

try:
    while True:
        command = listen()
        print(f"You said: {command}")
        speak_text(f"You said: {command}")
except KeyboardInterrupt:
    print("Exiting...")
