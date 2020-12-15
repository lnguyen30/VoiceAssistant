# VoiceAssistant
speech recognition program built will be able to recognize these commands:
name - tells its name.
date - tells the date.
time - tells the current time.
how are you? - will say "I am fine...".
search - will search using Google.
and finally, if we say "quit" or "exit", it will terminate.

3 modules needed:
SpeechRecognition - to recognize our speech and to convert it into text format using Google's Web Speech API.
PyAudio - for accessing and working with the Microphone.
pyttsx3 - for converting given text to speech(ie for generating computer voice)

first install pipwin then pyaudio, then pyttsx3 to talk
knowing the current date and time, we need that datetime module.
to open up a browser and do a google search, need the webbrowser module
pyttsx3 will be responsible for generating the computer voice. 

recognize_voice() listens to our Microphone, converts it to text with recognize_google()
