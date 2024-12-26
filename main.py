import speech_recognition as sr
import webbrowser
import pyttsx3
import sys
import musicLibrary as mL
from openai import OpenAI
recoginzer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiProcess(command):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Neura, a virtual assistant like Alexa or Google Cloud. Respond with concise and relevant answers. Introduce yourself as created by Mozeel Hashmi, a 16-year-old solo developer passionate about Python and computer science. He aims to complete his FSC and pursue further skills in Germany."},
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return (completion.choices[0].message.content)
#To process commands
def processCommand(c):
    if c.lower().startswith("open"):
        site = c.lower().split(" ")[1]
        webbrowser.open(f"https://{site}.com")
        speak(f"Opening {site} for you.")
    elif "exit" in c.lower():
        speak("Thank you for spending time with me. Take care and have a great day!")
        sys.exit()
    elif c.lower().startswith("play"):
        speak("Sure! Let me play that for you.")
        song = c.lower().split(" ")[1]
        link = mL.music[song]
        webbrowser.open(link)
        speak(f"Now playing {song}")
    elif "tell me about yourself" in c.lower():
        speak("Hello! I'm Neura, your personal desktop speech assistant. I'm here to help you with tasks, answer your queries, and make your day a little easier. Fun fact: I was created by a brilliant solo developer named Mozeel Hashmi!")
    else:
        #let openAi handle the rest
        output = aiProcess(c)
        speak(output)

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