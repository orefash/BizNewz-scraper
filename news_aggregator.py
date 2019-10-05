import feedparser as fp
import json
import newspaper
from newspaper import Article
from time import mktime
from datetime import datetime
import csv

# def parse_rss():

def get_news_articles():
    LIMIT = 5
    articles_array = []

    data = {}
    data['newspapers'] = {}

    with open('links.json') as data_file:
        companies = json.load(data_file)

    count = 1
    print(companies.items())
    # Iterate through each news company
    for company, value in companies.items():
        if 'rss' in value:
            d = fp.parse(value['rss'])
            print("Downloading articles from ", company)
            for entry in d.entries:
                # Check if publish date is provided, if no the article is skipped.
                # This is done to keep consistency in the data and to keep the script from crashing.
                if hasattr(entry, 'published'):
                    if count > LIMIT:
                        break
                    article = {}
                    article['link'] = entry.link
                    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    if entry.published_parsed is not None:
                        date = entry.published_parsed

                    article['published'] = datetime.fromtimestamp(mktime(date)).isoformat()
                    try:
                        content = Article(entry.link)
                        content.download()
                        content.parse()
                    except Exception as e:
                        # If the download for some reason fails (ex. 404) the script will continue downloading
                        # the next article.
                        print(e)
                        print("continuing...")
                        continue
                    article['title'] = content.title
                    article['source'] = company
                    # newsPaper['articles'].append(article)
                    articles_array.append(article)
                    print(count, "articles downloaded from", company, ", url: ", entry.link)
                    count = count + 1
        else:
            # This is the fallback method if a RSS-feed link is not provided.
            # It uses the python newspaper library to extract articles
            print("Building site for ", company)
            print(value['link'])
            paper = newspaper.build(value['link'], memoize_articles=False)
            # newsPaper = {
            #     "link": value['link'],
            #     "articles": []
            # }
            noneTypeCount = 0
            for content in paper.articles:
                if count > LIMIT:
                    break
                try:
                    content.download()
                    content.parse()
                except Exception as e:
                    print(e)
                    print("continuing...")
                    continue
                # Again, for consistency, if there is no found publish date the article will be skipped.

                article = {}
                article['title'] = content.title
                article['source'] = company
                article['link'] = content.url

                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if content.publish_date is not None:
                    date = content.publish_date
                article['published'] = date
                # newsPaper['articles'].append(article)
                articles_array.append(article)
#                 print(count, "articles downloaded from", company, " using newspaper, url: ", content.url)
                count = count + 1
                #noneTypeCount = 0
        count = 1
        # data['newspapers'][company] = newsPaper
    return articles_array
articles = get_news_articles()
# print (articles)
import json
articles_json = json.dumps(articles)
print(articles_json)
