class SeasonAnime:
    season_name: str
    episodes: list[dict[str, str]] = []

    def __init__(self, name:str, links: list[dict[str, str]]):
        self.season_name = name
        self.episodes = links