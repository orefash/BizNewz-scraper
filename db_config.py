

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
        host="ec2-54-75-245-196.eu-west-1.compute.amazonaws.com",
        database="db2ap032l7mp3t",
         user="jazzyzfqzynrrx",
          password="670a46230b9e682e3afafb134bf16421c01acb4f2d05183f0018a97fbc0d4724"
    )

    return conn

