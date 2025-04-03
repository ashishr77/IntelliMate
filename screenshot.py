import pyautogui
import speech_recognition as sr
import os
from speak import speak
from pathlib import Path

# Function to take a screenshot
def take_screenshot():
    speak("What do you want to name the screenshot? Please say it now.")

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for screenshot name...")
        recognizer.adjust_for_ambient_noise(source)  # Optional: adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        # Recognize the speech and convert it to text
        screenshot_name = recognizer.recognize_google(audio)
        # screenshot_path = f"{screenshot_name}.png"
        downloads_path = str(Path.home() / "Downloads")
        screenshot_path = os.path.join(downloads_path, f"{screenshot_name}.png")

        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        speak(f"Screenshot taken and saved as {screenshot_name} in downloads folder")
        print(f"Screenshot saved as: {screenshot_path}")
    except sr.UnknownValueError:
        speak("Sorry, I could not understand what you said. Please try again.")
    except sr.RequestError:
        speak("Sorry, I am having trouble with the speech recognition service.")
