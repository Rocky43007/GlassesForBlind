from gtts import gTTS
import os

mytext = 'Hi, Testing 123. This is a message created using Google Text To Speech.'

language = 'en'

output = gTTS(text=mytext, lang='en', slow=False)

output.save('output.mp3')

os.system('mpg123 output.mp3')
