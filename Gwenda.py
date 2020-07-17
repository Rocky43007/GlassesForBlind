#Made by Arnab Chakraborty
from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib



def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')


def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        command = r.recognize_google(audio, language = 'en')
        print("Gwenda thinks you said " + command)
        
    try:
        pass
    except sr.UnknownValueError:
        talkToMe('Sorry, I did not understand. Please repeat.')
        assistant(myCommand())


    return command


def assistant(command):
    if 'open reddit' in command:
        firefox_path = '/usr/bin/firefox'
        url = 'https://www.reddit.com'
        webbrowser.get(firefox_path).open(url) 
        
        
    elif 'test' in command:
        print('testing')
        agefile = '20'
        pickle_out = open("age.native","wb")
        pickle.dump(agefile, pickle_out)
        pickle_out.close()


    elif 'bye' in command:
        talkToMe('Bye')
        exit()

    elif 'Google' in command:
        talkToMe('Please repeat what you would like to search')
        query = myCommand()

myCommand()
