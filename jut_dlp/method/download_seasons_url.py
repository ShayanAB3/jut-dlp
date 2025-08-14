from jut_dlp.method.method import Method

from jut_dlp.parser.get_season_anime import GetSeasonAnime
from jut_dlp.action.select_season import SelectSeason

from loguru import logger

from jut_dlp.action.download_episode import DownloadEpisode
from jut_dlp.src.url import URL
from jut_dlp.dto.season_anime import SeasonAnime


class DownloadSeasonsURL(Method):
    def is_activation_allowed(self):
        url = URL(self.url)
        return url.is_list_seasons()

    def activate(self):
        getSeasonAnime = GetSeasonAnime(self.url)
        name, seasons, original_name = getSeasonAnime.get()

        seasons:list[SeasonAnime] = seasons
        table = [[i, val.season_name] for i, val in enumerate(seasons, start=1)]
        
        if not self.season:
            season = SelectSeason.show_table(name, table)
            self.season = season

        self.input.set_type_name_season_or_episode("сезонов")
        self.input.set_max_len_seasons(len(table))
        numbers:list[int] = self.input.get_list_numbers(self.season)
        
        for number in numbers:
            season_name = seasons[number].season_name
            episodes:list[dict[str,str]] = seasons[number].episodes
            
            self.input.set_type_name_season_or_episode("серий")
            self.input.set_max_len_seasons(len(episodes))
            number_episodes:list[int] = self.input.get_list_numbers(self.episode)

            episodes = list(map(lambda index: episodes[index] , number_episodes))

            self.path.set_dir(original_name)
            self.path.set_dir(season_name)

            logger.info(f"Начинается скачиваение {season_name} от аниме {original_name}")

            
            for episode in episodes:
                DownloadEpisode.download(episode["url"], self.path)
                self.path.reset_file()
            