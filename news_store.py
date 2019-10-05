

class NewsBean:
    from datetime import datetime

    news_id = 0
    title = ''
    source = ''
    publish_date = ''
    url=''
    stock=''
    img_url=''
    content=''
    entry_date = datetime.today().strftime('%Y-%m-%d')

class DBConnection:
    import mysql.connector

    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "cnews_db"

    )


class NewsDAO:

    def check_stock(self, title):
        stock_id = ''
#         title = /
        stock_list = self.getStocks()
        for stock in stock_list:
            name = stock[0]
            if name == 'FO':
                name = 'FO '
            elif name == 'ACCESS':
                name = 'ACCESS BANK '
            elif name == 'GUARANTY':
                if 'gtb' in title.lower():
                    stock_id = stock[0]
                    break
            if name.lower() in title.lower() or stock[1].lower().strip() in title.lower():
                stock_id = stock[0]
                break

        return stock_id


    def check_article(self,title):
        exists = False
        mydb = DBConnection().mydb
#         print(mydb)
        cursor = mydb.cursor()
        query = "select * from news_articles where title='"+title+"'"

        ## getting records from the table
        cursor.execute(query)

        ## fetching all records from the 'cursor' object
        records = cursor.fetchall()

        if(len(records)>0):
            exists = True
        return exists

    def addNewsArticle(self, newsBean = NewsBean()):

        check_status = False
        try:
            check_status = self.check_article(newsBean.title)
        except:
            check_status = False

        if check_status is False:
            mydb = DBConnection().mydb
            mycursor = mydb.cursor()
            query = "insert into news_articles values (0,%s,%s, %s,%s,%s,%s,%s,%s)"
            newsBean.stock = self.check_stock(newsBean.title)
            val = (newsBean.title, newsBean.source, newsBean.publish_date, newsBean.img_url, newsBean.content, newsBean.url, newsBean.stock, newsBean.entry_date)
    #         print("Val: ",val)
            mycursor.execute(query, val)
            mydb.commit()
            print(mycursor.rowcount, "records Inserted")
            status = 1
            if mycursor.rowcount > 0:
                status = 0
        else:
            status = -1

        return status

    def getStocks(self):
        stocks = []
        mydb = DBConnection().mydb
        mycursor = mydb.cursor()
        mycursor.execute("select stock_id, company_name from stock_universe")
        myResult = mycursor.fetchall()
        for x in myResult:
            company = x[1]
            split = company.split(' ')
            if len(split) > 2:
                company = split[0] + ' ' + split[1]
            data = (x[0], company.lower().replace('plc.', '').replace('plc', '').replace('.', ''))
            stocks.append(data)
#         mycursor.close()
#         mydb.close()
        return stocks
