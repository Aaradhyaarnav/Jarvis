import speech_recognition as sr 
import webbrowser
import pyttsx3
import time
import music_library
import requests
from client import aiProcess
import os
import subprocess

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
newsapi="YOUR API KEY"
is_paused = False

def speak(text):
    engine.say(text)
    engine.runAndWait()


def run_as_admin(path_to_exe):
    # This command runs your exe as admin
    subprocess.run([
        "powershell", 
        "Start-Process", f'"{path_to_exe}"', 
        "-Verb", "runAs"
    ], shell=True)


def processCommand(c):
    
    output = ""

    global is_paused

    if "pause listening" in c.lower():
        is_paused = True
        speak("Okay, I will pause listening. Say 'resume listening' to continue.")
        return  # Stop here, don't do anything else

    elif "resume listening" in c.lower():
        is_paused = False
        speak("Resuming listening.")
        return

    elif "stop jarvis" in c.lower() or "exit jarvis" in c.lower():
        speak("Goodbye!")
        os._exit(0)


    elif "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open my channel" in c.lower():
        webbrowser.open("https://www.youtube.com/@AaradhyMine")

    elif "open my youtube studio" in c.lower():
        webbrowser.open("https://studio.youtube.com/channel/UCph3hMPbRtU4yqSWM63PTAA")
    
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        link= music_library.song[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    
    elif "who is aaradhy" in c.lower():
        speak("Aaradhy is the creator of this jarvis and is my god , he is the most intelligent person in the world , he loves coding and he recently leared python from youtube.")

    elif "who is barkha" in c.lower():
        speak("Barkha is the mother of my god Aaradhy Badjatya. She is a very sweet,caring and lovely person.")
    
    elif "who is vivek" in c.lower():
        speak("Vivek is the father of my creator Aaradhy Badjatya . He is a very caring and lovely guy.")
    
    elif "who is akshara" in c.lower():
        speak("Akshara is the sister of the great Aaradhy badjatya . Her nose is as round as a  frying pan.")
    
    elif "who is vani" in c.lower():
        speak("Vani is the older sister of my creator Aaradhy Badjatya . She is an employee in a mumbai company TIAA . Her nickname is 1 gb data ")

    elif "open tlauncher" in c.lower():
        os.startfile("C:\\Users\\aarad\AppData\\Roaming\\.minecraft\\TLauncher.exe")

    elif "open valorant as admin" in c.lower():
        run_as_admin( r"C:\Riot Games\Riot Client\RiotClientServices.exe")
    
    elif "open stumble guys as admin" in c.lower():
        run_as_admin(r"C:\Program Files\BlueStacks_nxt\HD-Player.exe")

    elif "open geometry dash as admin" in c.lower():
        run_as_admin(r"C:\Program Files\BlueStacks_nxt\HD-Player.exe")

    elif "open free fire as admin" in c.lower():
        run_as_admin(r"C:\Program Files\BlueStacks_nxt\HD-Player.exe")
        
    elif "open steam" in c.lower():
        os.startfile(r"C:\Program Files (x86)\Steam\Steam.exe")

    elif "open powder" in c.lower():
        os.startfile(r"C:\Users\aarad\AppData\Local\Programs\powder-desktop\PowderInstaller.exe")
    
    elif "open spotify" in c.lower():
        os.system("start spotify")

    elif "open calculator" in c.lower():
        os.system("start calculator")
    
    elif "open notepad" in c.lower():
        os.system("start notepad")

    elif "open chat gpt" in c.lower():
        speak("Opening Chat Gpt")
        webbrowser.open("https://chatgpt.com/")

    elif "vs code" in c.lower():
        os.system(r"C:\Users\aarad\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    

    else: 
        try:
            output = aiProcess(c)

            if output!="":
                speak(output)

        except Exception as e:
            print(f"Error calling aiProcess: {e}")
            speak("Sorry, there was an error processing your request.")

    
if __name__=="__main__" :
    speak("Initialising Jarvis. Say 'Jarvis' to activate me.")

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # optional but helps

        while True:
            print("Waiting for 'Jarvis'...")  # show always
            try:
                audio = r.listen(source)  # no timeout, no phrase_time_limit
                word = r.recognize_google(audio)

                print(f"You said: {word}")

                if "jarvis" in word.lower():   # can also do == "jarvis"
                    speak("Yes?")
                    print("Listening for your command...")

                    audio = r.listen(source)  # listen full command
                    command = r.recognize_google(audio)
                    print(f"You said: {command}")

                    processCommand(command)

            except sr.UnknownValueError:
                # Just keep listening if nothing was recognized
                continue
            except sr.RequestError as e:
                print(f"Jarvis error; {e}")
            time.sleep(0.5)
