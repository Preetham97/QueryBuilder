import ast

from flask import Flask
from flask import render_template, request

from werkzeug.wrappers import Response
import json

import pgConnect

from plotting_script import final

import dash
import dash_core_components as dcc
import dash_html_components as html

import random
import webbrowser



app = Flask(__name__)

data_result = None

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/patientRecords')
def patinetRecords():
    return render_template('patientRecords.html')

@app.route('/patientID_select',methods=['GET', 'POST'])
def patientID_select():
    para = request.get_json()
    print("patientId",para)

    with open('arguments.txt', 'r') as f:
        args = ''
        for line in f.readlines():
            line = line.strip()
            args += line
        f.close()

    args = "".join(args).strip('\n')
    args_dict = ast.literal_eval(args)

    schema = args_dict['schema']
    db = pgConnect.db(schema)

    data_json = db.getLabData(para, database=args_dict['database'], user=args_dict['user'],
                            password=args_dict['password'], host=args_dict['host'], port=args_dict['port'])

    return data_json

@app.route('/queryBuilder')
def queryBuilder():
    return render_template('index.html')

@app.route('/auth', methods=['GET', 'POST'])
def authenticate():
    registry = {'admin': 'admin', 'paul': 'paul'}
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['name']
        passw = request.form['pass']
        if name in registry.keys() and passw == registry[name]:
            return render_template('index.html')
        else:
            return render_template('fail.html')
        
@app.route("/logout", methods = ["GET", "POST"])
def logout():
    # logout_user()
    return render_template("login.html")

@app.route('/getQueryResults', methods=('GET', 'POST'))
def getQueryResults():
    rules_json = request.get_json()
    #print("getQueryResults Json", rules_json)

    with open('arguments.txt', 'r') as f:
        args = ''
        for line in f.readlines():
            line = line.strip()
            args += line
        f.close()

    args = "".join(args).strip('\n')
    args_dict = ast.literal_eval(args)

    schema = args_dict['schema']
    db = pgConnect.db(schema)

    data_json = db.get_data(rules_json, database=args_dict['database'], user=args_dict['user'],
                            password=args_dict['password'], host=args_dict['host'], port=args_dict['port'])

    global data_result
    data_result = json.loads(data_json)["data_json"]

    return data_json

@app.route('/saveQuery', methods=('GET', 'POST'))
def saveQuery():
    saveQueryJson = request.get_json()

    with open('arguments.txt', 'r') as f:
        args = ''
        for line in f.readlines():
            line = line.strip()
            args += line
        f.close()

    args = "".join(args).strip('\n')
    args_dict = ast.literal_eval(args)

    schema = args_dict['schema']
    db = pgConnect.db(schema)

    saveQueryResponseJson = db.saveQuery(saveQueryJson, database=args_dict['database'], user=args_dict['user'],
                            password=args_dict['password'], host=args_dict['host'], port=args_dict['port'])


    return saveQueryResponseJson

@app.route('/selectQuery', methods=('GET', 'POST'))
def selectQuery():
    # saveQueryJson = request.get_json()

    with open('arguments.txt', 'r') as f:
        args = ''
        for line in f.readlines():
            line = line.strip()
            args += line
        f.close()

    args = "".join(args).strip('\n')
    args_dict = ast.literal_eval(args)

    schema = args_dict['schema']
    db = pgConnect.db(schema)

    selectQueryResponseJson = db.selectQuery(database=args_dict['database'], user=args_dict['user'],
                            password=args_dict['password'], host=args_dict['host'], port=args_dict['port'])

    # print("selectQueryResponseJson",selectQueryResponseJson)

    return selectQueryResponseJson

@app.route('/launcPlottingTool', methods=('GET', 'POST'))
def launcPlottingTool():
    #return render_template("login.html")
    #print("Hello World")
    requestJson = request.get_json()
    #print(requestJson)
    #print("First line....")
    #return render_template('fail.html')
    try:
        #print("thrid line....")
        subjectId = requestJson["person_id"]
        encounterId = requestJson["encntr_id"]
        random_number = random.randint(0,9999)
        final(subjectId,encounterId,app,random_number)
        url = '/dashplot/'+str(subjectId)+str(random_number)+'/'
        subId = str(subjectId)
        randomNum = str(random_number)
        #webbrowser.open_new_tab('http://127.0.0.1:5000/'+url)
        finalUrl = 'http://127.0.0.1:5000/'+url

        #mystr = 'http://127.0.0.1:5000/'+url

        #print("refreshing??")
        #redirect(mystr)
        return json.dumps([{"result": "success","subId":subId,"randomNum":randomNum}])
        #return render_template('fail.html')
        #return render_template('plot.html')
    except:
        return '{"result":"failure"}'

@app.route("/download", methods = ["GET", "POST"])
def download():
    csv_result = ''
    data = json.loads(data_result)

    for key in data[0].keys():
        csv_result = csv_result + key + ','
    csv_result = csv_result[:-1] + '\n'

    for row in data:
        for value in row.values():
            value = value.replace(',',' ')
            csv_result = csv_result + value + ','
        csv_result = csv_result[:-1] + '\n'

    response = Response(csv_result)
    response.headers['Content-Disposition'] = 'attachment; filename=result.csv'
    response.mimetype = 'text/csv'

    return response

@app.route('/searchDt', methods=('GET', 'POST'))
def searchDt():
    dataSource = request.get_json()
    researchValue = dataSource['keywords']
    rules = dataSource['rules']
    search_fields = dataSource['searchfield']

    with open('arguments.txt', 'r') as f:
        args = ''
        for line in f.readlines():
            line = line.strip()
            args += line
        f.close()

    args = "".join(args).strip('\n')
    args_dict = ast.literal_eval(args)

    schema = args_dict['schema']
    db = pgConnect.db(schema)

    set_rules = db.search(search_fields, researchValue, rules,database=args_dict['database'], user=args_dict['user'],
                              password=args_dict['password'], host=args_dict['host'], port=args_dict['port'])

    return set_rules

@app.route('/get_search_rules', methods=('GET', 'POST'))
def get_search_rules():
    dataSource = request.get_json()
    fields = dataSource['fields']
    is_search_fields = dataSource['searchfield']
    rules = dataSource['rules']

    with open('arguments.txt', 'r') as f:
        args = ''
        for line in f.readlines():
            line = line.strip()
            args += line
        f.close()

    args = "".join(args).strip('\n')
    args_dict = ast.literal_eval(args)

    schema = args_dict['schema']
    db = pgConnect.db(schema)

    set_rules = db.rule_setter(is_search_fields, fields, rules)

    return set_rules


@app.route('/id_group_by_date',methods=['GET', 'POST'])
def id_group_by_date():
    para = request.get_json()
    print("datepara",para)

    with open('arguments.txt', 'r') as f:
        args = ''
        for line in f.readlines():
            line = line.strip()
            args += line
        f.close()

    args = "".join(args).strip('\n')
    args_dict = ast.literal_eval(args)

    schema = args_dict['schema']
    db = pgConnect.db(schema)

    data_json = db.getId(para, database=args_dict['database'], user=args_dict['user'],
                            password=args_dict['password'], host=args_dict['host'], port=args_dict['port'])

    return data_json

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run(debug=True)
