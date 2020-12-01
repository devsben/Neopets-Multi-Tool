import requests
import time
import sys
import platform
from random import uniform
import classes.utilities as utilities

class wrapper:
    def __init__(self):
        self.session = requests.Session()
        self.base = "http://www.neopets.com/"
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:83.0) Gecko/20100101 Firefox/83.0"
        self.session.headers.update({"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.5", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": self.user_agent})
        self.minimum_delay = 1.5
        self.maximum_delay = 5.0
        self.utilities = utilities

    def set_proxy(self, proxy):
        self.session.proxies.update({"http": f"http://{proxy}", "https": f"https://{proxy}"})

    def url(self, path):
        return f"{self.base}{path}"

    def randomize_delay(self):
        return time.sleep(uniform(self.minimum_delay, self.maximum_delay))

    def get_data(self, path, params = None, referer = None):
        self.randomize_delay()
        url = self.url(path)
        if referer:
            self.session.headers.update({"Referer": referer})
        if params:
            response = self.session.get(url, params=params)
        else:
            response = self.session.get(url)
        if "Referer" in self.session.headers:
            del self.session.headers["Referer"]
        return response

    def post_data(self, path, data = None, referer = None):
        self.randomize_delay()
        url = self.url(path)
        if referer:
            self.session.headers.update({"Referer": referer})
        if data:
            response = self.session.post(url, data=data)
        else:
            response = self.session.post(url)
        if "Referer" in self.session.headers:
            del self.session.headers["Referer"]
        return response
