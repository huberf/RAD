import tensorflow as tf
import time
debug = False

def getStatus(frame, lastStatus):
    global debug
    averageR = 0
    averageG = 0
    averageB = 0
    added = 0
    for i in frame:
        averageR = averageR*added + i[0]
        averageG = averageG*added + i[1]
        averageB = averageB*added + i[2]
        added += 1
        averageR /= added
        averageG /= added
        averageB /= added
    if debug:
        print('Red: ', averageR)
        print('Green: ', averageG)
        print('Blue: ', averageB)
    currentState = 'normal'
    # Compare average deltas to detect movement or environment changes
    threshold = 4
    if not lastStatus == None:
        if (abs(lastStatus['channels']['red'] - averageR) > threshold or
            abs(lastStatus['channels']['green'] - averageG) > threshold or
            abs(lastStatus['channels']['blue'] - averageB) > threshold):
            currentState = 'motion'
    currentTime = time.time()
    return { 'state': currentState, 'channels' : { 'red': averageR, 'green': averageG, 'blue': averageB }, 'timestamp': currentTime }
