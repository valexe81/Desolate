from app import app #same as in runner file thing
from flask import render_template,redirect,url_for



@app.route('/') 
@app.route('/index')
def frontpage(): #written the same as telling an instance to do smth bc telling an instance to do smth is written as a function
    return render_template('mainpage.html') 


#return = output of function






