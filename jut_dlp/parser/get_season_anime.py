from jut_dlp.src.http_parser import HttpParser
from jut_dlp.dto.season_anime import SeasonAnime
from jut_dlp.src.global_state import global_state

class GetSeasonAnime(HttpParser):
    def __init__(self, url):
        self.url = url

    def parse(self, soup) -> tuple[str, list[SeasonAnime], str]:
        name = soup.find("h1", class_="header_video allanimevideo anime_padding_for_title").text

        seasons = []
        current_season = None
        h2_found = any(tag.name == "h2" for tag in soup.select(".the-anime-season, a.short-btn.video.the_hildi"))

        for tag in soup.select(".the-anime-season, a.short-btn.video.the_hildi"):
            if h2_found and tag.name == "h2":
                current_season = {
                    "name": tag.get_text(strip=True),
                    "links": []
                }
                seasons.append(current_season)

            elif tag.name == "a":
                href = tag.get("href")
                if href:
                    full_url = global_state.url + href
                    if h2_found:
                        if current_season:
                            current_season["links"].append({
                                "name": tag.text,
                                "url": full_url
                            })
                    else:
                        if not seasons:
                            current_season = {
                                "name": "1 сезон",
                                "links": []
                            }
                            seasons.append(current_season)
                        seasons[0]["links"].append({
                            "name": tag.text,
                            "url": full_url
                        })

        seasons_anime = [SeasonAnime(season["name"], season["links"]) for season in seasons]
        original_name = name.removeprefix("Смотреть ").removesuffix(" все серии и сезоны").strip()
        return name, seasons_anime, original_name