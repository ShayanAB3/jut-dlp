from jut_dlp.src.path import Path
from requests import Response
from tqdm import tqdm
from pathlib import Path as PathLib

class Uploader:
    path: Path
    response: Response
    def __init__(self, path:Path, response:Response):
        self.path = path
        self.response = response

    def upload(self):
        total = int(self.response.headers.get("Content-Length", 0))
        name = PathLib(self.path.get_all_path()).stem
        
        with open(self.path.get_all_path(), "wb") as f, tqdm(
                total=total,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                desc=name
            ) as bar:
                for chunk in self.response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        bar.update(len(chunk))
    