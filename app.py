from flask import Flask, render_template , request
from flaskext.mysql import MySQL
import MySQLdb
from flask_mysqldb import MySQL
import pymysql
import mysql.connector
import pymysql.cursors
import MySQLdb
import pymssql

server = "http://ec2-46-137-91-216.eu-west-1.compute.amazonaws.com"
user = "afstpratzpjdte"
password = "8fc13500ad53ae2dc352fc5adf02911a3c40b53aef1ebb02d05c39c7628b870a"
database = "d62fast5jf6n7u"



conn = pymssql.connect(server=server, user=user, password=password, database=db)
cursor = conn.cursor()


app=Flask(__name__)
app.config['TESTING'] = True

mydb = mysql.connector.connect(
  host="http://ec2-46-137-91-216.eu-west-1.compute.amazonaws.com",
  user="afstpratzpjdte",
  passwd="8fc13500ad53ae2dc352fc5adf02911a3c40b53aef1ebb02d05c39c7628b870a",
  database="d62fast5jf6n7u"
)

print(mydb)


conn = MySQLdb.connect('http://ec2-46-137-91-216.eu-west-1.compute.amazonaws.com', 'afstpratzpjdte', '8fc13500ad53ae2dc352fc5adf02911a3c40b53aef1ebb02d05c39c7628b870a', 'd62fast5jf6n7u')

def mysqlconnect(): 
    #Trying to connect  
    try: 
        db_connection= MySQLdb.connect 
        ("http://ec2-46-137-91-216.eu-west-1.compute.amazonaws.com","afstpratzpjdte","8fc13500ad53ae2dc352fc5adf02911a3c40b53aef1ebb02d05c39c7628b870a","d62fast5jf6n7u") 
    # If connection is not successful 
    except: 
        print("Can't connect to database") 
        return 0
    # If Connection Is Successful 
    print("Connected") 
  
    # Making Cursor Object For Query Execution 
    cursor=db_connection.cursor() 
  
    # Executing Query 
    cursor.execute("SELECT CURDATE();") 
  
    # Above Query Gives Us The Current Date 
    # Fetching Data  
    m = cursor.fetchone() 
  
    # Printing Result Of Above 
    print("Today's Date Is ",m[0]) 
  
    # Closing Database Connection  
    db_connection.close() 
  
# Function Call For Connecting To Our Database 
mysqlconnect() 


connection = pymysql.connect(host='http://ec2-46-137-91-216.eu-west-1.compute.amazonaws.com',
                             port=5432,
                             user='afstpratzpjdte',
                             password='8fc13500ad53ae2dc352fc5adf02911a3c40b53aef1ebb02d05c39c7628b870a',
                             db='d62fast5jf6n7u',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print(connection)

a = MySQLdb.connect()

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
    
