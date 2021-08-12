import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis AI, Please tell me how may I help you")

def takeCommand():
    # it takes microphone input and string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listing......")
        r.pause_threshold = 2
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="en-in")
        print(f'User said : {query} \n')
    except Exception as e:
        print("somthing wrong...say again...")
        return "None"
    return query

if __name__ == "__main__":
    WishMe()
    while(True):
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open javatpoint' in query:
            webbrowser.open("javatpoint.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'open my gmail' in query:
            webbrowser.open("gmail.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            vsPath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsPath)

        elif 'bye bye thank you' in query:
            exit(0)