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

cursor.execute("SELECT DISTINCT username FROM `users`")
temp = cursor.fetchall()
temp = list(temp)

SYMBOLS = '{}()[].,:;+-*/&|<>=~'

num_rows = len(temp)
print (temp[5])

n = num_rows
m = 3
a = [[0] * m for i in range(n)]
print (a)

for i in range (num_rows):
    a[i][0] = str(temp[i])
    a[i][0] = a[i][0][2:-3]
    


print (temp)
print (num_rows)
print (a)