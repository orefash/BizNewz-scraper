from db_config import postgres_connect
from datetime import date


def init_news_table():
    mydb = None
    cur = None
    try:
        mydb = postgres_connect()
        cur = mydb.cursor()
        cur.execute('''CREATE TABLE news_articles (
  id SERIAL,
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
        mydb.commit()

        print ("Article table created")

    except Exception as e:
        print("Exception", e)
    finally:
        if(mydb):
            cur.close()
            mydb.close()



def init_msg_table():
    mydb = None
    cur = None
    try:
        mydb = postgres_connect()
        cur = mydb.cursor()
        cur.execute('''CREATE TABLE user_msgs (
  id SERIAL,
  uname varchar(300) NOT NULL,
  uemail varchar(300) DEFAULT NULL,
  umessage text,
  entry_date date DEFAULT NULL,
  PRIMARY KEY (id)
)''')
        mydb.commit()

        print ("Msg table created")

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
        mydb = postgres_connect()
        cur = mydb.cursor()
        cur.execute('''CREATE TABLE stock_universe (
  stock_id char(25) NOT NULL,
  stock_symbol varchar(25) NOT NULL,
  company_name varchar(50) NOT NULL,
  PRIMARY KEY (stock_id)
)''')

        mydb.commit()

        print("Stock table created")

    except Exception as e:
        print("Exception", e)

    finally:
        if(mydb):
            cur.close()
            mydb.close()


def test_db():
    mydb = None
    cur = None
    try:
        mydb = postgres_connect()
        cur = mydb.cursor()
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

    except Exception as e:
        print("Exception", e)

    finally:
        if(mydb):
            cur.close()
            mydb.close()


if __name__ == '__main__':
    # test_db()
    # init_news_table()
    # init_stock_table()
    init_msg_table()