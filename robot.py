# phần nghe
from ast import Str
from calendar import calendar, weekday
from pickle import TRUE
from datetime import date, datetime
import speech_recognition
import datetime
import time
from gtts import gTTS
import os
import pyttsx3 
import requests,_json 
thoi_gian = datetime.datetime.now()
thoigian = int(thoi_gian.strftime("%H"))
weekdays = (thoi_gian.strftime("%A"))
robot_ear = speech_recognition.Recognizer()
while True:
    with speech_recognition.Microphone() as mic:
        audio = robot_ear.record(mic, duration=3)
        robot_ear.adjust_for_ambient_noise(mic)
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio, language= 'vi-VN')
    except:
        you = ""
    print("You: " + you)

    # phần hiểu
    if you == "bây giờ đang là buổi nào trong ngày" :
        if 6 <=  thoigian <= 11 :
            robot_brain = "good morning sir "
        elif 00 <= thoigian <= 5:
            robot_brain = "It's still early in the morning, so you should sleep a little longer"
        elif 12 <= thoigian <= 14 :
            robot_brain = "Hi sir, now it's noon"
        elif 15<= thoigian <=18:
            robot_brain = "now is afternoon"
        elif 19<= thoigian <= 22:
            robot_brain = "good evening sir"
        elif thoigian >= 23 :
            robot_brain = "too late you need go to bed now"
    elif you == "Hôm nay là thứ mấy" :
        if weekdays == "Monday":
            robot_brain = "Today is Monday"
        elif weekdays == "Tuesday":
            robot_brain = "Today is Tuesday"
        elif weekdays == "Wednesday":
            robot_brain = "Today is Wednesday"
        elif weekdays == "Thursday":
            robot_brain = "Today is Thursday"
        elif weekdays == "Friday":
            robot_brain = "Today is Friday"
        elif weekdays == "Saturday":
            robot_brain = "Today is Saturday"
        elif weekdays == "Sunday":
            robot_brain = "Today is Sunday"
    elif you == "mấy giờ":
        robot_brain = thoi_gian.strftime("%H")
    elif "bye" in you :
        robot_brain = "BYE SIR"
        print("Robot: "+ robot_brain)
        robot_mouth = pyttsx3.init()
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else: 
        robot_brain = "say something bro.."

    print(robot_brain)

    # phần nói (if you want speak Vietnamese)
    #tts = gTTS(text=robot_brain,lang='vi') 
    #tts.save("pcvoice.mp3")
    #os.system("start pcvoice.mp3")

    #(SPEAK ENGLISH)
    # robot_mouth = pyttsx3.init()
    # robot_mouth.say(robot_brain)
    # robot_mouth.runAndWait()




