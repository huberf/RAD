import requests as r
import alert
import classifier
from utils import load_config
from PIL import Image
from io import BytesIO
import time

config = load_config.get_config()

def grabFrames():
    to_return = []
    for i in config['webcams']:
        response = r.get(i)
        img = Image.open(BytesIO(response.content))
        raw_data = list(img.getdata())
        to_return += [raw_data]
    return to_return

def assessStatus(frame):
    status = classifier.getStatus(frame)
    return status

def counterMeasure():
    alert.alert_user('Risk situation', 1)

finished = False
delay = 1

print("Running... Ctrl+C to quit")
while not finished:
    frames = grabFrames()
    for i in frames:
        status = assessStatus(i)
        if status == 'risk':
            counterMeasure()
    time.sleep(delay)
