import requests
import atexit
import datetime
import itertools
import json
import logging
import random
import signal
import sys
import sqlite3
import time
import requests

class SuperBot:
    """
    My bot which reuse some code from instabot, but eperform steps
    that I want.
    """

    def __init__(self, login, password):
        self.login=login
        self.password=password

        self.session = requests.Session()

        #DB?




