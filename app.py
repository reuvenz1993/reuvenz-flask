from flask import Flask, render_template , request , session , redirect , url_for , escape , make_response
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
from sqlalchemy.dialects.mysql import mysqlconnector
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+mysqlconnector://usersdb-3131357d30:usersdb-3131357d30@mysql.stackcp.com:53856/usersdb-3131357d30")


myDB = MySQLdb.connect(host="mysql.stackcp.com",port=53856,user="usersdb-3131357d30",passwd="usersdb-3131357d30",db="usersdb-3131357d30" , charset='utf8')
cursor=myDB.cursor()

#cursor.execute("SELECT * FROM `users`")


app=Flask(__name__)
app.config['TESTING'] = True
app.secret_key = "fghfghfdgsdfhfhfghdfgrebdfbver"

login_manager = LoginManager()



@app.route('/' , methods =['GET','POST'])
def index():
    if 'username' in session:
        username = session['username']
        return redirect(url_for('main'))

    if ( request.method == 'POST' and request.form['signup'] == '0' ):
        print (request.form['signup'])
        username = request.form['username']
        password = request.form['password']
        print ("username is :" + username)
        print ("password is :" + password)
        cursor.execute("SELECT `username` ,`password` FROM `users` WHERE `username`=" +"'" + username +"'")
        res = cursor.fetchone()
        if ( res and res[1] == password ):
            session['username'] = username
            return redirect(url_for('main'))
        elif ( res ) :
            return render_template("index.html" , res = res , status = "username correct but password isnt")
        else :
            return render_template("index.html" , res = res , status = "no such username")

    if ( request.method == 'POST' and request.form['signup'] == '1' ):
        cont = True
        error =""
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor.execute ("SELECT COUNT(*) FROM `users` WHERE `username`=" +"'" + username +"'")
        username_check = cursor.fetchone()[0]
        if username_check > 0 :
            cont = False
            error += "Username is not free, try an other user name <br>"
        print (username_check )
        
        cursor.execute ("SELECT COUNT(*) FROM `users` WHERE `email`=" +"'" + email +"'")
        email_check = cursor.fetchone()[0]
        if  email_check > 0 :
            cont = False
            error += "Email is not free, try an other user name <br>"
        print (email_check )
        if ( cont ):
            sql = "INSERT INTO `users` ( `username` ,`password` , `email`) VALUES (%s, %s, %s)"
            val = ( username , password ,  email )
            cursor.execute(sql, val)
            myDB.commit()
            print ("can insert")
        
        

    return render_template("index.html" )

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/main/')
def main():
    if 'username' in session:
        username = session['username']
        print ( username )
        return render_template("main.html" , username = username)
    else:
        return redirect(url_for('index'))


@app.route('/whatsapp/')
def whatsapp():
    if 'username' in session:
        username = session['username']
        print ( username )
        return render_template("whatsapp.html" , username = (username) )
    else:
        return redirect(url_for('index'))
    

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)
    
