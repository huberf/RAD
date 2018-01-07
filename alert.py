from utils import load_config
import requests as r

config = load_config.get_config()

# Lower level means higher priority so 1 is the highest priority
def alert_user(message, level):
    url = config['alert_url']
    r.get(url)
