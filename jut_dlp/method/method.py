from abc import ABC, abstractmethod
from jut_dlp.src.input import Input
from jut_dlp.src.path import Path

class Method(ABC):
    url:str
    season:str
    episode:str
    
    input:Input
    path:Path

    def __init__(self, url:str, season:str, episode:str):
        self.url = url
        self.season = season
        self.episode = episode

        self.input = Input()
        self.path = Path()

    @abstractmethod
    def is_activation_allowed(self) -> bool:
        pass
    @abstractmethod
    def activate(self):
        pass