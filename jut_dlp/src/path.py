from re import sub
from jut_dlp.src.global_state import global_state
from pathlib import Path as SysPath

class Path:
    _path:list[str] = []
    _file: str = ""
    
    NORMALIZE_PATTERN = r'[<>:"/\\|?*]'

    def __init__(self):
        self._path.append(global_state.path)

    def set_dir(self,path:str):
        normalize_path = self.normalize_path(path)
        self._path.append(normalize_path)

    def set_file(self,file_name:str, file_ext:str):
        file_path = f"{file_name}.{file_ext}"
        normalize_file_name = self.normalize_path(file_path)
        self._file = normalize_file_name
    
    def normalize_path(self,path:str):
        return sub(self.NORMALIZE_PATTERN, '_', path)

    def get_all_path(self) -> str:
        path = SysPath(self._path[0])
        for subdir in self._path[1:]:
            path = path / subdir

        if self._file:
            path = path / self._file
        return str(path)
    
    def reset_file(self):
        self._file = ""