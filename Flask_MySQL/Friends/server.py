import hashlib # do this at the top of your file where you import modules
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    #print(friends)
    #friends={'first_name':'huy'}
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    first_name= request.form['first_name']
    last_name= request.form['last_name']
    email = request.form['email']
    password = hashlib.md5(request.form['password'].encode()).hexdigest()
    insert_query = "INSERT INTO friends ( first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    query_data = {'first_name': first_name, 'email': email, 'last_name': last_name,'password': password}
    mysql.query_db(insert_query, query_data)
    # add a friend to the database
    return redirect('/')
app.run(debug=True)