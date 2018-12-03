from  logger import setup_logging
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

    def __init__(self, username, password):
        self.username=username.lower()
        self.password=password

        self.session = requests.Session()
        #DB?
        logger = logging.getLogger(__name__)
        setup_logging()
        logger.info("Bot started. User {} attempt to login".format(self.username))
        self.login()





