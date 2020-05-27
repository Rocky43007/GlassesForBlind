#Copyright Arnab Chakraborty 2020
#For Glasses For Blind Project
#Do not use these files for anything else

from subprocess import check_call, CalledProcessError
import os

def pipinstall():
    try:
        check_call(['sudo','apt-get', 'install', '-y', 'python3-pip'], stdout=open(os.devnull,'wb'))
    except CalledProcessError as e:
       print(e.output)

import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Example
if __name__ == '__main__':
    pipinstall()
    install('numpy')