from jut_dlp.src.http_parser import HttpParser
import re
from urllib.parse import urlparse

class GetVideoLink(HttpParser):
    def __init__(self, url:str):
        self.url = url

    def parse(self, soup):
        media_link = None
        
        for script in soup.find_all("script"):
            content = script.string or ''.join(script.contents)

            if not content:
                continue

            match = re.search(r'player\.src\(\[\{src:\s*"(?P<path>/v/[^"]+\.mp4)"', content)
            if match:
                parsed = urlparse(self.url)
                base_url = f"{parsed.scheme}://{parsed.netloc}"
                media_link = base_url + match.group("path")
        
        if not media_link:
            raise ValueError("Не удалось получить прямую ссылку на видео.")
        
        return media_link