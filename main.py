# myenv\Scripts\activate
#  python -m venv myenv - to install

import ctypes
from decouple import config
from conv import how_are_you, jarvis
from random import choice
import keyboard
from greet_me import greet_me
from speak import speak
from screenshot import take_screenshot
from take_command import take_command
from command import (open_command_prompt, open_camera, open_chatgpt, open_file_explorer,
                     open_notepad, open_calculator, open_pycharm, open_vscode, open_whatsapp,
                     open_word, open_powerpoint, close_application, open_task_manager, get_current_time)
from online_data import (my_ip, youtube, search_on_google, search_on_wikipedia, send_mail, get_news,
                         calculate_expression)
from search_youtube import search_youtube
USER = config("USER")
HOSTNAME = config("BOT")

listening = True


def start_listening():
    global listening
    listening = True
    print("started Listening...")
    speak("I am listening now, sir")


def pause_listening():
    global listening
    listening = False
    print("Stopped Listening...")


keyboard.add_hotkey("ctrl+alt+z", start_listening)
# keyboard.add_hotkey("ctrl+alt+p", pause_listening)

if __name__ == "__main__":
    greet_me()
    while True:
        if listening:
            query1 = take_command().lower()
            if "how are you" in query1:
                print(query1)
                speak(choice(how_are_you))
            elif "wait" in query1:
                pause_listening()
            elif "open command prompt" in query1:
                open_command_prompt()
            elif "thanks" in query1:
                speak("Your welcome sir")
            elif "open camera" in query1:
                open_camera()
            elif "open youtube" in query1:
                speak("what do you want to see on youtube?")
                video = take_command().lower()
                youtube(video)

            elif "open google" in query1:
                speak("what do you want to search on google?")
                query = take_command().lower()
                search_on_google(query)

            # Chatgpt Opening
            elif "open chatgpt" in query1 or "open chat gpt" in query1:
                open_chatgpt()

            elif "open file explorer" in query1:
                open_file_explorer()

            elif "close file explorer" in query1:
                close_application("file explorer")

            elif "open notepad" in query1:
                open_notepad()

            elif "open calculator" in query1:
                open_calculator()

            elif "open pycharm" in query1:
                open_pycharm()

            elif "open vs code" in query1:
                open_vscode()

            elif "open whatsapp" in query1:
                open_whatsapp()

            elif "open word" in query1:
                open_word()

            elif "open powerpoint" in query1:
                open_powerpoint()

            # Taking ScreenShot
            elif "take a screenshot" in query1:
                take_screenshot()
            elif "close command prompt" in query1:
                close_application("command prompt")
            elif "close camera" in query1:
                close_application("camera")
            elif "close notepad" in query1:
                close_application("notepad")
            elif "close calculator" in query1:
                close_application("calculator")
            elif "close pycharm" in query1:
                close_application("pycharm")
            elif "close vs code" in query1:
                close_application("vscode")
            elif "close whatsapp" in query1:
                close_application("whatsapp")
            elif "close word" in query1:
                close_application("word")
            elif "close powerpoint" in query1:
                close_application("powerpoint")
            elif "close task manager" in query1:
                if ctypes.windll.shell32.IsUserAnAdmin():
                    close_application("Taskmgr")
                else:
                    speak("Please run the script as an administrator to close Task Manager.")
            elif "close browser" in query1:
                close_application("browser")
            #  Calling JArvis
            elif "jarvis " in query1:
                speak(choice(jarvis))
            elif "open task manager" in query1:
                open_task_manager()
            elif "abilities" in query1:
                speak(
                    "I can help you with tasks like opening and closing apps, mathematical calculation,  taking screenshots, and answering "
                    "questions!")

            elif "my ip" in query1:
                ip = my_ip()
                print("Your IP Address : ", ip)
                speak("Here is you IP address")

            elif "wikipedia" in query1:
                speak("what do you want to know on wikipedia?")
                print("what do you want to know on wikipedia?")
                query = take_command().lower()
                results = search_on_wikipedia(query)
                speak(f"According to Wikipedia {results}")
                print(results)

            elif "send an email" in query1:
                speak("Whom do you want to send the mail to? enter in terminal")
                receiver_mail = input("Email Address : ")
                speak("What should be the subject sir?")
                subject = take_command().capitalize()
                speak("What should be the message , sir?")
                message = take_command().capitalize()
                if send_mail(receiver_mail, subject, message):
                    speak("I have sent the email, sir")
                    print("message sent.")
                else:
                    speak("Sorry sir, but you have not set your mail ID and PAssword")
                    print("Sorry sir, message could not sent")


            elif "love" in query1:
                speak("I Love You too, sir")

            elif "news" in query1:
                headlines = get_news()
                if headlines:
                    print(headlines)
                    speak(f"So here are the latest news headlines, sir: {', '.join(headlines)}")
                else:
                    speak("Sorry sir, I couldn't fetch the news at the moment.")
            elif "calculation" in query1 or "math" in query1:
                while True:
                    speak("What kind of calculation do you want to do?")
                    query2 = take_command().lower()  # User provides the math expression

                    result = calculate_expression(query2)
                    speak(f"The result of your calculation is {result}")
                    print(f"The result of your calculation is {result}")

                    # Ask if the user wants to perform another calculation
                    speak("Do you want to perform another calculation? Say yes or no.")
                    response = take_command().lower()

                    if "no" in response:
                        speak("Okay, I will be here if you need anything else.")
                        break
                    elif "yes" not in response:
                        speak("I didn't catch that. Let's continue.")
            elif "time" in query1:
                speak(get_current_time())

            elif "search on youtube" in query1:
                search_youtube()
