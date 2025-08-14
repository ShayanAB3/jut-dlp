from loguru import logger

class Input:
    max_len_seasons:int
    type_name_season_or_episode:str

    def set_max_len_seasons(self, len:int):
        self.max_len_seasons = len

    def set_type_name_season_or_episode(self, name:str):
        self.type_name_season_or_episode = name

    def check_max_len_seasons(self,num:int) -> int:
        if self.max_len_seasons < num:
            logger.warning(f"Указанное число {num} превышает допустимое количество сезонов. Приведено к {self.type_name_season_or_episode}.")
            return self.max_len_seasons
        return num

    def get_list_numbers(self, type_str:str) -> list[int]:
        if(type_str == "*"):
            return list(range(self.max_len_seasons))
        if(type_str.isnumeric()):
            num = self.check_max_len_seasons(int(type_str))
            return [num-1]
        
        if(not type_str.find("-")):
            raise ValueError("Неверный формат диапазона. Укажите через дефис, например: 1-5")
        
        start_and_end = type_str.split("-")

        start = int(start_and_end[0])-1
        end = self.check_max_len_seasons(int(start_and_end[1]))

        if start <= -1:
            logger.warning(f"Начальное диапозонное число начинается с 1 (Одного). Приведено к 1.")
            start = 0

        return list(range(start, end))

