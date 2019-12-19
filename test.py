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


cursor.execute("SELECT username FROM `users`")
num_of_users = cursor.rowcount
rows, cols = (num_of_users, 3) 
arr = [[]*cols]*rows 
print(arr) 
userlist = list(cursor)

i = 0
while i < num_of_users :
    arr.append(userlist[i])
    i = i+1

[x[0][:x[0].index('(')] for x in userlist]

print(num_of_users)
print(userlist)
print(arr)