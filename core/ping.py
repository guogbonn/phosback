import time
import requests
import settings


while True:
    time.sleep(120)
    r = requests.get(settings.BACKEND_URL + '/ping')
    print("still alive")
