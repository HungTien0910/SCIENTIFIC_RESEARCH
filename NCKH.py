from datetime import date, datetime
import speech_recognition
import datetime
import time
from gtts import gTTS
import os
import pyttsx3 
robot_ear = speech_recognition.Recognizer()
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: Đang nghe.....")
        audio = robot_ear.listen(mic, phrase_time_limit=2)
        # audio = robot_ear.record(mic, duration = 5)
        robot_ear.adjust_for_ambient_noise(mic, duration = 5)
    try:
        you = robot_ear.recognize_google(audio, language= 'vi-VN', show_all=False)
    except:
        you = ""
    print("Có Phải bạn nói: " + you)
    if "tạm biệt" in you :
        robot_brain = "chào tạm biệt"
        print("Robot: "+ robot_brain)
        robot_mouth = pyttsx3.init()
        # robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif you == "": 
        robot_brain = "Tôi chưa nghe thấy bạn nói gì..."
        print("Robot: "+ robot_brain)
print(robot_brain)