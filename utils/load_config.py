import json

def get_config():
    config = json.load(open('config.json'))
    # TODO: Add screening function to verify config integrity
    return config
