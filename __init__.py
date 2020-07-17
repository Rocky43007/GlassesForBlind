import time
import os
import sys
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import pickle
import datefinder

r = sr.Recognizer()

if os.path.isfile('birthday.native') == True:
    os.system("python GFBDetect.py --conf config/config.json")

if os.path.isfile('birthday.native') == False:
    def talkToMe(audio):
        print(audio)
        tts = gTTS(text=audio, lang='en')
        tts.save('audio.mp3')
        os.system('mpg123 audio.mp3')

    def myCommand():
        Welcome = 'Welcome! Please say your date of birth.'
        talkToMe(Welcome)

        with sr.Microphone() as source:
            print('Ready')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            command = r.recognize_google(audio)
            print("Your birthday is on the " + command)
            matches = datefinder.find_dates(command)

            for match in matches:
                print (match)

        pickle_out = open("birthday.native","wb")
        pickle.dump(str(match), pickle_out)
        pickle_out.close()

        
        try:
            pass
        except sr.UnknownValueError:
            talkToMe('Sorry, I did not understand. Please repeat.')
            myCommand()
        return command
    
    myCommand()
    os.system('python GFBDetect.py --conf config/config.json')

