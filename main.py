import speech_recognition as sr
import webbrowser
import pyttsx3
import sys
import musicLibrary as mL
recoginzer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
#To process commands
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif "exit" in c.lower():
        speak("Thank you for spending time with me. Take care and have a great day!")
        sys.exit()
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = mL.music[song]
        webbrowser.open(link)
    elif "tell me about yourself" in c.lower():
        speak("Hello! I'm Neura, your personal desktop speech assistant. I'm here to help you with tasks, answer your queries, and make your day a little easier. Fun fact: I was created by a brilliant solo developer named Mozeel Hashmi!")
    else:
        speak("Hmm, that doesn't seem to match anything I know. Can you try again?")

if __name__ == "__main__":
    speak("Initializing Neura!.......")
    #Listen for the wake word "Neura!"
    while True:
        
        # recognize speech
        print("Recognizing.....")
        try:
            # obtain audio from the microphone
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening.........")
                audio = r.listen(source, timeout=2, phrase_time_limit=2) #To adjust the timming
            word = r.recognize_google(audio)
            if word.lower()=="neura":
                speak("Yes")
                #listen for command
                with sr.Microphone() as source:
                    print("Neura is Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print(e)