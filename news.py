import config
import parse
import os


def get_last_news():
    if not os.path.exists(config.ln_file):
        with open(config.ln_file, 'w') as file:
            pass

    last_news = ''
    with open(config.ln_file) as file:
        last_news = file.read()

    news = parse.parse_last_news(config.url + 'news')
    if last_news != news['title']:
        with open(config.ln_file, 'w') as file:
            file.write(news['title'])
        return news
    else:
        return None
