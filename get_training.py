from utils import load_config
import time
import urllib.request

import os

config = load_config.get_config()

def download_image(state):
    directory = 'training_set/'
    for i in config['webcams']:
        timestamp = time.time()
        filename = '{state}_{timestamp}.jpg'.format(state=state, timestamp=timestamp)
        urllib.request.urlretrieve(i, directory + filename)

if __name__ == '__main__':
    captureCount = 4
    state = input('State> ')
    for i in range(captureCount):
        time.sleep(0.5)
        download_image(state)
    print('Done.')
