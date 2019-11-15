from news_store import NewsDAO, NewsBean
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse

class PunchNG:
    base_url = "https://punchng.com/topics/business/"
    pages = 2
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like


    def __init__(self):
        print('in punch')
        articles = self.parse_articles()
        self.store_articles(articles)
#         print (articles)

    def get_page_soup(self, index):
        url = self.base_url
        if index>1:
            url = url+"page/"+str(index)+"/"
#         soup = ''
#         print(url)

        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        return soup

    def get_article_from_page(self, soup):
        articles = []
        article_div = soup.find_all('div', class_='items')
        for ard in article_div:
            header = ard.find('h2', class_='seg-title')
            title = header.text
            url = header.find_parent('a').get('href')
            ncontent = ard.find('div', class_='seg-summary').find('p').text
            # print(ncontent)
            img_url = ard.find('figure', class_='seg-image')['data-src']
            inner_div = ard.find('div', class_='seg-time').find('span', class_='pull-right')
            date = inner_div.text
            
            datetime = parse(date)
            articles.append((title.strip(), url, datetime, img_url, ncontent))
#             print("In Parse : ",article)
            # articles.append(article)

        return articles

    def parse_articles(self):
        articles_group = []
        for i in range(1,(self.pages+1)):
            try:
                soup = self.get_page_soup(i)
                articles = self.get_article_from_page(soup)

                articles_group = articles_group + articles
            except:
                pass
        return articles_group

    def store_articles(self, articles):
        newsDAO = NewsDAO()
#         print(articles)
        for article in articles:
#             print(article)
            newsBean = NewsBean()
            newsBean.title = article[0]
            newsBean.url = article[1]
            newsBean.publish_date = article[2]
            newsBean.img_url = article[3]
            newsBean.source = "PunchNG"
            newsBean.content = article[4]

            newsDAO.addNewsArticle(newsBean)

# nm = PunchNG()