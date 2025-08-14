from jut_dlp.src.http_parser import HttpParser
from jut_dlp.src.global_state import global_state

class GetMediaLinkEpisode(HttpParser):
    def __init__(self, url:str):
        self.url = url
        self.headers["Cookie"] = f"player[old][using10]=yes; wap_player=wap_player_3; player[wap_player_res]={global_state.screen_video}"

    def parse(self, soup):
        links = soup.find_all("span",class_="wap_player")
        link_sibnet = None
        for link in links:
            if link.attrs["data-player"].find("https://video.sibnet.ru/shell.php") == 0:
                link_sibnet = link.attrs["data-player"]

        if link_sibnet == None:
            link_sibnet = soup.find("link", itemprop="embedUrl").attrs["href"]      
                
        name = soup.find("h1", class_="header_video allanimevideo the_hildi anime_padding_for_title_post").text.replace("Смотреть ","")
        sub_name = soup.find("div", class_="video_plate_title").text
        full_name = f"{name} {sub_name}"
        
        if not link_sibnet or not full_name:
            raise ValueError("Не удалось получить ссылку или имя файла.")

        return (link_sibnet, full_name)