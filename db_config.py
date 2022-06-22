

from flaskext.mysql import MySQL
import psycopg2

def mysql_connect():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "password",
        # database = "cnews_db"
        database = "sampledb"

    )
    return mydb

def postgres_connect():
    	
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="test2",
    #      user="postgres",
    #       password="admin"
    # )

    conn = psycopg2.connect(
        host="DB-HOST",
        database="DB-NAME
         user="DB-USER",
          password="DB-PASS"
    )

    return conn

