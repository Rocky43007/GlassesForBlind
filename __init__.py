#Copyright Arnab Chakraborty 2020.
#Created by Arnab Chakraborty.
#----------------------------------------
#Used to allow code to measure time.
import time
#Allows code to use command line.
import os
#Same as os.
import sys
#Module which helps code recognise speech as seen in Mycommand.
import speech_recognition as sr
#Uses an API from Google to allow playing text as speech.
from gtts import gTTS
#Used to make sure audio works properly.
import pyaudio
#Used to save any data as a file.
import pickle
#Used to find dates from text.
import datefinder

#Set up speech recognition software.
r = sr.Recognizer()

#If statements checking if Date of Birth File exists or not.
if os.path.isfile('birthday.native') == True:
    os.system("python GFBDetect.py --conf config/config.json")
#If file does not exist, ask for Date of Birth.
if os.path.isfile('birthday.native') == False:
    #Define audio output for Google Text To Speech to give instructions to user.
    def talkToMe(audio):
        print(audio)
        tts = gTTS(text=audio, lang='en')
        tts.save('audio.mp3')
        #os.system used to run mpg123 as to get audio running from command line.
        os.system('mpg123 audio.mp3')

    #Asks for Date of Birth using Speech Recognistion.
    def myCommand():
        Welcome = 'Welcome! Please say your date of birth.'
        #Uses the Audio output setup to make text to speech easier.
        talkToMe(Welcome)

        #Defines microphone and starts microphone to listen for text.
        with sr.Microphone() as source:
            print('Ready')
            #Pauses to wait for speech.
            r.pause_threshold = 1
            #Waits and listens of ambient noise to remove from speech.
            r.adjust_for_ambient_noise(source, duration=1)
            #Uses Microphone to listen for speech.
            audio = r.listen(source)
            #Uses Google Speech Recognition API to understand speech.
            command = r.recognize_google(audio, language="en-EN")
            #Prints out when the user's birthday is - Used for checking if any errors occur.
            print("Your birthday is on the %s" %command)
            #Uses Date Finder to find dates from the Speech which was saved as text.
            matches = datefinder.find_dates(command)

            for match in matches:
                print (match)
        #Uses Pickle to save Date of Birth as File, which means that user has to never put in date of birth again.
        pickle_out = open("birthday.native","wb")
        pickle.dump(str(match), pickle_out)
        pickle_out.close()

        
        try:
            pass
        #Used only when Microphone is not picked up by code or machine.
        except sr.UnknownValueError:
            talkToMe('Sorry, I did not understand. Please repeat.')
            myCommand()
        return command
    #Runs the speech recogition code as shown above.
    myCommand()
    #Runs Object and Step/Distance Detection via command line.
    os.system('python GFBDetect.py --conf config/config.json')

