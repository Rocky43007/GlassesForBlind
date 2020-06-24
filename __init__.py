#import pip
#import __Installer__.py
import GFBDistance as d
import GFBDetection as d2
from threading import Thread
from subprocess import *
import multiprocessing as m
import time
import os
import sys
import concurrent.futures as cf
#def pipinstall():
#    try:
#        check_call(['sudo','apt-get', 'install', '-y', 'python3-pip'], stdout=open(os.devnull,'wb'))
#    except CalledProcessError as e:
#        print(e.output)
#
#def TesseractInstall():
#    try:
#        check_call(['sudo','apt-get', 'install', '-y', 'tesseract-ocr'], stdout=open(os.devnull,'wb'))
#    except CalledProcessError as e:
#        print(e.output)
#
#def install(package):
#    if hasattr(pip, 'main'):
#        pip.main(['install', package])
#    else:
#        pip._internal.main(['install', package])
#
# Example
#if __name__ == '__main__': 
#    pipinstall()
#    TesseractInstall()
#    install('numpy')
#
#def Data():
#    sd.ImageRec()
#    sd.ultrasonic()
p1 = m.Process(target=d.distance)
p2 = m.Process(target=d2.Detect)

name1 = input("Do you want to test? y/n: ")

if name1 == 'y':
#    with cf.ProcessPoolExecutor as executor:
#        f1 = executor.submit(d.Ultra, 1)
#        f2 = executor.submit(d2.Detect, 1)
#        print (f1.result())
#        print (f2.result())
    try:
        os.system("python DistanceScanner.py &")
        os.system("python GFBDetectV2.py --conf config/config.json")
    except KeyboardInterrupt:
        os.system("pkill -f python")
