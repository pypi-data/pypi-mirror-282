import requests
import json
import uuid
import threading
from datetime import datetime, timezone
import pytz

session = requests.Session()


def MaskaAI(whatisthemode, message):
    if whatisthemode == "Code":
        number = 15
    elif whatisthemode == "Fast":
        number = 6
    elif whatisthemode == "Text":
        number = 20
    elif whatisthemode == "Middle":
        number = 10
    else:
        number = 15
    return messagetotest(message, number)

