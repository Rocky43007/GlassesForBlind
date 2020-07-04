#import pip
#import __Installer__.py
import GFBDistance as d
import GFBDetection as d2
import time
import os
import sys

def pipinstall():
    try:
        check_call(['sudo','apt-get', 'install', '-y', 'python3-pip'], stdout=open(os.devnull,'wb'))
    except CalledProcessError as e:
        print(e.output)

def TesseractInstall():
    try:
        check_call(['sudo','apt-get', 'install', '-y', 'tesseract-ocr'], stdout=open(os.devnull,'wb'))
    except CalledProcessError as e:
        print(e.output)

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Example
if __name__ == '__main__': 
    pipinstall()
    TesseractInstall()
    install('numpy')

p1 = m.Process(target=d.distance)
p2 = m.Process(target=d2.Detect)

name1 = input("Do you want to test? y/n: ")

if name1 == 'y':
    try:
        import pickle

        age = input ('Age?: ')
        gender = input ('Gender?: ')
        agefile = age
        genderfile = gender

        pickle_out = open("age.native","wb")
        pickle.dump(agefile, pickle_out)
        pickle_out.close()


        pickle_out = open("gender.native","wb") 
        pickle.dump(genderfile, pickle_out)
        pickle_out.close()
        
        os.system("python GFBDetectV2.py --conf config/config.json")
    except KeyboardInterrupt:
        os.system("pkill -f GFBDetectV2")
