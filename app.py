from flask import Flask, render_template , request
from flaskext.mysql import MySQL

app=Flask(__name__)

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
    
