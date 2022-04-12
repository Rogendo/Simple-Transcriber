import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()
mic=sr.Microphone()
print("Say what you want to be transcribed here")
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)
    audio=r.recognize_google(audio)

    print("This is the transcribed text " +audio)