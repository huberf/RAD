import tensorflow as tf
import numpy as np
import time
debug = False

def chunks(l, n):
    return list(np.array_split(l,n))

def getStatus(frame, lastStatus):
    global debug
    frameSlats = 5
    frameSlits = 9
    modFrame = chunks(frame, frameSlats)
    motionPosition = None
    currentState = 'norm'
    saves = []
    for i in range(0,frameSlats):
        saves += [[]]
        for j in range(0, frameSlits):
            saves[i] += [None]
    for i in range(0,frameSlats):
        for j in range(0, frameSlits):
            averageR = 0
            averageG = 0
            averageB = 0
            added = 0
            jIndxB = int((len(modFrame[i])/frameSlits)*j)
            jIndxT = jIndxB + int(len(modFrame[i])/frameSlits)
            for k in modFrame[i][jIndxB:jIndxT]:
                averageR = averageR*added + k[0]
                averageG = averageG*added + k[1]
                averageB = averageB*added + k[2]
                added += 1
                averageR /= added
                averageG /= added
                averageB /= added
            if debug:
                print('Red: ', averageR)
                print('Green: ', averageG)
                print('Blue: ', averageB)
            # Compare average deltas to detect movement or environment changes
            threshold = 4
            if not lastStatus == None:
                if (abs(lastStatus['channels'][i][j]['red'] - averageR) > threshold or
                    abs(lastStatus['channels'][i][j]['green'] - averageG) > threshold or
                    abs(lastStatus['channels'][i][j]['blue'] - averageB) > threshold):
                    currentState = 'motion'
                    motionPosition = [i,j]
            saves[i][j] = { 'red': averageR, 'green': averageG, 'blue': averageB }
    currentTime = time.time()
    return { 'state': currentState, 'motionposition': motionPosition, 'channels' : saves, 'timestamp': currentTime }
