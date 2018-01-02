from utils import load_config
import time
import urllib.request

import os

config = load_config.get_config()

def download_image(state):
    for i in config['webcams']:
        timestamp = time.time()
        filename = '{state}_{timestamp}.jpg'.format(state=state, timestamp=timestamp)
        urllib.request.urlretrieve(i, filename)

if __name__ == '__main__':
    state = input('State> ')
    download_image(state)
    print('Done.')
