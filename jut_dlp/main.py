import argparse

from loguru import logger
from jut_dlp.provider.exception_provider import ExceptionProvider
from jut_dlp.provider.active_method_provider import ActiveMethodProvider

from jut_dlp.src.global_state import global_state
from urllib.parse import urlparse


def main():
    parser = argparse.ArgumentParser(description="jut-dlp — это консольная Python-программа для автоматической загрузки серий и сезонов аниме с сайта jut.su.")
    parser.add_argument("url", help="Ссылка на страницу аниме на jut.su (Например: https://jut.su/onepuunchman/)")
    parser.add_argument("--season", 
                        help="Указать сезоны для загрузки. Возможные форматы: \n" \
                        "* - все сезоны (по умолчанию)\n" \
                        "1 - только первый сезон\n" \
                        "2-4 - диапазон сезонов (второй по четвертый включительно)",
                        default="",
    )
    parser.add_argument("--episode",
                        help="Указать серий для загрузки." \
                        "1 - только первая серия\n"
                        "2-4 - диапазон сезонов (второй по четвертый включительно)",
                        default="*"
    )
    parser.add_argument("--screen",
                    help="Выбрать качество видео для загрузки. "
                         "Доступные значения: 360, 480, 720, 1080. "
                         "По умолчанию выбирается наивысшее доступное качество.",
                    type=int,
                    choices=[360, 480, 720, 1080],
                    default=720)
    
    parser.add_argument("--path",
                    help="Указать путь к папке, в которую будут сохранены загруженные видео. "
                         "По умолчанию используется текущая директория.",
                    type=str,
                    default=".")

    args = parser.parse_args()

    url = args.url
    season = args.season
    episode = args.episode
    
    screen = args.screen
    path = args.path

    parsed = urlparse(url)
    root_url = f'{parsed.scheme}://{parsed.netloc}'
    
    global_state.url = root_url
    global_state.screen_video = screen
    global_state.path = path

    try:
        active_method_provider = ActiveMethodProvider(url,season,episode)
        active_method_provider.active_method()
    except Exception as e:
        exception_provider = ExceptionProvider()
        message = exception_provider.get_message(e)
        logger.error(message)

#if __name__ == "__main__":
#    main()
