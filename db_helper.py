from flask import Flask, jsonify, flash, redirect, render_template, url_for
from nairametrics_parser import Nairametrics
from punch_parser import PunchNG
from db_config import mydb
from datetime import date
import pymysql




def get_sources():
    try:
        
        cur = mydb.cursor(dictionary=True)
        cur.execute("SELECT DISTINCT(source) from news_articles")
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print("Exception", e)

def get_article_data():

    try:
        cur = mydb.cursor(dictionary=True)
        cur.execute("SELECT * from news_articles")
        rows = cur.fetchall()
        resp = rows
        return resp
    except Exception as e:
        print("Exception", e)
        return []


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

    query = "{base_query} {source_query} {date_query} ORDER BY publish_date DESC".format(base_query=base_query, source_query=source_query, date_query=date_query)
       

    try:
        cur = mydb.cursor(dictionary=True)
        cur.execute(query)
        rows = cur.fetchall()
        resp = rows
        return resp
    except Exception as e:
        print("Exception", e)
        return []