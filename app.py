from flask import Flask, render_template , request
from flaskext.mysql import MySQL
import MySQLdb
from flask_mysqldb import MySQL
import pymysql
import mysql.connector
import pymysql.cursors
import MySQLdb
from MySQLdb import _mysql

myDB = MySQLdb.connect(host="ec2-46-137-91-216.eu-west-1.compute.amazonaws.com",port=5432,user="afstpratzpjdte",passwd="8fc13500ad53ae2dc352fc5adf02911a3c40b53aef1ebb02d05c39c7628b870a",db="d62fast5jf6n7u")

#db=_mysql.connect(host="outhouse",port=5432,passwd="8fc13500ad53ae2dc352fc5adf02911a3c40b53aef1ebb02d05c39c7628b870a",db="d62fast5jf6n7u")

#db=_mysql.connect(host="shareddb-p.hosting.stackcp.net:3306",user="usersdb-3131357d30",
#                  passwd="usersdb-3131357d30",db="usersdb-3131357d30")

app=Flask(__name__)
app.config['TESTING'] = True


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
    
