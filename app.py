import random
import string
import base64
from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, render_template, request

application = Flask(__name__)
application.secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


@application.route("/")
def home_page():
    pitchers = pd.read_csv('pitchers_2020.csv')
    pitches = 500
    search = ""
    names = pitchers["player_name"].tolist()
    names = set(names)
    names = sorted(names)
    names.insert(0, "")
    pitchers = pitchers[pitchers["Pitches"] >= pitches]
    if search != "":
        pitchers = pitchers[pitchers['player_name'] == search]
    pitchers = pitchers[["player_name", "Whiff", "xWhiff", "In_Whiff"]]
    pitchers = pitchers.rename(columns={"player_name": "Name"})
    pitchers = pitchers.round(3)
    pitchers = pitchers.sort_values(by='In_Whiff', ascending=False)
    whiff = "selected"
    woba = ""
    inzone = ""
    outofzone = ""
    stuffera = ""
    return render_template("pitchers.html", pitchers=pitchers, whiff=whiff, woba=woba, inzone=inzone,
                           outofzone=outofzone, stuffera=stuffera, pitches=pitches, names = names)


@application.route("/", methods=['POST'])
def pitchers_table():
    pitches = int(request.form['pitches'])
    type = request.form['type']
    search = request.form['search']
    pitchers = pd.read_csv('pitchers_2020.csv')
    names = set(names)
    names = sorted(names)
    names.insert(0, "")
    pitchers = pitchers[pitchers["Pitches"] >= pitches]
    if search != "":
        pitchers = pitchers[pitchers['player_name'] == search]
    if type == "Whiffs":
        pitchers = pitchers[["player_name", "Whiff", "xWhiff", "In_Whiff"]]
        pitchers = pitchers.rename(columns={"player_name": "Name"})
        pitchers = pitchers.round(3)
        pitchers = pitchers.sort_values(by='In_Whiff', ascending=False)
        whiff = "selected"
        woba = ""
        inzone = ""
        outofzone = ""
        stuffera = ""
        return render_template("pitchers.html", pitchers=pitchers, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, stuffera=stuffera, pitches=pitches, names = names)
    elif type == "In-Zone":
        pitchers = pitchers[["player_name", "IZ.Swing", "IZ.xSwing", "IZ"]]
        pitchers = pitchers.rename(columns={"player_name": "Name"})
        pitchers = pitchers.round(3)
        pitchers = pitchers.sort_values(by='IZ', ascending=True)
        whiff = ""
        woba = ""
        inzone = "selected"
        outofzone = ""
        stuffera = ""
        return render_template("pitchers.html", pitchers=pitchers, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, stuffera=stuffera, pitches=pitches, names = names)
    elif type == "Out Of Zone":
        pitchers = pitchers[["player_name", "OOZ.Swing", "OOZ.xSwing", "OOZ"]]
        pitchers = pitchers.rename(columns={"player_name": "Name"})
        pitchers = pitchers.round(3)
        pitchers = pitchers.sort_values(by='OOZ', ascending=False)
        whiff = ""
        woba = ""
        inzone = ""
        outofzone = "selected"
        stuffera = ""
        return render_template("pitchers.html", pitchers=pitchers, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, stuffera=stuffera, pitches=pitches, names = names)
    elif type == "wOBA":
        pitchers = pitchers[["player_name", "wOBA", "xwOBA", "In_wOBA"]]
        pitchers = pitchers.rename(columns={"player_name": "Name"})
        pitchers = pitchers.round(3)
        pitchers = pitchers.sort_values(by='In_wOBA', ascending=True)
        whiff = ""
        woba = "selected"
        inzone = ""
        outofzone = ""
        stuffera = ""
        return render_template("pitchers.html", pitchers=pitchers, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, stuffera=stuffera, pitches=pitches, names = names)
    else:
        pitchers = pitchers[["player_name", "Command", "S_ERA"]]
        pitchers = pitchers.rename(columns={"player_name": "Name", "S_ERA": "StuffERA"})
        pitchers = pitchers.round(2)
        pitchers = pitchers.sort_values(by='StuffERA', ascending=True)
        whiff = ""
        woba = ""
        inzone = ""
        outofzone = ""
        stuffera = "selected"
        return render_template("pitchers.html", pitchers=pitchers, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, stuffera=stuffera, pitches=pitches, names = names)


@application.route("/hitters")
def hitters_page():
    hitters = pd.read_csv('hitters_2020.csv', encoding="ISO-8859-1")
    pitches = 500
    hitters = hitters[hitters["Pitches"] >= pitches]
    hitters = hitters[["Name", "Whiff", "xWhiff", "In_Whiff"]]
    hitters = hitters.round(3)
    hitters = hitters.sort_values(by='In_Whiff', ascending=True)
    whiff = "selected"
    woba = ""
    inzone = ""
    outofzone = ""
    plate = ""
    return render_template("hitters.html", hitters=hitters, whiff=whiff, woba=woba, inzone=inzone,
                           outofzone=outofzone, plate=plate, pitches=pitches)


@application.route("/hitters", methods=['POST'])
def hitters_table():
    pitches = int(request.form['pitches'])
    type = request.form['type']
    hitters = pd.read_csv('hitters_2020.csv', encoding="ISO-8859-1")
    hitters = hitters[hitters["Pitches"] >= pitches]
    if type == "Whiffs":
        hitters = hitters[["Name", "Whiff", "xWhiff", "In_Whiff"]]
        hitters = hitters.round(3)
        hitters = hitters.sort_values(by='In_Whiff', ascending=True)
        whiff = "selected"
        woba = ""
        inzone = ""
        outofzone = ""
        plate = ""
        return render_template("hitters.html", hitters=hitters, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, plate=plate, pitches=pitches)
    elif type == "In-Zone":
        hitters = hitters[["Name", "IZ.Swing", "IZ.xSwing", "IZ"]]
        hitters = hitters.round(3)
        hitters = hitters.sort_values(by='IZ', ascending=False)
        whiff = ""
        woba = ""
        inzone = "selected"
        outofzone = ""
        plate = ""
        return render_template("hitters.html", hitters=hitters, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, plate=plate, pitches=pitches)
    elif type == "Out Of Zone":
        hitters = hitters[["Name", "OOZ.Swing", "OOZ.xSwing", "OOZ"]]
        hitters = hitters.round(3)
        hitters = hitters.sort_values(by='OOZ', ascending=True)
        whiff = ""
        woba = ""
        inzone = ""
        outofzone = "selected"
        plate = ""
        return render_template("hitters.html", hitters=hitters, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, plate=plate, pitches=pitches)
    elif type == "wOBA":
        hitters = hitters[["Name", "wOBA", "xwOBA", "In_wOBA"]]
        hitters = hitters.round(3)
        hitters = hitters.sort_values(by='In_wOBA', ascending=False)
        whiff = ""
        woba = "selected"
        inzone = ""
        outofzone = ""
        plate = ""
        return render_template("hitters.html", hitters=hitters, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, plate=plate, pitches=pitches)
    else:
        hitters = hitters[["Name", "xwOBA_Swing", "xwOBA_Take", "SAE"]]
        hitters = hitters.round(2)
        hitters = hitters.sort_values(by='SAE', ascending=False)
        whiff = ""
        woba = ""
        inzone = ""
        outofzone = ""
        plate = "selected"
        return render_template("hitters.html", hitters=hitters, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, plate=plate, pitches=pitches)


@application.route("/prospects")
def prospects_page():
    prospects = pd.read_csv('prospects_2019.csv', encoding="ISO-8859-1")
    prospects = prospects[prospects["PlayerID"].str.contains("sa")]
    prospects = prospects[["Name", "Value", "Adjusted Value", "Elite Rate"]]
    prospects = prospects.round(2)
    prospects = prospects.sort_values(by='Elite Rate', ascending=False)
    minors = "selected"
    all = ""
    return render_template("prospects.html", prospects=prospects, minors=minors, all=all)


@application.route("/prospects", methods=['POST'])
def prospects_table():
    type = request.form['type']
    prospects = pd.read_csv('prospects_2019.csv', encoding="ISO-8859-1")
    if type == "Minors":
        prospects = prospects[prospects["PlayerID"].str.contains("sa")]
        prospects = prospects[["Name", "Value", "Adjusted Value", "Elite Rate"]]
        prospects = prospects.round(2)
        prospects = prospects.sort_values(by='Elite Rate', ascending=False)
        minors = "selected"
        all = ""
        return render_template("prospects.html", prospects=prospects, minors=minors, all=all)
    else:
        prospects = prospects[["Name", "Value", "Adjusted Value", "Elite Rate"]]
        prospects = prospects.round(2)
        prospects = prospects.sort_values(by='Elite Rate', ascending=False)
        minors = ""
        all = "selected"
        return render_template("prospects.html", prospects=prospects, minors=minors, all=all)


@application.route("/prospectchart")
def prospects_chart():
    comps = pd.read_csv('comps.csv', encoding="ISO-8859-1")
    milb = pd.read_csv('milb.csv', encoding="ISO-8859-1")
    colors = pd.read_csv('colors.csv', encoding="ISO-8859-1")
    list = comps["player_list"].tolist()
    list = set(list)
    list = sorted(list)
    p1 = 'Brennen Davis-Cubs-A'
    p2 = ""
    team1 = milb[milb['player_list'] == p1]['Team'].values[0]
    x1 = comps[comps['player_list'] == p1]['Total Val'].to_list()
    w1 = comps[comps['player_list'] == p1]['W'].to_list()
    color = [colors[colors['mascot'] == team1]['primary'].values[0]]
    names = [p1]
    fig = plt.figure()
    plt.hist(x1, weights=w1, bins=20,color=color, label=names,edgecolor='black', linewidth=1.2, figure = fig, density= True)
    plt.suptitle('Comp Based Range Of Outcomes')
    plt.title(p1)
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    selected = [""]
    for i in list:
        if i == p1:
            selected.append("selected")
        else:
            selected.append("")
    selected2 = []
    for i in list:
        if i == p2:
            selected2.append("selected")
        else:
            selected2.append("")
    players = zip(list, selected)
    list2 = list
    list2.insert(0, "")
    selected2.insert(0, "selected")
    players2 = zip(list2, selected2)
    return render_template("prospect_chart.html", players=players, players2=players2, plot = encoded)


@application.route("/prospectchart",methods=['POST'])
def prospects_compare():
    p1 = request.form['player']
    p2 = request.form['player2']
    comps = pd.read_csv('comps.csv', encoding="ISO-8859-1")
    milb = pd.read_csv('milb.csv', encoding="ISO-8859-1")
    colors = pd.read_csv('colors.csv', encoding="ISO-8859-1")
    list = comps["player_list"].tolist()
    list = set(list)
    list = sorted(list)
    selected = [""]
    for i in list:
        if i == p1:
            selected.append("selected")
        else:
            selected.append("")
    selected2 = []
    for i in list:
        if i == p2:
            selected2.append("selected")
        else:
            selected2.append("")
    players = zip(list, selected)
    list2 = list
    list2.insert(0, "")
    selected2.insert(0, "selected")
    players2 = zip(list2, selected2)
    team1 = milb[milb['player_list'] == p1]['Team'].values[0]
    x1 = comps[comps['player_list'] == p1]['Total Val'].to_list()
    w1 = comps[comps['player_list'] == p1]['W'].to_list()
    if p2 == "":
        color = [colors[colors['mascot'] == team1]['primary'].values[0]]
        names = [p1]
        fig = plt.figure()
        plt.hist(x1, weights=w1, bins=20,color=color, label=names,edgecolor='black', linewidth=1.2, figure = fig, density= True)
        plt.suptitle('Comp Based Range Of Outcomes')
        plt.title(p1)
        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
        return render_template("prospect_chart.html", players=players, players2=players2, plot = encoded)
    else:
        team2 = milb[milb['player_list'] == p2]['Team'].values[0]
        x2 = comps[comps['player_list'] == p2]['Total Val'].to_list()
        w2 = comps[comps['player_list'] == p2]['W'].to_list()
        color = [colors[colors['mascot'] == team1]['primary'].values[0],colors[colors['mascot'] == team2]['secondary'].values[0]]
        names = [p1,p2]
        fig = plt.figure()
        plt.hist([x1,x2], weights=[w1,w2], bins=20, color=color, label=names, edgecolor='black', linewidth=1.2, figure=fig,
                 density=True)
        plt.suptitle('Comp Based Range Of Outcomes')
        plt.title(p1 + " vs " + p2)
        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
        return render_template("prospect_chart.html", players=players, players2=players2, plot=encoded)


if __name__ == "__main__":
    application.run(port=4500)
