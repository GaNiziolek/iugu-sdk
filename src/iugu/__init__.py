import importlib.metadata
import requests

from iugu.customer import CustomerActions

__version__ = importlib.metadata.version('iugu-sdk')

class Iugu:

    def __init__(self, token: str) -> None:

        self.token = token

        self.base_url = 'https://api.iugu.com/v1'
        
        self.default_headers = {
            "User-Agent": f"Iugu Python SDK v{__version__}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        self.customer = CustomerActions(self)

    def request(self, method: str, url: str, params: dict = None, json: dict = None ) -> requests.Response:

        if not url.startswith('/'):
            url = '/' + url

        full_url = self.base_url + url

        res = requests.request(
            method  = method,
            url     = full_url,
            headers = self.default_headers,
            params  = params,
            json    = json,
            timeout = 10
        )

        res.raise_for_status()

        return res.json()

