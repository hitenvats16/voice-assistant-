import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print("you said : " + query)

    except Exception as e:
        print("SAY Again")
        return "None"
    return query



def wish():
    speak("Hello")
    speak("I am Sophia...Version 0.1. Please tell me, how may i help you")

if __name__ == '__main__':
    wish()
    take()



