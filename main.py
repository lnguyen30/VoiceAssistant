# imports for program
import speech_recognition as sr
from time import sleep
from datetime import datetime
import webbrowser
import pyttsx3

# make instance of Recognizer class
r = sr.Recognizer()

# confs for pyttsx3
engine = pyttsx3.init()


# function to recognize voice and return text version of speech
def recongize_voice():
    text = ''

    # create instance of Microphone class
    with sr.Microphone() as source:
        # adjust for ambient noise
        r.adjust_for_ambient_noise(source)

        # capture voice
        voice = r.listen(source)

        # recognition check
        try:
            text = r.recognize_google(voice)
        except sr.RequestError:
            speak("Sorry, I can't access Google API...")
        except sr.UnknownValueError:
            speak("Unable to recognize speech")
        return text.lower()


def reply(text_version):
    # name
    if "name" in text_version:
        speak("My name is cheeks")

    # how are you?
    if "how are you" in text_version:
        speak("I am fine")

    # date
    if "date" in text_version:
        # get today's date and format it
        date = datetime.now().strftime("%d %b %Y")
        speak(date)

    # time
    if "time" in text_version:
        # get current time and format it
        time = datetime.now().time().strftime("%H %M")
        speak("Time is " + time)

    # search google
    if "search" in text_version:
        speak("What would you like to search?")
        keyword = recongize_voice()

        # if keyword is not empty
        if keyword != '':
            url = "https://google.com/search?q=" + keyword

            # webbrowser module to work with web browser
            speak("Here are the search results for " + keyword)
            webbrowser.open(url)
            sleep(3)

    if "quit" in text_version or "exit" in text_version:
        speak("shutting down")
        exit()


# changing from text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()


# wait a second for adjust_for_ambient_noise() to work
sleep(1)

while True:
    speak("start speaking")
    # listen for voice and convert it into text format
    text_version = recongize_voice()

    # give "text_version" to reply function
    reply(text_version)
