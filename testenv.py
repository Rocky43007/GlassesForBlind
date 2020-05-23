from subprocess import check_call, CalledProcessError
import os

def pipinstall():
    try:
        check_call(['sudo','apt-get', 'install', '-y', 'python3-pip'], stdout=open(os.devnull,'wb'))
    except CalledProcessError as e:
        print(e.output)

Test()