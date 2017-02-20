import requests
from requests.exceptions import RequestException


class PopcornTime:
    headers = {'content-type': 'application/json; charset=utf-8'}

    def get_request(self, url):
        try:
            r = requests.get(url, headers=self.headers)
            return r
        except RequestException:
            return


popcorn_time = PopcornTime()
