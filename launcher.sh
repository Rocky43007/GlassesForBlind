#!/bin/bash
#!/usr/local/lib/python3.7
# launcher.sh
# Go to home directory, then to file then excecute python script.
export PYTHONPATH=$PYTHONPATH:/home/pi/GlassesForBlind/pyimagesearch:/home/pi/.virtualenvs/openvino/lib/python3.7/site-packages
source /home/pi/openvino/bin/activate
# Only uncomment the line below if needed for testing the Object Detection by itself.
#python3 /home/pi/GlassesForBlind/GFBDetect.py --conf /home/pi/GlassesForBlind/config/config.json
python3 /home/pi/GlassesForBlind/__init__.py

