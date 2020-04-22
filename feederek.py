import feedparser
import pickle
import telebot
import sys
from time import sleep

feed_list =["https://vchasnoua.com/rss/",
            ]

last_feeds = pickle.load(open("db.p", 'rb'))
fee_links = []

bot = telebot.TeleBot(token='1279713740:AAHr5YwqV-f1vHC0mxXdCuAqOSovRHhZSfU')

print(last_feeds)
print("-----Last feeds---")

def feederek():
    for i in feed_list:
        fee = feedparser.parse(i)
        fee_title = fee.feed.title
        for x in range(5):
            fee_links.append(fee['entries'][x]['id'])
            if fee['entries'][x]['id'] in last_feeds:
                print("Nothing new - " + fee_title)
            else:
                sleep(5) # for server flood detection
                entry_title = fee['entries'][x]['title']
                entry_id = fee['entries'][x]['id']
                print("Updated - " + fee_title)


                message = str(fee_title +"\n" + entry_title +"\n" + entry_id)
                bot.send_message(chat_id="@pokrovskme", text=message)

    pickle.dump(fee_links, open("db.p", 'wb'))
    sys.exit(0)

if __name__ == "__main__":
    feederek()
