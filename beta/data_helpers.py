'''Imports all image files and automatically makes classifiers for training'''

import numpy as np
from os import listdir
import pickle
import sys
from PIL import Image
from io import BytesIO

def load_data():
    to_return = { 'images_train': [],
            'labels_train': [],
            'images_test': [],
            'labels_test': [],
            'classes': []
            }
    keys = {}
    classes = []
    last_index = -1
    imageDir = '../'
    imageFiles = listdir(imageDir)
    for i in imageFiles:
        if i.endswith('.jpg'):
            img = Image.open(imageDir + i)
            raw_data = list(img.getdata())
            data_array = []
            for q in raw_data:
                data_array += [q[0]]
                data_array += [q[1]]
                data_array += [q[2]]
            print(len(data_array))
            splinter = i.split('1')
            label = splinter[0]
            label_index = 0
            try:
                label_index = keys[label]
            except:
                last_index += 1
                keys[label] = last_index
                classes += [label]
                label_index = last_index
            to_return['images_train'] += [data_array]
            to_return['labels_train'] += [label_index]
            # In the future make selective test addition
            to_return['images_test'] += [data_array]
            to_return['labels_test'] += [label_index]
    to_return['images_train'] = np.array(to_return['images_train'])
    to_return['labels_train'] = np.array(to_return['labels_train'])
    to_return['images_test'] = np.array(to_return['images_test'])
    to_return['labes_test'] = np.array(to_return['images_test'])
    to_return['classes'] = classes
    return to_return

if __name__ == '__main__':
    out = load_data()
    print("Working...")
