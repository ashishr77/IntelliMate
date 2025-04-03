from datetime import datetime
from speak import speak
from decouple import config


USER = config("USER")
HOSTNAME = config("BOT")

def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USER} sir")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good Afternoon {USER} sir")
    elif (hour >= 10) and (hour <= 19):
        speak(f"Good Evening {USER} sir")
    else:
        speak(f" Hello {USER} ")
    speak(f"I Am {HOSTNAME} , How May i assist you?")