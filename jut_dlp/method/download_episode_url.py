from jut_dlp.method.method import Method
from jut_dlp.src.url import URL
from jut_dlp.action.download_episode import DownloadEpisode
from jut_dlp.parser.get_media_link_episode import GetMediaLinkEpisode
from loguru import logger

class DownloadEpisodeURL(Method):
    def is_activation_allowed(self):
        url = URL(self.url)
        return url.is_page_episode()
    
    def activate(self):
        get_media_link_episode = GetMediaLinkEpisode(self.url)
        sibnet_link, full_name = get_media_link_episode.get()
        logger.info(f"Начинается скачиваение {full_name}")
        DownloadEpisode.download(self.url, self.path)