import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# print(voices[1].id) === For Female Voice


def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except RuntimeError as e:
        print("Speech engine is already running.")
