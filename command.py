import os
import webbrowser
import subprocess
from _datetime import datetime
from speak import speak


# Function to open command prompt
def open_command_prompt():
    speak("Opening command prompt")
    os.system("start cmd")


def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


# Function to open camera
def open_camera():
    speak("Opening camera")
    os.system("start microsoft.windows.camera:")


# Function to open YouTube
def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")


# Function to open Google
def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")


def open_task_manager():
    speak("Opening Task Manager")
    os.system("start Taskmgr.exe")


# Function to open ChatGPT
def open_chatgpt():
    speak("Opening ChatGPT")
    webbrowser.open("https://chat.openai.com")


# Function to open File Explorer
def open_file_explorer():
    speak("Opening File Explorer")
    os.system("explorer")


# Function to open Notepad
def open_notepad():
    speak("Opening Notepad")
    os.system("start notepad")


# Function to open Calculator
def open_calculator():
    speak("Opening Calculator")
    os.system("calc")


# Function to open PyCharm
def open_pycharm():
    speak("Opening PyCharm")
    os.system("start pycharm")


# Function to open Visual Studio Code
def open_vscode():
    speak("Opening Visual Studio Code")
    os.system("code")


# Function to open WhatsApp (Desktop version)


def open_whatsapp():
    speak("Opening WhatsApp")
    subprocess.Popen(["start", "whatsapp:"], shell=True)


# Function to open Microsoft Word
def open_word():
    speak("Opening Microsoft Word")
    os.system("start winword")


# Function to open Microsoft PowerPoint
def open_powerpoint():
    speak("Opening Microsoft PowerPoint")
    os.system("start powerpnt")


def close_application(app_name):
    try:
        if app_name == "command prompt":
            os.system("taskkill /f /im cmd.exe")
        elif app_name == "camera":
            os.system("taskkill /f /im WindowsCamera.exe")  # Adjust if necessary
        elif app_name == "notepad":
            os.system("taskkill /f /im notepad.exe")
        elif app_name == "file explorer":
            os.system("taskkill /f /im explorer.exe")
        elif app_name == "task manager":
            os.system("taskkill /f /im Taskmgr.exe")
        elif app_name == "calculator":
            os.system("taskkill /f /im CalculatorApp.exe")
        elif app_name == "pycharm":
            os.system("taskkill /f /im pycharm64.exe")  # Adjust if necessary
        elif app_name == "vscode":
            os.system("taskkill /f /im Code.exe")  # Adjust if necessary
        elif app_name == "whatsapp":
            os.system("taskkill /f /im WhatsApp.exe")
        elif app_name == "word":
            os.system("taskkill /f /im WINWORD.EXE")
        elif app_name == "powerpoint":
            os.system("taskkill /f /im POWERPNT.EXE")
        elif app_name == "browser":
            os.system("taskkill /f /im chrome.exe")  # Adjust for your browser
            os.system("taskkill /f /im firefox.exe")  # Add more if necessary

        print(f"{app_name.title()} has been closed.")
    except Exception as e:
        print(f"Failed to close {app_name}: {e}")
