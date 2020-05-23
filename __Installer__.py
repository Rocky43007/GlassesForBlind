<<<<<<< HEAD
from subprocess import check_call, CalledProcessError
import os

def pipinstall():
    try:
        check_call(['sudo','apt-get', 'install', '-y', 'python3-pip'], stdout=open(os.devnull,'wb'))
    except CalledProcessError as e:
        print(e.output)

=======
>>>>>>> 0ef8fb72fdb40d41ebb43b5959da29e73f277391
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Example
if __name__ == '__main__':
<<<<<<< HEAD
    pipinstall()
=======
>>>>>>> 0ef8fb72fdb40d41ebb43b5959da29e73f277391
    install('numpy')