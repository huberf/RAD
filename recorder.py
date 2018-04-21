import json
EVENT_FILE = 'events.rad'

eventFile = open(EVENT_FILE, 'a')

def log(event):
    event['version'] = '0.1.0'
    eventFile.write('\n' + json.dumps(event))
