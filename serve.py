from flask import Flask, jsonify, flash, redirect, render_template, url_for, request
from nairametrics_parser import Nairametrics
from punch_parser import PunchNG

from apscheduler.schedulers.background import BackgroundScheduler
# from db_config import mysql
import pymysql

from datetime import date, datetime

app = Flask(__name__)

def update_news():
    ar = Nairametrics()
    punch = PunchNG()

    print("News Updated: ", datetime.now())

sched = BackgroundScheduler(daemon=True)
sched.add_job(update_news,'interval',minutes=120)
sched.start()

@app.route('/fetch-news')
def get_news():
    print("Getting news....")
    ar = Nairametrics()
    punch = PunchNG()

    return "We are done"

@app.route('/')
def home():
    
    return render_template('index.html')


@app.route('/articles', methods=['GET'])
def get_articles():
    
    from db_helper import get_article_data
    resp = get_article_data()

    return jsonify(resp)



@app.route('/articles/', methods=['GET'])
def get_m_articles():

    source = request.args.get('source')
    dateFrom = request.args.get('from')
    dateTo = request.args.get('to')
    
    from db_helper import get_articles
    resp = get_articles(source, dateFrom, dateTo)

    return jsonify(resp)

@app.route('/articles/sources', methods=['GET'])
def get_sources():
    
    from db_helper import get_sources
    resp = get_sources()

    return jsonify(resp)

if __name__ == '__main__':
    app.run()


