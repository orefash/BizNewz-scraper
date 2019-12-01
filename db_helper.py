from flask import Flask, jsonify, flash, redirect, render_template, url_for
from nairametrics_parser import Nairametrics
from punch_parser import PunchNG
from db_config import mysql_connect, postgres_connect
from datetime import date
import pymysql
import psycopg2.extras




def get_sources():
    mydb = None
    cur = None
    try:
        mydb = postgres_connect()
        cur = mydb.cursor()
        cur.execute("SELECT DISTINCT(source) from news_articles")
        rows = cur.fetchall()
        resp = rows
        # resp.status_code = 200
        return resp
    except Exception as e:
        print("Exception", e)
        return []
    finally:
        if mydb is not None:
            cur.close()
            mydb.close()

def get_article_data():
    
    mydb = None
    cur = None
    try:
        mydb = postgres_connect()
        cur = mydb.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * from news_articles")
        rows = cur.fetchall()
        resp = rows
        return resp
    except Exception as e:
        print("Exception", e)
        return []
    finally:
        if mydb is not None:
            cur.close()
            mydb.close()


def get_articles(source, dateFrom, dateTo):
    # mydb = DBConnection().mydb

    source_query = ""
    date_query = ""

    base_query = "SELECT * from news_articles WHERE source IS NOT NULL"

    if source is not None:
        source_query = " AND source = '{source}'". format(source=source)
    
    if dateFrom is not None:
        if dateTo is None:
            dateTo = date.today()

        date_query = " AND publish_date between '{dateFrom}' and '{dateTo}'".format(dateFrom=dateFrom, dateTo=dateTo)

    query = "{base_query} {source_query} {date_query} ORDER BY publish_date DESC LIMIT 30".format(base_query=base_query, source_query=source_query, date_query=date_query)
       
    mydb = None
    cur = None
    try:
        mydb = postgres_connect()
        cur = mydb.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cur.execute(query)
        rows = cur.fetchall()
        resp = rows
        return resp
    except Exception as e:
        print("Exception", e)
        return []
    finally:
        if mydb is not None:
            cur.close()
            mydb.close()



def search_articles(qs):

    base_query = "SELECT * from news_articles WHERE title ~* '\y{qs}\y'  ORDER BY publish_date DESC LIMIT 30".format(qs=qs)

    # base_query = "SELECT * from news_articles WHERE strpos('{sq}', title) > 0  OR strpos('{sq}', content) > 0  ORDER BY publish_date DESC LIMIT 30".format(qs=qs)
    
      
    mydb = None
    cur = None
    try:
        mydb = postgres_connect()
        cur = mydb.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cur.execute(base_query)
        rows = cur.fetchall()
        resp = rows
        return resp
    except Exception as e:
        print("Exception", e)
        return []
    finally:
        if mydb is not None:
            cur.close()
            mydb.close()