from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from speak import speak
from take_command import take_command
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_youtube():
    speak("Opening YouTube")

    # Set up WebDriver with a new profile directory
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=C:/Users/ashis/AppData/Local/Google/Chrome/User Data/SeleniumProfile")
    path = "C:\\Program Files\\chromedriver-win64\\chromedriver.exe"  # Update path if needed

    try:
        driver = webdriver.Chrome(service=Service(path), options=chrome_options)

        # Open YouTube
        driver.get("https://www.youtube.com")

        # Wait for YouTube to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "search_query")))

        # Ask user for search query
        speak("What do you want to search, sir?")
        query = take_command().lower()

        if query:
            search_box = driver.find_element(By.NAME, "search_query")
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)

            speak(f"Searching {query} on YouTube")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "video-title")))  # Wait for results
        else:
            speak("No search query received.")

    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, I encountered an error.")