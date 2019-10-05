from flask import Flask, jsonify, flash, redirect, render_template, url_for
from nairametrics_parser import Nairametrics
from punch_parser import PunchNG
from db_config import mysql
import pymysql

app = Flask(__name__)

@app.route('/fetch-news')
def get_news():
    print("Getting news....")
    # ar = Nairametrics()
    punch = PunchNG()

    return "We are done"

@app.route('/')
def home():
    
    return render_template('index.html')


@app.route('/articles')
def get_articles():
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * from news_articles")
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print("Exception", e)

@app.route('/articles/sources')
def get_sources():
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT DISTINCT(source) from news_articles")
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print("Exception", e)

if __name__ == '__main__':
    app.run()


