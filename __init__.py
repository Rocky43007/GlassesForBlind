import pip
import __Installer__.py
import SensorData.py as sd
import OCRRecog.py


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

def Data():
    sd.ImageRec()
    sd.ultrasonic()
