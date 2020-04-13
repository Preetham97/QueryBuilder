# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:41:00 2020

@author: aaiyer
"""

from flask_mysqldb import MySQL
from datetime import datetime
from flask import Flask,render_template,url_for,flash,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,Required
from wtforms.ext.sqlalchemy.fields import QuerySelectField
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'aaiyer'
app.config['MYSQL_PASSWORD'] = 'abc123'
app.config['MYSQL_DB'] = 'sbu_fhr'

mysql = MySQL(app)
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstCol = details['col1']
        firstColValue = details['fname']
        firstColEq = details['equal1']
        secondCol = details['col2']
        secondColValue = details['lname']
        secondColEq = details['equal2']
        
        operator = details['operation1']

        cur = mysql.connection.cursor()
        
        
        query_string = ("SELECT * FROM labevents where %(tab)s= %(col1)s limit 10")
        print(query_string)
        #%s labevents.%s "+secondColEq+" %s limit 10"
        cur.execute(query_string,{'tab':firstCol,'col1':firstColValue})
                                  #,operator,secondCol,secondColValue))
        data = cur.fetchall()
        table = Results(data)
        table.border = True
        mysql.connection.commit()
        cur.close()
        return render_template('registration.html', data = data)
    return render_template('registration.html',title ='Register')
#"Rubella IgG Ab"


def enabled_categories():
    cur = mysql.connection.cursor()
    cur.execute("SELECT distinct(labitem_description) FROM dt_labitems")
    data = cur.fetchall()
    table = Results(data)
    table.border = True 
    mysql.connection.commit()
    cur.close()
    return data

class RegistrationForm(FlaskForm):
    username = StringField('Value', 
                           validators=[DataRequired(),Length(min = 2, max = 20)])
    email = StringField('ValueNum',
                        validators=[DataRequired()])
    #client_id = QuerySelectField(query_factory=enabled_categories, allow_blank=True)
    #password = PasswordField('Password',
                             #validators=[DataRequired()])
    #confirmPassword = PasswordField('Confirm Password',
                                    #validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Search for Values')


class Results(Table):
    ROW_ID = Col('ROW_ID')
    PERSON_ID = Col('PERSON_ID')
    ENCOUNTER_ID = Col('ENCOUNTER_ID')
    CONTRIBUTOR_SYSTEM = Col('CONTRIBUTOR_SYSTEM')
    CHARTTIME = Col('CHARTTIME')
    VALUE = Col('VALUE')
    VALUENUM = Col('VALUENUM')
    VALUEUOM = Col('VALUEUOM')
    NORMAL_LOW = Col('NORMAL_LOW')
    NORMAL_HIGH = Col('NORMAL_HIGH')
    FLAG = Col('FLAG')
    ITEM_ID = Col('ITEM_ID')
    VALUENUM_DECIMAL = Col('VALUENUM_DECIMAL')



if __name__ == '__main__':
    app.run()
    
    #aaiyer
    #abc123/stony