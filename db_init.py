from db_config import mysql_connect
from datetime import date
import pymysql


def init_news_table():
    mydb = None
    cur = None
    try:
        mydb = mysql_connnect()
        cur = mydb.cursor()
        cur.execute('''CREATE TABLE news_articles (
  id int(11) NOT NULL AUTO_INCREMENT,
  title varchar(300) NOT NULL,
  source varchar(50) NOT NULL,
  publish_date date NOT NULL,
  img_url varchar(300) DEFAULT NULL,
  content text,
  url varchar(300) NOT NULL,
  stock_id varchar(50) DEFAULT NULL,
  entry_date date DEFAULT NULL,
  PRIMARY KEY (id)
)''')

    except Exception as e:
        print("Exception", e)
    finally:
        if(mydb):
            cur.close()
            mydb.close()


def init_stock_table():
    mydb = None
    cur = None
    try:
        mydb = mysql_connnect()
        cur = mydb.cursor()
        cur.execute('''CREATE TABLE stock_universe (
  stock_id char(25) NOT NULL,
  stock_symbol varchar(25) NOT NULL,
  company_name varchar(50) NOT NULL,
  PRIMARY KEY (stock_id)
)''')

    except Exception as e:
        print("Exception", e)

    finally:
        if(mydb):
            cur.close()
            mydb.close()


if __name__ == '__main__':
    init_news_table()
    init_stock_table()