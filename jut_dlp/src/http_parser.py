from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

import requests

class HttpParser(ABC):
    url:str
    headers:dict[str,str] = {
        "User-Agent": "Mozilla/5.0"
    }

    @abstractmethod
    def parse(self,soup: BeautifulSoup):
        pass
    
    def _send_parse(self, html:str):
        soup = BeautifulSoup(html, "html.parser")
        return self.parse(soup)

    def get(self):
        response = requests.get(self.url, headers=self.headers)
        return self._send_parse(response.text)

    def post(self, data:dict[str,str] = {}):
        response = requests.post(self.url, data=data, headers=self.headers)
        self._send_parse(response.text)