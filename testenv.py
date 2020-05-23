from subprocess import check_call, CalledProcessError
import os

<<<<<<< HEAD
def pipinstall():
=======
def Test():
>>>>>>> 0ef8fb72fdb40d41ebb43b5959da29e73f277391
    try:
        check_call(['sudo','apt-get', 'install', '-y', 'python3-pip'], stdout=open(os.devnull,'wb'))
    except CalledProcessError as e:
        print(e.output)

Test()