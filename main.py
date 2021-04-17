import engine
import webbrowser

def speak(audio):
    engine.speak(audio)


if __name__ == "__main__":
    engine.clr()
    engine.AskPass()
    engine.whish()
    while True:

       query = engine.listen().lower()

       if 'what is the time' in query:
          engine.CurrentTime()
       elif 'quit' in query:
           speak("ok sir ,thank you have a great day")
           exit()
       elif 'open youtube' in query:
           speak("ok")
           webbrowser.open("youtube.com")

       elif 'open facebook' in query:
           speak("ok")
           webbrowser.open("www.facebook.com")
       elif 'open MP3 quack' in query:
           speak("ok")
           webbrowser.open("www.mp3.com")

       elif "wait a minute" in query:
           import time
           speak("ok")
           print('-_-"')
           time.sleep(10)
           speak("have you done?")
           pass


