# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:41:00 2020

@author: arijit, preetham
"""

'''from flask_mysqldb import MySQL

from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,Required
from wtforms.ext.sqlalchemy.fields import QuerySelectField
'''
from datetime import datetime
from flask import Flask,render_template,url_for,flash,redirect,request,jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'aaiyer'
app.config['MYSQL_PASSWORD'] = 'abc123'
app.config['MYSQL_DB'] = 'sbu_fhr'

mysql = MySQL(app)
#db = SQLAlchemy(app)


@app.route('/',methods=['GET', 'POST'])
def index():
    tableName = 'labevents'
    if request.method == 'POST':
        #keyWord = request.form['keyword']
        data = request.json
        #colValue = data[2]
        cur = mysql.connection.cursor()
        #t = (colValue,)
        ##new code
        
        i = 0
        str1 = 'SELECT * FROM labevents where '
        str = ''
        while(i<len(data)):
            str3 = "'"+ data[i+2] + "'"
            str = str + data[i] + ' ' + data[i+1] + ' ' + str3 + ' ' + data[i+3]+ ' ' 
            i = i+5
        final = str1+str + ' limit 10'
        cur.execute(final)
        ##new code ends
        
        #cur.execute('SELECT value,valuenum FROM labevents where valuenum = %s limit 10', t) 
        results = cur.fetchall()
        mysql.connection.commit()
        cur.close()        
        
        empList = []
        for emp in results:
            empDict = {
                'ROW_ID': emp[0],
                'PERSON_ID': emp[1],
                'ENCOUNTER_ID': emp[2],
                'CONTRIBUTOR_SYSTEM': emp[3],
                'CHARTTIME': emp[4],
                'VALUE': emp[5],
                'VALUENUM': emp[6],
                'VALUEUOM': emp[7],
                'NORMAL_LOW': emp[8],
                'NORMAL_HIGH': emp[9],
                'FLAG': emp[10]}
            empList.append(empDict)
        return jsonify(empList)

    return render_template('home.html')
    
    
@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        data = request.args.get['host']
        print(data)
        return render_template('about.html',data=data)
    return render_template('about.html')
#"Rubella IgG Ab"


if __name__ == '__main__':
    app.run()
    #aaiyer
    #abc123/stony