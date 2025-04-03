import webbrowser
import pyautogui
import requests
import pywhatkit
import wikipedia
from speak import speak
from email.message import EmailMessage
import smtplib
from sympy import sympify
import time
from take_command import take_command


def my_ip():
    ip = requests.get("https://api.ipify.org?format=json").json()
    return ip


def search_on_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result

    except Exception as e:
        speak("Sorry Sir, Data No Found , Please Try again")


def search_on_google(query):
    pywhatkit.search(query)


def youtube(video):
    if video == "none":
        webbrowser.open("https://www.youtube.com/")
    else:
        pywhatkit.playonyt(video)


EMAIL = ""
PASSKEY = ""


def send_mail(reciever_mail, subject, message):
    try:
        email = EmailMessage()
        email["To"] = reciever_mail
        email["Subject"] = subject
        email["From"] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSKEY)
        s.send_message(email)
        s.close()
        return True

    except Exception as e:
        print("ERROR : ", e)
        speak("Unable To send mail")
        return False


def get_news():
    news = []
    api_key = "ccc58649110ac72d1ab2f7da9f481624"  # Replace with your GNews API key
    url = f"https://gnews.io/api/v4/search?q=India&token={api_key}"

    response = requests.get(url)
    data = response.json()

    if data['totalArticles'] > 0:
        news_articles = data['articles']
        for article in news_articles:
            news.append(article['title'])
    else:
        print("No news articles found.")

    return news[:6]


def calculate_expression(expr):
    try:
        # Convert the string expression to a SymPy expression
        result = sympify(expr)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

# def search_on_youtube():
#     speak("Opening YouTube")
#     webbrowser.open("https://www.youtube.com")
#     time.sleep(5)  # Wait for the browser to load
#
#     speak("What do you want to search, sir?")
#     query = take_command().lower()
#
#     if query:
#         pyautogui.moveTo(800, 220)  # Adjust the coordinates based on screen size
#         pyautogui.click()
#         pyautogui.write(query, interval=0.1)
#         pyautogui.press("enter")
#         speak(f"Searching {query} on YouTube")
#     else:
#         speak("No search query received.")