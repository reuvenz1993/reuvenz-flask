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

n = len(temp)
a = [[0] * 3 for i in range(n)]
print (a)

for i in range (n):
    username = str(temp[i])
    username = username [2:-3]
    a[i][0] = username

print (a)
print ("ss")
print ("ss")
print (a)