import subprocess
import detect_realtime_tinyyolo_ncs
import os

subprocess.call(["python detect_realtime_tinyyolo_ncs.py","--conf" , "config/config.json", ""])