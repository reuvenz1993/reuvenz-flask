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
import numpy as np

myDB = MySQLdb.connect(host="mysql.stackcp.com",port=53856,user="usersdb-3131357d30",passwd="usersdb-3131357d30",db="usersdb-3131357d30" , charset='utf8')
cursor=myDB.cursor()
logged_in = 'reuven'
user1 = logged_in
user2 = "maria"
cursor.execute("SELECT * FROM `massages` WHERE ( sender='{}' AND receiver='{}' ) OR ( sender='{}' AND  receiver='{}'  ) ORDER BY `time` DESC".format(user1, user2 ,user2 , user1))
temp = list( cursor.fetchall() )

for i in range ( len(temp) ):
    temp[i] = list(temp[i])
    temp[i][4] = str(temp[i][4])


print (temp)

print (temp)