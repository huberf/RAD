import requests as r
from utils import load_config
from PIL import Image
from io import BytesIO
import time

config = load_config.get_config()

def grabFrame():
    for i in config['webcams']:
        response = r.get(i)
        img = Image.open(BytesIO(response.content))
        print(img)

finished = False
delay = 1

print("Running... Ctrl+C to quit")
while not finished:
    grabFrame()
    time.sleep(delay)
