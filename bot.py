import config
import telebot
import news
import time

bot = telebot.TeleBot(config.token)


if __name__ == '__main__':
    while True:
        time.sleep(2.0)
        data = news.get_last_news()
        if data:
            title, link = data['title'], data['link']
            bot.send_message(config.channel_id, f'{title}\n\n{config.url}{link}')
