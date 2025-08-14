from jut_dlp.method.download_episode_url import DownloadEpisodeURL
from jut_dlp.method.download_seasons_url import DownloadSeasonsURL

from jut_dlp.method.method import Method

from jut_dlp.src.provider.src_active_method_provider import SrcActiveMethodProvider

class ActiveMethodProvider(SrcActiveMethodProvider):
    methods:list[type[Method]] = [
        DownloadEpisodeURL,
        DownloadSeasonsURL
    ]