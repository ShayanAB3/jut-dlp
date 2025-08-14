from jut_dlp.parser.get_media_link_episode import GetMediaLinkEpisode
from jut_dlp.parser.sibnet.get_video_link import GetVideoLink

from jut_dlp.src.downloader.downloader import Downloader

from concurrent.futures import ThreadPoolExecutor, as_completed

from os import makedirs
from os.path import exists

from jut_dlp.src.path import Path
from jut_dlp.src.downloader.drivers.sibnet_driver_download import SibnetDriverDownload

from loguru import logger

class DownloadEpisode:
    def download(url:str, path:Path):
        get_media_link_episode = GetMediaLinkEpisode(url)
        sibnet_link, full_name = get_media_link_episode.get()

        get_video_link = GetVideoLink(sibnet_link)
        media_link = get_video_link.get()

        dir_path = path.get_all_path()

        makedirs(dir_path, exist_ok=True)

        path.set_file(full_name, "mp4")
        file_path = path.get_all_path()

        if exists(file_path):
            logger.info(f"Файл с именем {file_path} уже существует. Пропускаем загрузку.")
            return
        
        sibnet_driver_download = SibnetDriverDownload()
        sibnet_driver_download.set_header("Referer", sibnet_link)

        downloader = Downloader(sibnet_driver_download, path)
        downloader.download(media_link)
    

    def download_in_batches(urls: list[str], path: Path, max_workers=4):
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(DownloadEpisode.download, url, path) for url in urls]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logger.error(f"Ошибка при загрузке: {e}")