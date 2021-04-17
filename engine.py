import datetime
import pyttsx3
import speech_recognition as sr
import settings
import os
import connnection
import time
import random
'''this is the resource codes of vector'''


gender = settings.gender
voiceRate = settings.VoiceRate
name = settings.username

connnection.try_connection()

if 'true' in settings.clear_screen:
    def clr():
        if os.name == 'nt':
            os.system("cls")
            print("")
        else:
            os.system("clear")
            print("")
else:
    def clr():
         pass


'''this is the resource codes of vector'''
def AskPass():
   if "false" in settings.passwd:
       pass

   else:
       print("enter password below")
       password = settings.password
       enteredpass = input(">>>")
       if f"{password}" in enteredpass:
           pass
           clr()
       else:
           print("wrong")
           exit()

#<engine settings>
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
if "female" in gender:
    engine.setProperty('voice',voices[1].id)
elif "male" in gender:
    engine.setProperty('voice',voices[0].id)
else:
    print("ERROR:no such gender it can only be male, female. don't you know?")
    exit()

engine.setProperty('rate',voiceRate)
#<engine/>

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        if "" in name:
            print(f">>>{query}\n")
        else:
            print(f"{name}:{query}\n")
    except Exception:
        speak("sorry,didn't hear that")
        return "None"
    return query
if "false" in settings.hello_massage:
    def whish():
        pass
elif "true" in settings.hello_massage:
        def whish():
            hour=int(datetime.datetime.now().hour)
            if not 5 >= hour < 12:
                speak('good morning')
            else:
                speak("hello sir ")


else:
    print("ERROR:can't put '",settings.hello_massage,"' in hello_massage, it can only be true,false")
    exit()

def CurrentTime():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(f"the time is {time}")
    if "00" in time:
        speak("sir this is time , to sleep so please go to your bed")

def command(input,output):
    query=listen().lower()
    if f'{input}' in query:
        speak(output)

def conversation():
    def command(input,output):
        query=listen().lower()
        if f'{input}' in query:
            speak(output)

    command("how are you","i am good man")
    command("what are you doing","i am talking to you")
    command("tell me a story","a story")
    command("what is your name","my name is vector")
    command("what is your age","my age is , wait a sec i don't have any age")
    command("what is your purpose","my purpose is to help and talk with you")
    command("who is your best friend"," u ")
    command("sorry","it's ok")
    command("","")
