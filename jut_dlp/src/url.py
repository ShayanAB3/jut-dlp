from re import compile
from urllib.parse import urlparse

class URL:
    LIST_SEASONS = r"^/[^/]+/?$"
    PAGE_EPISODE = r"^/[^/]+/season-\d+/episode-\d+\.html$"

    path:str

    def __init__(self, url:str):
        parsed_url = urlparse(url)
        self.path = parsed_url.path

    def is_list_seasons(self) -> bool:
        pattern = compile(self.LIST_SEASONS)
        return bool(pattern.fullmatch(self.path))

    def is_page_episode(self) -> bool:
        pattern = compile(self.PAGE_EPISODE)
        return bool(pattern.fullmatch(self.path))