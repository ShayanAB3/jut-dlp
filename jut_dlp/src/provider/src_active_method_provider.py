from abc import ABC
from jut_dlp.method.method import Method

from loguru import logger
from os import remove
from os.path import exists

class SrcActiveMethodProvider(ABC):
    url:str
    season:str
    episode:str

    methods:list[type[Method]]

    def __init__(self, url:str, season:str, episode:str):
        self.url = url
        self.season = season
        self.episode = episode

    def active_method(self):
        for MethodClass in self.methods:
            method_class = MethodClass(self.url,self.season,self.episode)
            if method_class.is_activation_allowed():
                try:
                    method_class.activate()
                except KeyboardInterrupt:
                    logger.warning("⚠️ Скачивание прервано пользователем. Удаляю файл...")
                    temp_path = method_class.path.get_all_path()
                    if exists(temp_path):
                        remove(temp_path)