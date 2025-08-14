from jut_dlp.src.downloader.drivers.driver_download import DriverDownload
from jut_dlp.src.downloader.uploader import Uploader

from jut_dlp.src.path import Path

class Downloader:
    download_driver : DriverDownload
    path:Path

    def __init__(self, download_driver : DriverDownload, path: Path):
        self.download_driver = download_driver
        self.path = path

    def download(self, media_url:str):
        response = self.download_driver.download(media_url)
        uploader = Uploader(self.path,response)
        uploader.upload()
        

        