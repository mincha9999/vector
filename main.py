import os
import datetime
import random
import time
import urllib.request
import requests
import re
import operator
import platform
import psutil

try:
    import colorama
    import pyttsx3
    import pyaudio
    import wave
    import signal
    import speech_recognition as sr
    import webbrowser
    import wikipedia
    from  AppOpener import open, close
    import pytube
    from newsapi import NewsApiClient
    import cv2
    from bs4 import BeautifulSoup
    import pyaudio
    import io
    from googletrans import Translator

except:
    print("required packages missing. starting inistallation")
    os.system("pip install colorama speechRecognition pytube pyttsx3 ffmpeg wave pydub pyaudio wikipedia AppOpener newsapi-python opencv-python beautifulsoup4 googletrans==4.0.0-rc1")
    try:
        import colorama
        import pyttsx3
        import pyaudio
        import wave
        import signal
        import speech_recognition as sr
        import webbrowser
        import wikipedia
        from  AppOpener import open, close
        import pytube
        from newsapi import NewsApiClient
        import cv2
        from bs4 import BeautifulSoup
        import pyaudio
        import io
        from googletrans import Translator
    except:
        print("iNSTALLATION ABROAD")
        exit()

print(colorama.Fore.LIGHTGREEN_EX+ "Loading VECTOR..." + colorama.Fore.RESET)
try:
    urllib.request.urlopen('https://www.google.com')
    pass
except:
    print("No Internet")
    exit()

'''variable'''
strTime = datetime.datetime.now().strftime("%I:%M %p")
'''Weather Api and Web setting'''
url = "https://weather.com/en-IN/weather/today/l/7e2c2ba73c7c434f4d58ab05148e6f1b593ba9f39b3378ba861a9d59a3f2b044"
response = requests.get(url)
strTime = datetime.datetime.now().strftime("%I:%M %p")
soup = BeautifulSoup(response.content, "html.parser")
News_Api_Key = "4bd297e7f79543458e07928546fdabd8"
'''initialize the pyttsx3 engine'''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

'''functions to be used'''
def speak(audio):
    print(colorama.Fore.LIGHTGREEN_EX + "Vector:" + colorama.Fore.RESET,audio)
    engine.say(audio)
    engine.runAndWait()

def NewsFromBBC():
	query_params ={
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": News_Api_Key
	}
	main_url = " https://newsapi.org/v1/articles"
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()
	article = open_bbc_page["articles"]
	results = []
	for ar in article:
		results.append(ar["title"])
	for i in range(len(results)):
		print(i + 1, results[i])

def solve_math_question(question):
    match = re.match(r'what is (\d+) ([+\-*/x]|into) (\d+)', question)
    if match:
        num1 = int(match.group(1))
        operator_str = match.group(2)
        num2 = int(match.group(3))
        # Performing the calculation
        operators = {'+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    'into': operator.mul,
                    'X':operator.mul,
                    '/': operator.truediv         
                    }
        
        print("test:",num1,num2,str(operator_str))
        try:
            result = operators[operator_str](num1, num2)
            return f"The result of {question} is:{result}"
        except:
            return f"Sorry,cannot solve the equation"

def  greet():
    current_time = int(datetime.datetime.now().hour)
    if 0 <= current_time < 3:
        speak("Hello, It's quite late now, but I'm here and ready to assist you. How can I help you today?")  # Set(1)
    elif 3 <= current_time < 6:
        speak("Good morning! It's early, but I'm here and ready to assist you")  # Set(2)
    elif 6 <= current_time < 12:
        speak("Morning vibes! What can I do to kickstart your day?")  # Set(3)
    elif 12 <= current_time < 17:
        speak("Good afternoon! How may I assist you?")  # Set(4)
    elif 17 <= current_time < 24:
        speak("Good evening! The stars are out, and so am I. How can I assist you tonight?")  # Set(5)

def search_google_scholar(query):
    base_url = "https://scholar.google.com/scholar"
    params = {"q": query}
    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    for result in soup.find_all('h3', {'class': 'gs_rt'}):
        title = result.a.text
        link = result.a['href']
        print(f"Title: {title}\n Link: {link}\n")

def roll_a_dice():
    sides_of_dice = [1,2,3,4,5,6]
    rolled_dice_side = random.choice(sides_of_dice)
    speak("here you go")
    if rolled_dice_side == 1:
        print("your pip is ", rolled_dice_side)
        print(
            " +-------+\n"
            " |       |\n"
            " |   ●   |\n"
            " |       |\n"
            " +-------+\n"
        )
    elif rolled_dice_side == 5:
        print("your pip is ", rolled_dice_side)
        print(
            " +-------+\n"
            " | ●   ● |\n"
            " |   ●   |\n"
            " | ●   ● |\n"
            " +-------+\n"
        )
    elif rolled_dice_side == 3:
        print("your pip is ", rolled_dice_side)
        print(
            " +-------+\n"
            " | ●     |\n"
            " |   ●   |\n"
            " |     ● |\n"
            " +-------+\n"
        )
    elif rolled_dice_side == 4:
        print("your pip is ", rolled_dice_side)
        print(
            " +-------+\n"
            " | ●   ● |\n"
            " |       |\n"
            " | ●   ● |\n"
            " +-------+\n"
        )
    elif rolled_dice_side == 2:
        print("your pip is ", rolled_dice_side)
        print(
            "  +-------+\n"
            "  |  ●    |\n"
            "  |       |\n"
            "  |     ● |\n"
            "  +-------+\n"
        )
    elif rolled_dice_side == 6:
        print("your pip is ", rolled_dice_side)
        print(
            "  +--------+\n"
            "  |  ●  ●  |\n"
            "  |  ●  ●  |\n"
            "  |  ●  ●  |\n"
            "  +--------+\n"
        )

def headlines(country=None, category='general', num_articles=5):
    from newsapi.newsapi_client import NewsApiClient
    newsapi = NewsApiClient(api_key=News_Api_Key)
    try:
        if country:
            headlines = newsapi.get_top_headlines(country=country, category=category, page_size=num_articles)
        else:
            headlines = newsapi.get_top_headlines(category=category, page_size=num_articles)
        print(f"\nTop {num_articles} headlines in the {category} category")
        if country:
            print(f"for {country.upper()}:\n")
        else:
            print("globally:\n")
        for i, article in enumerate(headlines['articles']):
            speak(f"{i + 1}) {article['title']}")
            print("link:",article['url'])
            
    except Exception as e:
        print(f"An error occurred: {e}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print(colorama.Fore.LIGHTYELLOW_EX + "Listening..." + colorama.Fore.RESET )
            r.pause_threshold = 1
            audio = r.listen(source)
        except:
            print(colorama.Fore.LIGHTRED_EX + "Program Exited..."+ colorama.Fore.LIGHTRED_EX)
            exit()

    try:
        print(colorama.Fore.CYAN + "Sanctioning..." + colorama.Fore.RESET)
        query = r.recognize_google(audio, language='en-in')
        print(colorama.Fore.MAGENTA + "User:"+ colorama.Fore.RESET +f" {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...")
        return "None"
    return query
    
def capture_picture(camera_index=0, output_file=f'{random.randint(000000,99999)}_vector_click.jpg'):
    
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        speak("Sorry can't access the camera.")
        return
    ret, frame = cap.read()
    if not ret:
        speak("sorry there")
        return
    cv2.imwrite(output_file, frame)
    cap.release()
    speak(f"Picture captured and saved as {output_file}")

def get_random_joke():
        JOKEapi_url = "https://v2.jokeapi.dev/joke/Any"
        try:
            response = requests.get(JOKEapi_url)
            response.raise_for_status() 
            joke_data = response.json()
            if joke_data['type'] == 'single':
                speak(joke_data['joke'])
                
            elif joke_data['type'] == 'twopart':
                speak(joke_data['setup'])
                speak(f"{joke_data['delivery']}")
            else:
                speak("Invalid joke format from API.")
        except requests.exceptions.RequestException as e:
            return f"Error fetching joke: {e}"

def translate_text(user_input):
    translator = Translator()

    # Extract text and target language using regular expressions
    match = re.search(r'translate (.+) in (.+)', user_input, re.IGNORECASE)
    
    if match:
        text_to_translate = match.group(1).strip()
        language_code = match.group(2).strip()

        # Perform translation
        translation = translator.translate(text_to_translate, dest=language_code)
        
        speak(f"Translated text in {language_code}: {translation.text}")
    else:
        speak("Invalid input format. Please enter in the format 'What is (text) in (language)'.")

def get_recipe(dish_name):
    base_url = "https://api.spoonacular.com/recipes/search"
       # Replace with your actual API key
    
    params = {
        "query": dish_name,
        "number": 1,
        "apiKey": '04911c87d1f04ccca66f7e20215b34d5',
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if any recipes were found
        if data['totalResults'] > 0:
            # Get the first recipe's ID
            recipe_id = data['results'][0]['id']

            # Make a new request to get the detailed information for the recipe
            recipe_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
            params = {"apiKey": '04911c87d1f04ccca66f7e20215b34d5'}
            recipe_response = requests.get(recipe_url, params=params)

            # Check if the detailed request was successful
            if recipe_response.status_code == 200:
                recipe_data = recipe_response.json()
                print(f"Ingredients for {dish_name}:")
                for ingredient in recipe_data['extendedIngredients']:
                    print(f"- {ingredient['original']}")

                # Print the steps
                print(f"\nSteps to cook {dish_name}:")
                for i, step in enumerate(recipe_data['analyzedInstructions'][0]['steps'], start=1):
                    print(f"{i}. {step['step']}")

            else:
                print(f"Error fetching recipe details: {recipe_response.status_code}")
        else:
            print(f"No recipes found for {dish_name}")
    else:
        print(f"Error searching for recipes: {response.status_code}")
    
if __name__ == "__main__":
    os.system("cls")
    greet()
    while True:
        #DEBUGGING PURPOSE/TEST PURPOSE/INTERACTIVE MODE
        debug_mode = False #True for command prompt

        if debug_mode:
            reply = input(">")
        else:
            reply = takeCommand()

        reply = reply.replace("Vector","")
        reply = reply.replace("vector","")

        if ("what's the time" in reply or "what is the time" in reply):                  # TIME INFO
            speak(f"the time is {strTime}")

        elif "Indian National Anthem" in reply:
            speak("playing The Indian national anthem...")
            os.system("NATION.mp3.m4a")

        elif "translate " in reply:
            lowered_query = reply.lower
            translate_text(lowered_query)
        
        elif ("what is today's date" or "what's today's date") in reply:
            formatted_date = datetime.datetime.now().strftime("%d/%m/%y")
            speak(f"Today is {formatted_date}")

        elif ('Wikipedia' or "tell me about")in reply:
            random_list_set = random.choice(['Searching answeres...',
                                             "Searching for upshots...",
                                             "Searching for out-turns...",
                                             "Serching for results..."
                                            ])
            speak(random_list_set)
            reply = reply.replace("Wikipedia","")
            reply = reply.replace("tell me about","")
            try:
                results = wikipedia.summary(reply, sentences=2) 
                speak("According to Wikipedia")
                speak(results)
            except:
                speak("Sorry I am having trouble finding the results")

        elif ('quit'or'exit'or'bye'or'tata') in reply:
           speak("Thank you have a great day")
           exit()

        elif 'open YouTube' in reply:
           speak("okey")
           webbrowser.open("youtube.com")
        elif 'open Facebook' in reply:
           speak("okey")
           webbrowser.open("facebook.com")
        elif 'open browser' in reply:
            speak("okey")
            webbrowser.open("www.google.com")

        elif "wait a minute" in reply:
           speak("okey")
           print('-_-"')
           time.sleep(10)
           speak("have you done?")
           time.sleep(5)
           speak("there we go...")

        elif "can you sing" in reply:
            speak("not really, am not a great singer")           

        elif "when were you born"in reply:
           speak("i was made not born")

        elif "where were you born" in reply:
           speak("i was made not born")
           
        elif "who made you" in reply:
            speak("I was made by my enginners, namely Debanjan , Ankana , Jagyasani, Meghna and Mriganka.")

        elif ("what's your name" or "what is your name" or "who are you")  in reply:
            speak("my name is Vector")

        elif ("what is your purpose"or"what's your purpose"or"why do you exist") in reply:
            speak("to try my best to make your life easier and more convinient by providing hands free acces to information and services")

        elif "can you tell" in reply:
            reply = reply.replace("can you tell","")
            reply = reply.replace("me","")
            reply = reply.replace("vector","")
            speak("sorry, but i havent learned it yet.")

        elif "who gave your voice" in reply:
            speak("I am voiced by pyttsx3 engine and powered by sapi5")

        elif ("what's your favourite" or "what is your favourite")in reply:
            speak("being a programmed personal assistant,I have no personal preference.")

        elif "how do you work" in reply:
            speak("I use internet and various API's of popular websites and and your some baisic Python libraries to render the outputs.")

        elif "credits" in reply:            #CREDITS
            print("==========", colorama.Fore.MAGENTA + "CREDITS" + colorama.Fore.RESET, "=========")
            print("Scrpting: Ankana,Jagyasani".center(50))
            print ("Dialouges: Ankana,Meghna".center(50))
            print("Designing: Jagyasani,Meghna".center(50))
            print("Programming/Coding: Debanjan".center(50))
            print("Contribution: Jagyasani,Ankana,Debanjan,Mriganka,Meghna".center(50))
            print("Coordination: Debanjan".center(50))
            print("Management: Ankana,Mriganka".center(50))
            print("=======================================")

        elif "roll a dice" in reply:                            #ROLL A DICE
            roll_a_dice()

        elif "article" in reply:                               #ARTICLE
            reply = reply.replace("article","")
            speak("here is what i found")
            search_google_scholar(reply)

        elif 'what is' in reply and any(op in reply for op in ['+', '-', 'x', '/','into']):     #
            math_result = solve_math_question(reply)
            speak(math_result)
        
        elif 'what is the temperature' in reply:
            speak("Grabbing the information from the web")
            if response.status_code == 200:
                temperature_span = soup.find("span", {"data-testid": "TemperatureValue"})
                temperature_value = temperature_span.get_text()
                speak(f"the temparature is {temperature_value}")
            else:
                speak("Sorry, i am having problem to access the web")

        elif 'what is the humidity' in reply:
            speak("Grabbing the information from the web")
            if response.status_code == 200:
                percentage_span = soup.find("span", {"data-testid": "PercentageValue"})
                percentage_value = percentage_span.get_text()
                speak(f"Current Humidity is {percentage_value}")
            else:
                speak("Sorry, I am having problem to access the web")
        
        elif 'what is the wind speed' in reply:
            speak("Grabbing the information from the web")
            if response.status_code == 200:
                wind_span = soup.find("span", {"data-testid": "Wind"})
                wind_speed = wind_span.find_all("span")[1].get_text(strip=True)
                speak(f"the wind speed is {wind_speed} Km/h")
            else:
                speak("Sorry, i am having problem to access the web")
        
        elif 'what is the weather' in reply:                    #WEATHER
            speak("Grabbing the information from the web")
            if response.status_code == 200:
                wx_phrase_div = soup.find("div", {"data-testid": "wxPhrase"})
                wx_phrase = wx_phrase_div.get_text(strip=True)
                if wx_phrase == "Clear":
                    speak(f"The current weather is {wx_phrase}")
                else:
                    speak(f"The current weather is {wx_phrase}y")

        elif "flip a coin" in reply:             #flip a computer
            b = [1,2]
            side_of_coin = random.choice(b)
            if b == 1:
                print("⏫")
                speak("Its HEAD")
            else:
                print("⏬")
                speak("Its TAILS")

        elif ("open" or "start") in reply:               #start programs
            reply = reply.replace("open","")
            try:
                speak(f"ok opening {reply}")
                open(reply,match_closest=True)
            except:
                speak(f"cannot open {reply}")
                
        elif "close" in reply:
            try:
                reply = reply.replace("close","")
                speak(f"ok closing {reply}")
                close(reply,match_closest=True)
            except:
                speak(f"cannot closing {reply}")
        
        elif "None" in reply:
            pass

        elif 'Top 10 news' in reply:                      # Top 10 news
            speak("Here are the top 10 global news")
            NewsFromBBC()

        elif 'headlines' in reply:                         #headlines
            reply = reply.replace("headlines","")
            if "Global" in reply:
                headlines(country=None)
            elif'India'in reply:
                headlines(country='in')
            elif'USA' in reply:
                headlines(country='us')
            elif'French' in reply:
                headlines(country='fr')
            elif'Japan' in reply:
                headlines(country='jp')

        elif 'specs' in reply:                               #SPECS
            speak("Here are the specs of the device:-")
            speak(f"Computer name: {platform.node()}")
            speak(f"Machine type: {platform.machine()}")
            speak(f"Processor type: {platform.processor()}")
            speak(f"Operating system + virsion: {platform.system()} {platform.release()}")
            speak(f"Number of physical cores: {psutil.cpu_count(logical=False)}")
            speak(f"Max CPU frequency: {psutil.cpu_freq().max}Hz")
            speak(f"Total RAM: {round(psutil.virtual_memory().total/1000000000, 2)} GB")

        elif 'click a' in reply:             #SELFIE
            speak("clicking a picture in")
            speak('3')
            speak('2')
            speak('1')
            speak("stay steady...")
            capture_picture()

        elif 'tell me a joke' in reply:          #JOKE 
            get_random_joke()

        elif ('receipe of' or "receipe for") in reply:
            dish_name = reply.replace(("receipe of"and"receipe for"),"")
            print(dish_name)
            if dish_name == "None":
                pass
            else:
               speak(get_recipe(dish_name))
                
        elif 'download a Youtube video' in reply:
            video_url = input(colorama.Fore.LIGHTWHITE_EX + "Paste " + colorama.Fore.RED + "You"+colorama.Fore.WHITE+"Tube Link:")
            yt = pytube.YouTube(video_url)
            video_stream = yt.streams.get_highest_resolution()
            print(colorama.Fore.GREEN + "Video Downloaded..." +colorama.Fore.RESET)
            file_name = input("Save file as:")
            video_stream.download(file_name)
            print(colorama.Fore.GREEN+"File saved as",file_name,".mp4"+colorama.Fore.RESET)

        else:
            speak("sorry i can't answer that")
