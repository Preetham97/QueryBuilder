# import mysql.connector
import collections
# import matplotlib.pyplot as plt
import sys
import datetime
import numpy as np
import os
import glob
import pandas as pd
import csv
import time
import psycopg2
import webbrowser


aa=0
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="aaiyer",
#   passwd="abc123",
#   database="sbu_fhr"
# )
#print("You are connected to - ", record,"\n")
# x = sys.argv[1]
# y = sys.argv[2]
# aa = sys.argv[3:]
# if aa:
#     aa = aa[0]
# else:
#     aa = 0
# print('here',x, y,aa)

# "database":"fhr",
# "user":"postgres",
# "password":"sagar",
# "host":"127.0.0.1",
# "port":"5432",
# "schema":"sbufhr"
    


def zero_to_nannew(values):
    list1 = []
    for i, j in values:
        if i == 0:
            list1.append((float('nan'), j))
        else:
            list1.append((i, j))
    return list1




def combine(patientID, encid):

    root_dir = os.getcwd()

    print("Inside combine method")

    camm_name = camname(patientID,encid)

    print("Outside combine method")

    #sub_list = [i[1] for i in os.walk(root_dir)]
    #print(sub_list)
    #for dirName, subdirList, fileList in os.walk(root_dir):
        
        #print('preethzzz', subdirList)
    #print(root_dir)
    merged_file = os.path.join(root_dir, patientID, str(camm_name))
    #merged_file = os.path.join(root_dir, patientID, str(camm_name))
    print(merged_file)
    return merged_file


def camname(pid,enid):
    print("Trying to connec to database from plotting script")
    # connection = psycopg2.connect(user = "postgres",
    #                               password = "preetham",
    #                               host = "127.0.0.1",
    #                               port = "5432",
    #                               database = "fhr",
    #                               schema = "sbufhr")
    # cursor = connection.cursor()


    connection = psycopg2.connect(database="fhr", user="postgres", password="preetham", host="127.0.0.1", port="5432")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(),"\n")
    print("connected")
    # Print PostgreSQL version
    #cursor.execute("Select fhr_signals.camm_file_name from sbufhr.fhr_signals where fhr_signals.person_id = x and fhr_signals.encntr_id = 48116001")
    cursor.execute("Select fhr_signals.camm_file_name from sbufhr.fhr_signals where fhr_signals.person_id = %s and fhr_signals.encntr_id = %s", (pid,enid))
    record = cursor.fetchall()
    print(record)
    connection.commit()
    cursor.close()
    connection.close()
    print("my recodr")
    print(record[0][0])
    return record[0][0]


def final(patientID, encid, server, random_number):
    #cam_name = camname(patientID, encid)

    print("im in the final")

    import plotly.offline as pyo
    import plotly.graph_objs as go
    import plotly as py
    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    import dash_bootstrap_components as dbc
    from dash.dependencies import Input, Output, State
    #app = dash.Dash()

    
    url = '/dashplot/'+str(patientID)+str(random_number)+'/'
    app  = dash.Dash(__name__, server = server, url_base_pathname=url)

    #webbrowser.open_new_tab('http://127.0.0.1:5000/'+url)

    #dbc.Spinner(size = "sm", color = "success", type="border", fullscreen = "True")

   
    #cam_name = encid
    #print(cam_name)
    print("Entering Combine")
    merged_file = combine(patientID, encid)
    fhr0 = []
    fhr1 = []
    fhr2 = []
    fhr3 = []
    fhr_avg = []
    mhr0 = []
    mhr1 = []
    mhr2 = []
    mhr3 = []
    mhr_avg = []
    toco0 = []
    toco1 = []
    toco2 = []
    toco3 = []
    toco_avg = []
    with open(merged_file, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        # Start reading from the second row in CSV to leave out column names
        header = next(plots)
        # Get Acquired Time
        # timestamp_list = [datetime.datetime.strptime(str(row[1][:-4])
        #                  ,"%Y-%m-%d::%H:%M:%S") for row in plots]
        timestamp_list = [datetime.datetime.strptime(str(row[1])
                                                     , "%Y-%m-%d::%H:%M:%S.%f") for row in plots]
    # print(timestamp_list)
    timestamp_list.reverse()
    with open(merged_file, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        header = next(plots)
        counter = 0
        # Collect the four FHR samples in different lists
        for d, t in zip(plots, timestamp_list):
            counter += 1

            # get C1 HRO
            hr1_0 = int(float(d[3]))

            # get C1 HR1
            hr1_1 = int(float(d[4]))

            # get C1 HR2
            hr1_2 = int(float(d[5]))

            # get C1 HR3
            hr1_3 = int(float(d[6]))
            # get MHR 0
            mhr1_0 = int(float(d[11]))

            # get MHR 1
            mhr1_1 = int(float(d[12]))

            # get MHR 2
            mhr1_2 = int(float(d[13]))

            # get MHR 3
            mhr1_3 = int(float(d[14]))
            # get TOCO 0
            toco_0 = int(float(d[15]))

            # get TOCO 1
            toco_1 = int(float(d[16]))

            # get TOCO 2
            toco_2 = int(float(d[17]))

            # get TOCO 3
            toco_3 = int(float(d[18]))
            time1 = t + datetime.timedelta(milliseconds=250)
            time2 = t + datetime.timedelta(milliseconds=500)
            time3 = t + datetime.timedelta(milliseconds=750)

            toco3.append((toco_3, time3))
            toco2.append((toco_2, time2))
            toco1.append((toco_1, time1))
            toco0.append((toco_0, t))
            toco_avg.append((toco_0 + toco_1 + toco_2 + toco_3) // 4)

            mhr3.append((mhr1_3, time3))
            mhr2.append((mhr1_2, time2))
            mhr1.append((mhr1_1, time1))
            mhr0.append((mhr1_0, t))
            mhr_avg.append((mhr1_0 + mhr1_1 + mhr1_2 + mhr1_3) // 4)

            fhr3.append((hr1_3, time3))
            fhr2.append((hr1_2, time2))
            fhr1.append((hr1_1, time1))
            fhr0.append((hr1_0, t))
            
            fhr_avg.append((hr1_0 + hr1_1 + hr1_2 + hr1_3) // 4)

    fhr0 = np.array(zero_to_nannew(fhr0))
    fhr1 = np.array(zero_to_nannew(fhr1))
    fhr2 = np.array(zero_to_nannew(fhr2))
    fhr3 = np.array(zero_to_nannew(fhr3))
    # fhr_avg = np.array(zero_to_nan(fhr_avg))
    mhr0 = np.array(zero_to_nannew(mhr0))
    mhr1 = np.array(zero_to_nannew(mhr1))
    mhr2 = np.array(zero_to_nannew(mhr2))
    mhr3 = np.array(zero_to_nannew(mhr3))
    # mhr_avg = np.array(zero_to_nannew(mhr_avg))
    toco0 = np.array(zero_to_nannew(toco0))
    toco1 = np.array(zero_to_nannew(toco1))
    toco2 = np.array(zero_to_nannew(toco2))
    toco3 = np.array(zero_to_nannew(toco3))
    # toco_avg=np.array(zero_to_nannew(toco_avg))

    listx = []
    listy = []
    for i, j, k, l in zip(fhr0, fhr1, fhr2, fhr3):
        listx.append(l[1])
        listx.append(k[1])
        listx.append(j[1])
        listx.append(i[1])
        listy.append(l[0])
        listy.append(k[0])
        listy.append(j[0])
        listy.append(i[0])
    listx1 = []
    listy1 = []
    for i, j, k, l in zip(mhr0, mhr1, mhr2, mhr3):
        listx1.append(l[1])
        listx1.append(k[1])
        listx1.append(j[1])
        listx1.append(i[1])
        listy1.append(l[0])
        listy1.append(k[0])
        listy1.append(j[0])
        listy1.append(i[0])
    listx2 = []
    listy2 = []
    for i, j, k, l in zip(toco0, toco1, toco2, toco3):
        listx2.append(l[1])
        listx2.append(k[1])
        listx2.append(j[1])
        listx2.append(i[1])
        listy2.append(l[0])
        listy2.append(k[0])
        listy2.append(j[0])
        listy2.append(i[0])

    timestamp_list = np.array(timestamp_list)
    # print(timestamp_list[0],timestamp_list[-1])
    from plotly.subplots import make_subplots

    import plotly.graph_objects as go
    print(counter, "number of sessions")
    firsttime = listx[len(listx) // 2]
    nexttime = firsttime + datetime.timedelta(minutes=5)
    nexttimesec = firsttime + datetime.timedelta(seconds=10)
    diff = int(((nexttime - firsttime).total_seconds()) // 10)
    list_x = [(listx[0] - i).total_seconds() for i in listx]
    list_x1 = [(listx1[0] - i).total_seconds() for i in listx1]
    list_x2 = [(listx2[0] - i).total_seconds() for i in listx2]
    # aa=int(aa)
    print(len(list_x), "-----", counter)
    if aa:
        print(aa)
        list_x = list_x[:int(aa) * 4]
        list_x1 = list_x1[:int(aa) * 4]
        list_x2 = list_x2[:int(aa) * 4]
        listy = listy[:int(aa) * 4]
        listy1 = listy1[:int(aa) * 4]
        listy2 = listy2[:int(aa) * 4]
    print(len(list_x), "-----", counter)
    # print(list_x)
    ft = listx[0]
    newlist = [(ft + datetime.timedelta(seconds=i + 10)).strftime('%B') for i in list_x]
    print(len(newlist), len(list_x), newlist[0])
    print(ft)

    d1 = datetime.datetime.strptime(str(listx[0]), '%Y-%m-%d %H:%M:%S.%f')
    d2 = datetime.datetime.strptime(str(listx[-1]), '%Y-%m-%d %H:%M:%S.%f')
    print(d1, d2)
    timer = (d1 - d2).total_seconds()
    t = 0
    new1 = []
    new2 = [i for i in range(0, int(timer), 300)]
    while t < timer:
        t += 60
        new1.append(str(ft))
        ft = (ft - datetime.timedelta(seconds=300))
    print(new1[0], new1[1])
    # 2017-02-22 10:18:00.002000
    newfinal = []
    for i in new1:
        j = i.split(' ')
        dt = j[0].split('-')
        tm = j[1].split(':')[:2]
        fnl = dt[1] + '/' + dt[2] + '/' + dt[0] + ' ' + tm[0] + ':' + tm[1]
        newfinal.append(fnl)
    print(newfinal[0])
    # print(list_x)
    newlist = newlist[:int(aa)]
    tf = time.time()
    n_feats = 3
    n_timesteps = len(list_x)
    shapes = []
    # print(listy)
    # fig = dict(data=data, layout=layout)
    t3 = time.time()
    fig1 = go.Figure()
    min_x = 0
    max_x = 300

    min_y = 0
    max_y = 240

    # Generate random data for testing

    fig1 = make_subplots(rows=2, cols=1, shared_xaxes=False, vertical_spacing=0.1)

    fig1.add_trace(go.Scatter(
        x=list_x,
        y=listy,
        name="FHR data",
        yaxis="y1",
        xaxis="x1",

    ), row=1,
        col=1)
    fig1.add_trace(go.Scatter(
        x=list_x1,
        y=listy1,
        name="MHR data",
        yaxis="y1",
        xaxis="x1",

    ), row=1,
        col=1)
    fig1.add_trace(go.Scatter(
        x=list_x2,
        y=listy2,
        name="TOCO data",
        yaxis="y2",
        xaxis="x2",

    ), row=2,
        col=1)

    fig1.add_trace(go.Scatter(
        x=[],
        y=[],
        # name="yaxis3 data",
        yaxis="y3",
        xaxis="x3",
    ))

    fig1.add_trace(go.Scatter(
        x=[],
        y=[],
        # name="yaxis4 data",
        yaxis="y4",
        xaxis="x4",
    ))

    fig1.add_trace(go.Scatter(
        x=[],
        y=[],
        # name="yaxis5 data",
        yaxis="y5",
        xaxis="x5"
    ))

    fig1.add_trace(go.Scatter(
        x=[],
        y=[],
        # name="yaxis6 data",
        yaxis="y6",
        xaxis="x6",
    ))

    fig1.add_trace(go.Scatter(
        x=[],
        y=[],
        # name="yaxis7 data",
        yaxis="y7",
        xaxis="x7",
    ))

    fig1.add_trace(go.Scatter(
        x=[],
        y=[],
        # name="yaxis8 data",
        yaxis="y8",
        xaxis="x8"
    ))

    # Create axis objects
    fig1.update_layout(
        xaxis=dict(
            showgrid=False,
            showticklabels=False,
            range=(600, min_x),
            zeroline=False,
            showline=True,
            linewidth=0.5,
            linecolor='black',
            mirror=True,

        ),

        xaxis2=dict(
            showgrid=False,
            showticklabels=False,
            range=(min_x, 600),
            zeroline=False,
            showline=True,
            linewidth=0.5,
            linecolor='black',
            mirror=True,
            #     rangeslirangeslider=dict(
            #     visible = True,
            #     bgcolor=' #FFFFFF'
            # ),

        ),

        xaxis3=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=10, tick0=min_x,
            showticklabels=False,
            overlaying='x',
            range=(min_x, max_x),
            zeroline=False

        ),
        xaxis4=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.3)', dtick=60, tick0=min_x,
            overlaying='x',
            range=(min_x, max_x),
            zeroline=False,
            showticklabels=False,

        ),
        xaxis5=dict(
            showgrid=True, gridwidth=1.5, gridcolor='rgba(0,0,0,1.0)', dtick=300, tick0=min_x,
            overlaying='x',
            range=(min_x, max_x),
            zeroline=False,
            side='top',
            tickmode='array',
            tickvals=new2,
            ticktext=newfinal
        ),
        xaxis6=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=10, tick0=min_x,
            showticklabels=False,
            overlaying='x2',
            range=(min_x, max_x),
            zeroline=False,

        ),
        xaxis7=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.3)', dtick=60, tick0=min_x,
            overlaying='x2',
            range=(min_x, max_x),
            zeroline=False,
            showticklabels=False,

        ),
        xaxis8=dict(
            showgrid=True, gridwidth=1.5, gridcolor='rgba(0,0,0,1.0)', dtick=300, tick0=min_x,
            overlaying='x2',
            range=(min_x, max_x),
            zeroline=False,
            tickmode='array',
            side='top',
            tickvals=new2,
            ticktext=newfinal

        ),

        # data axis
        yaxis=dict(
            showgrid=False,
            showticklabels=False,
            range=(30, max_y),
            fixedrange=True,
            zeroline=False

        ),
        yaxis2=dict(
            showgrid=False,
            showticklabels=False,
            range=(min_y, 100),
            fixedrange=True,
            zeroline=False

        ),

        # For left ticks
        yaxis3=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=10, tick0=30,
            showticklabels=False,
            side='left',
            mirror=True,
            overlaying='y',
            range=(30, max_y),
            fixedrange=True,
            zeroline=False

        ),
        # For right ticks
        yaxis4=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=30, tick0=30,
            showticklabels=True,
            side='right',
            overlaying='y',
            range=(30, max_y),
            fixedrange=True,
            zeroline=False

        ),
        # For 30 increments
        yaxis5=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,1.0)', dtick=30, tick0=30,
            overlaying='y',
            range=(30, max_y),
            fixedrange=True,
            zeroline=False

        ),
        yaxis6=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=10, tick0=min_y,
            showticklabels=False,
            side='left',
            mirror=True,
            overlaying='y2',
            range=(min_y, 100),
            fixedrange=True,
            zeroline=False

        ),
        # For right ticks
        yaxis7=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=20, tick0=min_y,
            showticklabels=True,
            side='right',
            overlaying='y2',
            range=(min_y, 100),
            fixedrange=True,
            zeroline=False

        ),
        # For 30 increments
        yaxis8=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,1.0)', dtick=20, tick0=min_y,
            overlaying='y2',
            range=(min_y, 100),
            fixedrange=True,
            zeroline=False

        ),

    )

    t4 = time.time()
    print("axis adding: ", t4 - t3)

    fig1.update_layout(
        paper_bgcolor='rgba(1.0,1.0,1.0,0.0)',
        plot_bgcolor='rgba(1.0,1.0,1.0,1.0)',
        autosize=False,

        height=1000, width=1000,
        #title_text="Subplots: START DATETIME:" + str(listx[0]) + ", END DATETIME:" + str(listx[-1]),
        title_text="PatientId: "+ patientID + " Encounter Id: "+ encid +"<br>" +"Subplots: START DATETIME:" + str(listx[0])[:-7] + 
        ", END DATETIME:" + str(listx[-1])[:-7] , dragmode='pan',
        showlegend=True)
    # print(fig)
    fig1.update_xaxes(matches='x')

    # Add shape regions
    fig1.update_layout(
        shapes=[
            # 1st highlight during Feb 4 - Feb 6
            dict(
                type="rect",
                # x-reference is assigned to the x-values
                xref="x",
                # y-reference is assigned to the plot paper [0,1]
                # yref="paper",
                yref="y",
                x0=0,
                y0=110,
                x1=list_x[-1],
                y1=170,
                fillcolor="Gray",
                opacity=0.2,

            ),
        ]
    )
    t6 = time.time()
    print("total time", t6 - tf)
    # fig1.show()

    print("--------")

    fig2 = go.Figure()
    min_x = 0
    max_x = 300

    min_y = 0
    max_y = 240

    # Generate random data for testing
    fig2 = make_subplots(rows=2, cols=1, shared_xaxes=False, vertical_spacing=0.1)

    fig2.add_trace(go.Scatter(
        x=list_x,
        y=listy,
        name="FHR data",
        yaxis="y1",
        xaxis="x1",

    ), row=1,
        col=1)
    fig2.add_trace(go.Scatter(
        x=list_x1,
        y=listy1,
        name="MHR data",
        yaxis="y1",
        xaxis="x1",

    ), row=1,
        col=1)
    fig2.add_trace(go.Scatter(
        x=list_x2,
        y=listy2,
        name="TOCO data",
        yaxis="y2",
        xaxis="x2",

    ), row=2,
        col=1)

    fig2.add_trace(go.Scatter(
        x=[],
        y=[],
        # name="yaxis3 data",
        yaxis="y3",
        xaxis="x3",
    ))

    fig2.add_trace(go.Scatter(
        x=[],
        y=[],
        # name="yaxis4 data",
        yaxis="y4",
        xaxis="x4",
    ))

    fig2.add_trace(go.Scatter(
        x=[],
        y=[],
        # name="yaxis5 data",
        yaxis="y5",
        xaxis="x5"
    ))

    fig2.add_trace(go.Scatter(
        x=[],
        y=[],
        # name="yaxis6 data",
        yaxis="y6",
        xaxis="x6",
    ))

    fig2.add_trace(go.Scatter(
        x=[],
        y=[],
        # name="yaxis7 data",
        yaxis="y7",
        xaxis="x7",
    ))

    fig2.add_trace(go.Scatter(
        x=[],
        y=[],
        # name="yaxis8 data",
        yaxis="y8",
        xaxis="x8"
    ))

    # Create axis objects
    fig2.update_layout(
        xaxis=dict(
            showgrid=False,
            showticklabels=False,
            range=(900, min_x),
            zeroline=False,
            showline=True,
            linewidth=0.5,
            linecolor='black',
            mirror=True,

        ),

        xaxis2=dict(
            showgrid=False,
            showticklabels=False,
            range=(min_x, 900),
            zeroline=False,
            showline=True,
            linewidth=0.5,
            linecolor='black',
            mirror=True,
            #     rangeslirangeslider=dict(
            #     visible = True,
            #     bgcolor=' #FFFFFF'
            # ),

        ),

        xaxis3=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=10, tick0=min_x,
            showticklabels=False,
            overlaying='x',
            range=(min_x, max_x),
            zeroline=False,
            # side='top',

        ),
        xaxis4=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.3)', dtick=60, tick0=min_x,
            overlaying='x',
            range=(min_x, max_x),
            zeroline=False,
            showticklabels=False,
            # side='top',

        ),
        xaxis5=dict(
            showgrid=True, gridwidth=1.5, gridcolor='rgba(0,0,0,1.0)', dtick=300, tick0=min_x,
            overlaying='x',
            range=(min_x, max_x),
            zeroline=False,
            side='top',

            tickmode='array',
            tickvals=new2,
            ticktext=newfinal
        ),
        xaxis6=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=10, tick0=min_x,
            showticklabels=False,
            overlaying='x2',
            range=(min_x, max_x),
            zeroline=False,

        ),
        xaxis7=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.3)', dtick=60, tick0=min_x,
            overlaying='x2',
            range=(min_x, max_x),
            zeroline=False,
            showticklabels=False,

        ),
        xaxis8=dict(
            showgrid=True, gridwidth=1.5, gridcolor='rgba(0,0,0,1.0)', dtick=300, tick0=min_x,
            overlaying='x2',
            range=(min_x, max_x),
            zeroline=False,
            side='top',
            tickmode='array',
            tickvals=new2,
            ticktext=newfinal

        ),

        # data axis
        yaxis=dict(
            showgrid=False,
            showticklabels=False,
            range=(30, max_y),
            fixedrange=True,
            zeroline=False

        ),
        yaxis2=dict(
            showgrid=False,
            showticklabels=False,
            range=(min_y, 100),
            fixedrange=True,
            zeroline=False

        ),

        # For left ticks
        yaxis3=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=10, tick0=30,
            showticklabels=False,
            side='left',
            mirror=True,
            overlaying='y',
            range=(30, max_y),
            fixedrange=True,
            zeroline=False

        ),
        # For right ticks
        yaxis4=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=30, tick0=30,
            showticklabels=True,
            side='right',
            overlaying='y',
            range=(30, max_y),
            fixedrange=True,
            zeroline=False

        ),
        # For 30 increments
        yaxis5=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,1.0)', dtick=30, tick0=30,
            overlaying='y',
            range=(30, max_y),
            fixedrange=True,
            zeroline=False

        ),
        yaxis6=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=10, tick0=min_y,
            showticklabels=False,
            side='left',
            mirror=True,
            overlaying='y2',
            range=(min_y, 100),
            fixedrange=True,
            zeroline=False

        ),
        # For right ticks
        yaxis7=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=20, tick0=min_y,
            showticklabels=True,
            side='right',
            overlaying='y2',
            range=(min_y, 100),
            fixedrange=True,
            zeroline=False

        ),
        # For 30 increments
        yaxis8=dict(
            showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,1.0)', dtick=20, tick0=min_y,
            overlaying='y2',
            range=(min_y, 100),
            fixedrange=True,
            zeroline=False

        ),

    )

    fig2.update_layout(
        paper_bgcolor='rgba(1.0,1.0,1.0,0.0)',
        plot_bgcolor='rgba(1.0,1.0,1.0,1.0)',
        autosize=False,
        height=1000, width=1200,
        title_text="Subplots: START DATETIME:" + str(listx[0])[:-7] + ", END DATETIME:" + str(listx[-1])[:-7], dragmode='pan',
        showlegend=True)
    # print(fig)
    fig2.update_xaxes(matches='x')
    fig2.update_layout(
        shapes=[
            # 1st highlight during Feb 4 - Feb
            dict(
                type="rect",
                # x-reference is assigned to the x-values
                xref="x",
                # y-reference is assigned to the plot paper [0,1]
                # yref="paper",
                yref="y",
                x0=0,
                y0=110,
                x1=list_x[-1],
                y1=170,
                fillcolor="Gray",
                opacity=0.2,

            ),
        ]
    )
    FHRClick = [-1, -1]
    MHRClick = [-1, -1]
    TOCOClick = [-1, -1]
    # t6=time.time()
    # fig1.show()
    # fig2.show()
    fig4 = go.Figure()
    fig4 = make_subplots(rows=2, cols=1, shared_xaxes=False, vertical_spacing=0.1)
    fig4.update_layout(paper_bgcolor='rgba(1.0,1.0,1.0,0.0)',
                       plot_bgcolor='rgba(1.0,1.0,1.0,1.0)',
                       xaxis={'showgrid': False, 'showline': False, 'zeroline': False, 'showticklabels': False},
                       yaxis={'showgrid': False, 'showline': False, 'zeroline': False, 'showticklabels': False},
                       width=700, height=700)

    text_markdown = "Hello World"


    html.Div([
    html.Div([
        html.Div([
            html.H3('Column 1'),
            dcc.Graph(id='g1', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),

        html.Div([
            html.H3('Column 2'),
            dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),
    ], className="row")
])

    app.layout = html.Div([
        #dbc.Spinner()
        html.Div([
            html.Div([
                dbc.Button('Open filtered graph', id='open-backdrop', color='secondary', className='mr-1',
                           style={'margin-left': '50%'}),
                ]),


            dbc.Popover(
                    [dbc.PopoverBody(dcc.Graph(id='live_graph'))
                     ],
                    id='modal',
                    is_open=False,
                    target='open-backdrop',
                    placement='bottom',
                    style={'background-color': '#fff', 'border': ' 2px solid black'}
                ),
                dcc.Graph(figure=fig1, id="fig1"),
                dcc.Graph(figure=fig2, id="fig2"),
                html.Div(id='intermediate-value'),
                html.Div(id='intermediate-value2', style={'display': 'none'}),
                html.Button('Generate Graph', id='button', style={'display': 'none'})

            ])
       ])


    # for figure 1
    @app.callback(
        output=Output('intermediate-value', 'children'),
        inputs=[Input('fig1', 'clickData')])
    def display_click_data(clickData):
        if clickData:
            index = clickData['points'][0]['pointIndex']
            curveNumber = clickData['points'][0]['curveNumber']
            if curveNumber == 0:
                if FHRClick[0] == -1:
                    FHRClick[0] = index
                    return [FHRClick[0]]
                else:
                    FHRClick[1] = index
                    click1 = FHRClick[0]
                    click2 = FHRClick[1]
                    print("FHR index range clicked is " + str(FHRClick))
                    # print("y values are: " +  str(list_x[FHRClick[0]]))
                    # print("y values are: " + str(list_x1[FHRClick[0]]))
                    # print("y values are: " + str(list_x2[FHRClick[0]]))
                    print("Values between range are: ")
                    temp = listy[FHRClick[0]:FHRClick[1]]
                    temp1 = listy1[FHRClick[0]:FHRClick[1]]
                    temp2 = listy2[FHRClick[0]:FHRClick[1]]
                    print(temp)
                    print("----------------------------------------------")
                    FHRClick[0] = -1
                    FHRClick[1] = -1
                    return [click1, click2]
                # print("FHR data from list " + str(list_x[index]) + " " + str(listy[index]))
                # print("data from click " + str(clickData['points'][0]['x']) + " " + str(clickData['points'][0]['y']))
            elif curveNumber == 1:
                if MHRClick[0] == -1:
                    MHRClick[0] = index
                    return [MHRClick[0]]
                else:
                    MHRClick[1] = index
                    click1 = MHRClick[0]
                    click2 = MHRClick[1]
                    print("MHR index range clicked is " + str(MHRClick))
                    print("Values between range are: ")
                    temp = listy1[MHRClick[0]:MHRClick[1]]
                    print(temp)
                    print("----------------------------------------------")
                    MHRClick[0] = -1
                    MHRClick[1] = -1
                    return [click1, click2]
                # print("MHR data from list " + str(list_x1[index]) + " " + str(listy1[index]))
                # print("data from click " + str(clickData['points'][0]['x']) + " " + str(clickData['points'][0]['y']))
            else:
                if TOCOClick[0] == -1:
                    TOCOClick[0] = index
                    return [TOCOClick[0]]
                else:
                    TOCOClick[1] = index
                    click1 = TOCOClick[0]
                    click2 = TOCOClick[1]
                    print("TOCO index range clicked is " + str(TOCOClick))
                    print("Values between range are: ")
                    temp = listy2[TOCOClick[0]:TOCOClick[1]]
                    print(temp)
                    print("----------------------------------------------")
                    TOCOClick[0] = -1
                    TOCOClick[1] = -1
                    return [click1, click2]
                # print("TOCO from list " + str(list_x2[index]) + " " + str(listy2[index]))
                # print("data from click " + str(clickData['points'][0]['x']) + " " + str(clickData['points'][0]['y']))

    # @app.callback(
    #     output=Output('intermediate-value2', 'children'),
    #     inputs=[Input('fig2', 'clickData')])
    # def display_click_data(clickData):
    #     if clickData:
    #         print("fig2 " + str(clickData))
    #         return None

    @app.callback(
        output=Output('live_graph', 'figure'),
        inputs=[Input('button', 'n_clicks'),
                Input('intermediate-value', 'children')])
    def update_graph(n_clicks, children):
        if not children or len(children) == 1:
            return fig4
        else:

            temp = listy[children[0]:children[1]]
            temp1 = listy1[children[0]:children[1]]
            temp2 = listy2[children[0]:children[1]]
            poplistfhrx = list_x[children[0]:children[1]]
            poplistfhrxy = listy[children[0]:children[1]]
            poplistmhrx = list_x1[children[0]:children[1]]
            poplistmhry = listy1[children[0]:children[1]]
            poplisttocox = list_x2[children[0]:children[1]]
            poplisttocoy = listy2[children[0]:children[1]]
            minstart = poplistfhrx[0]
            poplistfhrx = [(i - poplistfhrx[0]) for i in poplistfhrx]
            poplistmhrx = [(i - poplistmhrx[0]) for i in poplistmhrx]
            poplisttocox = [(i - poplisttocox[0]) for i in poplisttocox]
            min_x = 0
            max_x = 300

            min_y = 0
            max_y = 240

            fig3 = make_subplots(rows=2, cols=1, shared_xaxes=False, vertical_spacing=0.1)

            fig3.add_trace(go.Scatter(
                x=poplistfhrx,
                y=poplistfhrxy,
                name="FHR data",
                yaxis="y1",
                xaxis="x1",

            ), row=1,
                col=1)
            fig3.add_trace(go.Scatter(
                x=poplistmhrx,
                y=poplistmhry,
                name="MHR data",
                yaxis="y1",
                xaxis="x1",

            ), row=1,
                col=1)
            fig3.add_trace(go.Scatter(
                x=poplisttocox,
                y=poplisttocoy,
                name="TOCO data",
                yaxis="y2",
                xaxis="x2",

            ), row=2,
                col=1)

            fig3.add_trace(go.Scatter(
                x=[],
                y=[],
                # name="yaxis3 data",
                yaxis="y3",
                xaxis="x3",
            ))

            fig3.add_trace(go.Scatter(
                x=[],
                y=[],
                # name="yaxis4 data",
                yaxis="y4",
                xaxis="x4",
            ))

            fig3.add_trace(go.Scatter(
                x=[],
                y=[],
                # name="yaxis5 data",
                yaxis="y5",
                xaxis="x5"
            ))

            fig3.add_trace(go.Scatter(
                x=[],
                y=[],
                # name="yaxis6 data",
                yaxis="y6",
                xaxis="x6",
            ))

            fig3.add_trace(go.Scatter(
                x=[],
                y=[],
                # name="yaxis7 data",
                yaxis="y7",
                xaxis="x7",
            ))

            fig3.add_trace(go.Scatter(
                x=[],
                y=[],
                # name="yaxis8 data",
                yaxis="y8",
                xaxis="x8"
            ))

            # Create axis objects
            fig3.update_layout(
                xaxis=dict(
                    showgrid=False,
                    showticklabels=False,
                    range=(min_x, 120),
                    zeroline=False,
                    showline=True,
                    linewidth=0.5,
                    linecolor='black',
                    mirror=True,

                ),

                xaxis2=dict(
                    showgrid=False,
                    showticklabels=False,
                    range=(min_x, 120),
                    zeroline=False,
                    showline=True,
                    linewidth=0.5,
                    linecolor='black',
                    mirror=True,
                    #     rangeslirangeslider=dict(
                    #     visible = True,
                    #     bgcolor=' #FFFFFF'
                    # ),

                ),

                xaxis3=dict(
                    showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=10, tick0=min_x,
                    showticklabels=False,
                    overlaying='x',
                    range=(min_x, max_x),
                    zeroline=False

                ),
                xaxis4=dict(
                    showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.3)', dtick=60, tick0=min_x,
                    overlaying='x',
                    range=(min_x, max_x),
                    zeroline=False,
                    showticklabels=False,

                ),
                xaxis5=dict(
                    showgrid=True, gridwidth=1.5, gridcolor='rgba(0,0,0,1.0)', dtick=300, tick0=min_x,
                    overlaying='x',
                    range=(min_x, max_x),
                    zeroline=False,
                    side='top',
                    # tickmode='array',
                    showticklabels=False,
                    # tickvals=new2,
                    # ticktext=newfinal
                ),
                xaxis6=dict(
                    showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=10, tick0=min_x,
                    showticklabels=False,
                    overlaying='x2',
                    range=(min_x, max_x),
                    zeroline=False,

                ),
                xaxis7=dict(
                    showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.3)', dtick=60, tick0=min_x,
                    overlaying='x2',
                    range=(min_x, max_x),
                    zeroline=False,
                    showticklabels=False,

                ),
                xaxis8=dict(
                    showgrid=True, gridwidth=1.5, gridcolor='rgba(0,0,0,1.0)', dtick=300, tick0=min_x,
                    overlaying='x2',
                    range=(min_x, max_x),
                    zeroline=False,
                    # tickmode='array',
                    side='top',
                    showticklabels=False,
                    # tickvals=new2,
                    # ticktext=newfinal

                ),

                # data axis
                yaxis=dict(
                    showgrid=False,
                    showticklabels=False,
                    range=(30, max_y),
                    fixedrange=True,
                    zeroline=False

                ),
                yaxis2=dict(
                    showgrid=False,
                    showticklabels=False,
                    range=(min_y, 100),
                    fixedrange=True,
                    zeroline=False

                ),

                # For left ticks
                yaxis3=dict(
                    showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=10, tick0=30,
                    showticklabels=False,
                    side='left',
                    mirror=True,
                    overlaying='y',
                    range=(30, max_y),
                    fixedrange=True,
                    zeroline=False

                ),
                # For right ticks
                yaxis4=dict(
                    showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=30, tick0=30,
                    showticklabels=True,
                    side='right',
                    overlaying='y',
                    range=(30, max_y),
                    fixedrange=True,
                    zeroline=False

                ),
                # For 30 increments
                yaxis5=dict(
                    showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,1.0)', dtick=30, tick0=30,
                    overlaying='y',
                    range=(30, max_y),
                    fixedrange=True,
                    zeroline=False

                ),
                yaxis6=dict(
                    showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=10, tick0=min_y,
                    showticklabels=False,
                    side='left',
                    mirror=True,
                    overlaying='y2',
                    range=(min_y, 100),
                    fixedrange=True,
                    zeroline=False

                ),
                # For right ticks
                yaxis7=dict(
                    showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,0.1)', dtick=20, tick0=min_y,
                    showticklabels=True,
                    side='right',
                    overlaying='y2',
                    range=(min_y, 100),
                    fixedrange=True,
                    zeroline=False

                ),
                # For 30 increments
                yaxis8=dict(
                    showgrid=True, gridwidth=0.5, gridcolor='rgba(0,0,0,1.0)', dtick=20, tick0=min_y,
                    overlaying='y2',
                    range=(min_y, 100),
                    fixedrange=True,
                    zeroline=False

                ),

            )

            fig3.update_layout(
                paper_bgcolor='rgba(1.0,1.0,1.0,0.0)',
                plot_bgcolor='rgba(1.0,1.0,1.0,1.0)',
                autosize=False,
                # title_text="Subplots: START DATETIME:" + str(listx[0]) + ", END DATETIME:" + str(listx[-1]),
                dragmode='pan',
                showlegend=False)
            # print(fig)
            fig3.update_xaxes(matches='x')

            # Add shape regions
            fig3.update_layout(
                shapes=[
                    # 1st highlight during Feb 4 - Feb 6
                    dict(
                        type="rect",
                        # x-reference is assigned to the x-values
                        xref="x",
                        # y-reference is assigned to the plot paper [0,1]
                        # yref="paper",
                        yref="y",
                        x0=0,
                        y0=110,
                        x1=list_x[-1],
                        y1=170,
                        fillcolor="Gray",
                        opacity=0.2,

                    ),
                ]
            )
            return fig3

    @app.callback(
        Output("modal", "is_open"),
        [Input("open-backdrop", "n_clicks")], [State("modal", "is_open")], )
    def toggle_modal(n1, is_open):
        if n1:
            return not is_open
        return is_open
        
    #if __name__ == '__main__':
    #app.run_server(debug=True)


#final(x, y)
#final(subjectId, record[0][0])
# plots = [fig1, fig2]
# app = dash.Dash()
# layout = html.Div(
# [html.Div(plots[i]) for i in range(len(plots))],
# style = {'margin-right': '0px'}
# )
# app.layout = layout
# app.run_server(port=8052)

# input()

# fig.show()
# py.iplot(data, filename='webgl75')
# py.iplot(fig, filename='axes-ticks')

# Add traces
# fig.add_trace(go.Scatter(x=listx, y=listy,
#                   mode='markers',
#                    name='markers'))

# fig.show()


'''
    fig = make_subplots(rows=3, cols=1,subplot_titles=("Plot FHR", "Plot MHR", "Plot TOCO"))

    fig.add_trace(
        go.Scatter(x=fhr0[1], y=fhr0[0]),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=fhr1[1], y=fhr1[0]),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=fhr2[1], y=fhr2[0]),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=fhr3[1], y=fhr3[0]),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(x=timestamp_list, y=mhr_avg),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=timestamp_list, y=toco_avg),
        row=3, col=1
    )

    fig.update_layout(height=800, width=1000, title_text="Subplots")
    fig.show()





    #fig1 = go.Figure(data=go.Scatter(x=timestamp_list, y=fhr_avg))
    #fig2 = go.Figure(data=go.Scatter(x=timestamp_list, y=mhr_avg))
    #fig3 = go.Figure(data=go.Scatter(x=timestamp_list, y=toco_avg))
    #fig1.show()
    #fig2.show()
    #fig3.show()


    fig, ax = plt.subplots(3)
    ax[0].plot_date(timestamp_list,fhr_avg,fmt='b-',color='green')
    ax[1].plot_date(timestamp_list,mhr_avg,fmt='b-',color='blue')
    ax[2].plot_date(timestamp_list,toco_avg,fmt='b-',color='purple')
    fig.autofmt_xdate()
    plt.yticks(np.arange(30, 240, 10))

    major_ticks = np.arange(30, 250, 30)
    minor_ticks = np.arange(30, 250, 10)

    ax[0].set_yticks(major_ticks)
    ax[0].set_yticks(minor_ticks, minor=True)
    ax[0].grid(which='both')
    ax[0].grid(which='minor', alpha=0.2)
    ax[0].grid(which='major', alpha=0.5)
    #ax[0].set_xlim([datetime.datetime(2017, 5, 26,22,11,0), datetime.datetime(2017, 5, 26,22,17,11)])
    ax[1].set_yticks(major_ticks)
    ax[1].set_yticks(minor_ticks, minor=True)
    ax[1].grid(which='both')
    ax[1].grid(which='minor', alpha=0.2)
    ax[1].grid(which='major', alpha=0.5)
    ax[2].set_yticks(major_ticks)
    ax[2].set_yticks(minor_ticks, minor=True)
    ax[2].grid(which='both')
    ax[2].grid(which='minor', alpha=0.2)
    ax[2].grid(which='major', alpha=0.5)
    ax[0].title.set_text('FHR '+str(patientID))
    ax[1].title.set_text('MHR '+str(patientID))
    ax[2].title.set_text('TOCO '+str(patientID))
    #ax[2].set_xlim([datetime.datetime(2017, 5, 26,22,16,0), datetime.datetime(2017, 5, 26,22,21,11)])

    plt.xlabel('Time Stamp')
    plt.ylabel('Heart Rate')
    plt.rcParams['figure.figsize'] = (25,10)
    #plt.show()
    #plt.draw()
    #plt.waitforbuttonpress(0)
    #plt.close()
'''

