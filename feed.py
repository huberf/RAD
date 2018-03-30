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
        response = r.get(i.replace('{time}', str(int(time.time()))))
        img = Image.open(BytesIO(response.content))
        raw_data = list(img.getdata())
        to_return += [raw_data]
    return to_return

lastStatus = None
def assessStatus(frame):
    global lastStatus
    status = classifier.getStatus(frame, lastStatus)
    lastStatus = status
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
        print(status)
        if status == 'risk':
            counterMeasure()
    time.sleep(delay)
