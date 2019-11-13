from news_store import NewsDAO, NewsBean
import requests
from bs4 import BeautifulSoup

class Nairametrics:
    base_url = "https://nairametrics.com/category/nigeria-business-news/latest-nigerian-company-news/"
    pages = 15
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like


    def __init__(self):
        print('in nairametrics')
        articles = self.parse_articles()
        self.store_articles(articles)

    def get_page_soup(self, index):
        url = self.base_url
        if index>1:
            url = url+"page/"+str(index)+"/"

        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        return soup

    def get_article_from_page(self, soup):
        articles = []
        article_div = soup.find_all('div', class_='td_module_11 td_module_wrap td-animation-stack')
#         print(article_div)
        for div in article_div:
            parent_div = div.find_parent('div')
            img_url = div.find('img', class_='entry-thumb')['src']

            header = div.find('h3', class_='entry-title td-module-title')
            
#             print("In parse head : ",header)
            title = header.find('a').text
#             print("In parse: ",title)
            url = header.find('a').get('href')
            inner_div = div.find('div', class_='td-module-meta-info')
            
            ncontent = div.find('div', class_='td-excerpt').text
            # print('ncontent: ', ncontent)
            inner_span = inner_div.find('span', class_='td-post-date')
            date = inner_span.find('time', class_='entry-date updated td-module-date').get('datetime').split('T',1)[0]
            article= (title.strip(), url, date, img_url, ncontent)
            articles.append(article)

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
        
        for article in articles:
            newsBean = NewsBean()
            newsBean.title = article[0]
            newsBean.url = article[1]
            newsBean.publish_date = article[2]
            newsBean.img_url = article[3]
            newsBean.source = "Nairametrics"
            newsBean.content = article[4]

            try:
                newsDAO.addNewsArticle(newsBean)
            except:
                pass

# nm = Nairametrics()