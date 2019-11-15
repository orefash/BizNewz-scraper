
from db_config import mysql_connect, postgres_connect

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
        mydb = None
        cursor = None

        try:

            # mydb = mysql_connnect()
            mydb = postgres_connect()
    #         print(mydb)
            cursor = mydb.cursor()
            query = "select * from news_articles where title='"+title+"'"

            ## getting records from the table
            cursor.execute(query)

            ## fetching all records from the 'cursor' object
            records = cursor.fetchall()

            if(len(records)>0):
                exists = True
        except Exception as e:
            print("Exception", e)
        finally:
            if(mydb):
                cursor.close()
                mydb.close()
        return exists

    def addNewsArticle(self, newsBean = NewsBean()):
        status = -1
        check_status = False
        try:
            check_status = self.check_article(newsBean.title)
        except:
            check_status = False

        if check_status is False:

            mydb = None
            mycursor = None
            
            try:
                # mydb = mysql_connnect()
                
                mydb = postgres_connect()
                mycursor = mydb.cursor()
                query = "insert into news_articles values (DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s)"
                newsBean.stock = ""
                # newsBean.stock = self.check_stock(newsBean.title)
                val = (newsBean.title, newsBean.source, newsBean.publish_date, newsBean.img_url, newsBean.content, newsBean.url, newsBean.stock, newsBean.entry_date)
        #         print("Val: ",val)
                mycursor.execute(query, val)
                mydb.commit()
                print(mycursor.rowcount, "records Inserted")
                status = 1
                if mycursor.rowcount > 0:
                    status = 0
            except Exception as e:
                print("Exception", e)
            finally:
                if(mydb):
                    mycursor.close()
                    mydb.close()


        else:
            status = -1

        return status

    def getStocks(self):
        stocks = []
        mydb = None
        mycursor = None

        try:
            # mydb = mysql_connnect()
            mydb = postgres_connect()
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
        except Exception as e:
                print("Exception", e)
        finally:
            if(mydb):
                mycursor.close()
                mydb.close()
#         mycursor.close()
#         mydb.close()
        return stocks
