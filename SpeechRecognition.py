# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Creator: Gary
Create Date: 2020 Nov 14
Update Date: 2022 Jul 15
Function: Virtual Assistance Voice
"""

import datetime
import pyttsx3
import speech_recognition as sr

def speak(audio):
   engine.say(audio) 
   engine.runAndWait() #Without this command, speech will not be audible to us..

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("Welcome! Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as e:
        # print(e)  use only if you want to print the error!
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #getting details of the current voice
engine.setProperty('voice', voices[1].id)

if __name__=="__main__" :
    wishMe()
    while True:
        query = takeCommand().lower() #Converting user query into lower case
    
    
