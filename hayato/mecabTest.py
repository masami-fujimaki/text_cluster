from database import Database
import mecab

db = Database()
news = db.news("568ce39ee1382354c301f100")
for n in mecab.get_noun(news['text']):
    print "{}\t{}\t{}".format(n['noun'], n['feature_1'], n['feature_2'])

for n in mecab.get_news_noun(news['text']):
    print n 
