from flask import Flask, render_template , request
from flaskext.mysql import MySQL
import MySQLdb
from flask_mysqldb import MySQL
import pymysql
import mysql.connector
import pymysql.cursors

app=Flask(__name__)
app.config['TESTING'] = True



connection = pymysql.connect(host='http://ec2-46-137-91-216.eu-west-1.compute.amazonaws.com/',
                             port=5432,
                             user='afstpratzpjdte',
                             password='8fc13500ad53ae2dc352fc5adf02911a3c40b53aef1ebb02d05c39c7628b870a',
                             db='d62fast5jf6n7u',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print(connection)



mysql = MySQL()

print('after app.config')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'todo'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MYSQL
mysql = MySQL(app)

@app.route('/' , methods =['GET','POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print ("username is :" + username)
        print ("password is :" + password)
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
    
