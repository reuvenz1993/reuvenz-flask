from flask import Flask, render_template , request
from flaskext.mysql import MySQL
import MySQLdb
from flask_mysqldb import MySQL
import pymysql
import mysql.connector
import pymysql.cursors

app=Flask(__name__)
app.config['TESTING'] = True



from flaskext.mysql import MySQL
import mysql.connector
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('shareddb-p.hosting.stackcp.net'),
    ssh_username='engramar', ssh_password='usersdb-3131357d30',
    remote_bind_address=('shareddb-p.hosting.stackcp.net', 3306)
) as tunnel:
    connection = mysql.connector.connect(
        user='usersdb-3131357d30', password='usersdb-3131357d30',
        host='127.0.0.1', port=tunnel.local_bind_port,
        database='usersdb-3131357d30',
    )

print('after SSH connection')

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'engramar'
app.config['MYSQL_DATABASE_PASSWORD'] = '<password>'
app.config['MYSQL_DATABASE_DB'] = 'engramar$default'
app.config['MYSQL_DATABASE_HOST'] = 'engramar.mysql.pythonanywhere-services.com'
mysql.init_app(app)

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
    
