import requests


class BaseApi:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_response(self, endpoint):
        return requests.get(self.base_url(endpoint))


