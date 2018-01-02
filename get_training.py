from utils import load_config
import time
import urllib
import os

config = load_config.get_config()

def download_image(state):
    for i in config['webcams']:
        image = urllib.URLopener()
        timestamp = time.time()
        image.retrieve(i, '{state}{timestamp}.jpg'.format(state=state, timestamp=timestamp))

if __name__ == '__main__':
    state = raw_input('State> ')
    download_image(state)
    print('Done.')
