
import mysql.connector

from serve import app
from flaskext.mysql import MySQL
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'cnews_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "password",
#     database = "cnews_db"

#     )

# class DBConnection:

#     mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "password",
#     database = "cnews_db"

#     )