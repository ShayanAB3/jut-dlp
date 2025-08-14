from abc import ABC, abstractmethod
from requests import Response

class DriverDownload(ABC):
    _headers:dict[str,str] = {}
    _cookies:dict[str,str] = {}

    def set_header(self,key:str, value:str):
        self._headers[key] = value

    def set_cookie(self,key:str, value:str):
        self._cookies[key] = value

    @abstractmethod
    def download(self,media_url:str) -> Response:
        pass