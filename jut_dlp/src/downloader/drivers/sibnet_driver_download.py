from jut_dlp.src.downloader.drivers.driver_download import DriverDownload
from requests import get
from secrets import token_hex

class SibnetDriverDownload(DriverDownload):
    _headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        ),
        "Accept": "*/*",
        "Accept-Encoding": "identity",
        "Connection": "keep-alive",
        "DNT": "1",
        "Sec-Fetch-Dest": "video",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "cross-site",
    }

    def __init__(self):
        self._cookies = {
            "PHPSESSID": token_hex(16)
        }

    def download(self, media_url):
        response = get(media_url, headers=self._headers, cookies=self._cookies, stream=True) 
        return response