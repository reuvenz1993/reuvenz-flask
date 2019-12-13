from flask import Flask, render_template , request , session
from flaskext.mysql import MySQL
import MySQLdb
from flask_mysqldb import MySQL
import pymysql
import mysql.connector
import pymysql.cursors
import MySQLdb
from MySQLdb import _mysql
import json
from twisted.web.server import Session
from flask_login import LoginManager

myDB = MySQLdb.connect(host="mysql.stackcp.com",port=53856,user="usersdb-3131357d30",passwd="usersdb-3131357d30",db="usersdb-3131357d30" , charset='utf8')
cursor=myDB.cursor()

#cursor.execute("SELECT * FROM `users`")


app=Flask(__name__)
app.config['TESTING'] = True

login_manager = LoginManager()



@app.route('/' , methods =['GET','POST'])
def home():
    if ( session['username'] != "" ) :
        return render_template("main.html")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print ("username is :" + username)
        print ("password is :" + password)
        cursor.execute("SELECT `username` ,`password` FROM `users` WHERE `username`=" +"'" + username +"'")
        res = cursor.fetchone()
        if ( res and res[1] == password ):
            return render_template("home.html" , res = res , status = "connaction scss")
        elif ( res ) :
            return render_template("home.html" , res = res , status = "username correct but password isnt")
        else :
            return render_template("home.html" , res = res , status = "no such username")

        
    return render_template("home.html" )

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/main/')
def main():
    return render_template("main.html")

if __name__=="__main__":
    app.run(debug=True)
    
