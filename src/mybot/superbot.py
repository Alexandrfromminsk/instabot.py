from  logger import setup_logging
import constants
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

    url = 'https://www.instagram.com/'

    def __init__(self, username, password):
        self.is_logged=False
        self.username=username.lower()
        self.password=password

        self.session = requests.Session()
        #DB?
        self.logger = logging.getLogger(__name__)
        setup_logging()
        self.logger.info("Bot started. User {} attempt to login".format(self.username))
        self.login()

    def login(self):

        self.login_post_data = {
            'username':self.username,
            'password':self.password
        }
        self.session.headers.update(
            {
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Content-Length': '0',
                'Host': 'www.instagram.com',
                'Origin': 'https://www.instagram.com',
                'Referer': 'https://www.instagram.com/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
                'X-Instagram-AJAX': '1',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-Requested-With': 'XMLHttpRequest'
            }
        )
        start_page = self.session.get(constants.url_instagram)
        self.session.headers.update({'X-CSRFToken': start_page.cookies['csrftoken']})

        time.sleep(5 * random.random())

        login_page=self.session.post(
            constants.url_login, data=self.login_post_data, allow_redirects=True
        )

        self.csrftoken = login_page.cookies['csrftoken']
        self.session.update({'X-CSRFToken': self.csrftoken})
        self.session.cookies['ig_vw'] = '1536'
        self.session.cookies['ig_pr'] = '1.25'
        self.session.cookies['ig_vh'] = '772'
        self.session.cookies['ig_or'] = 'landscape-primary'
        time.sleep(5 * random.random())

        if login_page.status_code==200:
            res = self.session.get(constants.url_instagram)
            check=res.text.find(self.username)
            if check!=-1:
                self.is_logged = True
                self.logger.info("{} succesfully loged in".format(self.username))
            else:
                self.logger.error("Failed to log in as {} with password {}".format(self.username, self.password))






