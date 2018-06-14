from flask import Flask
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'twitter')
print (mysql.query_db("SELECT * FROM users"))
print(mysql.query_db("SELECT * FROM users WHEN "))
app.run(debug=True)
