from datetime import datetime
import speech_recognition as sr
from speak import speak

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognization...")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
        if "stop" not in query and "bye" not in query:
            speak("ok sir")
        else:
            hour = datetime.now().hour
            if hour >= 21 or hour < 6:
                speak("Good Night sir, Take Care")
                print("Good Night sir, see you tomorrow")
            else:
                speak("Good Bye Sir, Have a Nice Day")
            exit()

    except Exception as e:
        print(f"ERROR : {e}")
        speak("Sorry sir , I could not understand , can you say it again?")
        query = "None"
    return query
