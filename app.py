import random
import string
import base64
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

application = Flask(__name__)
application.secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


@application.route("/")
def home_page():
    pitchers = pd.read_csv('all_seasons_pitchers.csv', encoding = 'utf_8')
    pitchers = pitchers[pitchers['Season'] == 2021]
    pitches = 250
    values = "selected"
    percentile = ""
    pitchers = pitchers[pitchers["Pitches"] >= pitches]
    expected = "xWhiff (AVG - 0.105) - Average expected swing and miss rate of all pitches thrown by the pitcher based on count/pitch type/location"
    influence = "In_Whiff (AVG - 0) - How much more or less likely a pitcher is to generate a swinging strike factoring in opposing hitter"
    pitchers = pitchers[["player_name", "Season", "Whiff", "xWhiff", "In_Whiff"]]
    pitchers = pitchers.rename(columns={"player_name": "Name"})
    pitchers = pitchers.round(3)
    pitchers = pitchers.sort_values(by='In_Whiff', ascending=False)
    whiff = "selected"
    woba = ""
    inzone = ""
    outofzone = ""
    stuffera = ""
    start21 = "selected"
    start20 = ""
    start19 = ""
    start18 = ""
    start17 = ""
    start16 = ""
    start15 = ""
    end21 = "selected"
    end20 = ""
    end19 = ""
    end18 = ""
    end17 = ""
    end16 = ""
    end15 = ""
    return render_template("pitchers.html", pitchers=pitchers, whiff=whiff, woba=woba, inzone=inzone,
                           outofzone=outofzone, stuffera=stuffera, pitches=pitches, influence=influence,
                           expected=expected,start21=start21,start20=start20, start19=start19, start18=start18, start17=start17, start16=start16,
                           start15=start15,
                           end21=end21,end20=end20, end19=end19, end18=end18, end17=end17, end16=end16, end15=end15, values = values,percentile = percentile)


@application.route("/", methods=['POST'])
def pitchers_table():
    pitches = int(request.form['pitches'])
    display = request.form['display']
    search = request.form['search']
    text = search
    search = search.strip()
    type = request.form['type']
    year = int(request.form['year'])
    yearend = int(request.form['yearend'])
    if year > yearend:
        end = year
        year = yearend
        yearend = end
    if year == 2021:
        start21 = "selected"
        start20 = ""
        start19 = ""
        start18 = ""
        start17 = ""
        start16 = ""
        start15 = ""
    elif year == 2020:
        start21 = ""
        start20 = "selected"
        start19 = ""
        start18 = ""
        start17 = ""
        start16 = ""
        start15 = ""
    elif year == 2019:
        start21 = ""
        start20 = ""
        start19 = "selected"
        start18 = ""
        start17 = ""
        start16 = ""
        start15 = ""
    elif year == 2018:
        start21 = ""
        start20 = ""
        start19 = ""
        start18 = "selected"
        start17 = ""
        start16 = ""
        start15 = ""
    elif year == 2017:
        start21 = ""
        start20 = ""
        start19 = ""
        start18 = ""
        start17 = "selected"
        start16 = ""
        start15 = ""
    elif year == 2016:
        start21 = ""
        start20 = ""
        start19 = ""
        start18 = ""
        start17 = ""
        start16 = "selected"
        start15 = ""
    else:
        start21 = ""
        start20 = ""
        start19 = ""
        start18 = ""
        start17 = ""
        start16 = ""
        start15 = "selected"
    if yearend == 2021:
        end21 = "selected"
        end20 = ""
        end19 = ""
        end18 = ""
        end17 = ""
        end16 = ""
        end15 = ""
    elif yearend == 2020:
        end21 = ""
        end20 = "selected"
        end19 = ""
        end18 = ""
        end17 = ""
        end16 = ""
        end15 = ""
    elif yearend == 2019:
        end21 = ""
        end20 = ""
        end19 = "selected"
        end18 = ""
        end17 = ""
        end16 = ""
        end15 = ""
    elif yearend == 2018:
        end21 = ""
        end20 = ""
        end19 = ""
        end18 = "selected"
        end17 = ""
        end16 = ""
        end15 = ""
    elif yearend == 2017:
        end21 = ""
        end20 = ""
        end19 = ""
        end18 = ""
        end17 = "selected"
        end16 = ""
        end15 = ""
    elif yearend == 2016:
        end21 = ""
        end20 = ""
        end19 = ""
        end18 = ""
        end17 = ""
        end16 = "selected"
        end15 = ""
    else:
        end21 = ""
        end20 = ""
        end19 = ""
        end18 = ""
        end17 = ""
        end16 = ""
        end15 = "selected"
    if display == "Percentile":
        pitchers = pd.read_csv('all_seasons_pitchers_percentile.csv', encoding = 'ISO-8859-1')
        percentile = "selected"
        values = ""
    else:
        pitchers = pd.read_csv('all_seasons_pitchers.csv', encoding = 'utf_8')
        percentile = ""
        values = "selected"
    pitchers = pitchers[pitchers['Season'] <= yearend]
    pitchers = pitchers[pitchers['Season'] >= year]
    pitchers = pitchers[pitchers["Pitches"] >= pitches]
    if search is not None:
        pitchers = pitchers[pitchers['player_name'].str.contains(search, case=False)]
    if type == "Whiffs":
        pitchers = pitchers[["player_name","Season", "Whiff", "xWhiff", "In_Whiff"]]
        pitchers = pitchers.rename(columns={"player_name": "Name"})
        pitchers = pitchers.round(3)
        pitchers = pitchers.sort_values(by='In_Whiff', ascending=False)
        expected = "xWhiff (AVG - 0.105) - Average expected swing and miss rate of all pitches thrown by the pitcher based on count/pitch type/location"
        influence = "In_Whiff (AVG - 0) - How much more or less likely a pitcher is to generate a swinging strike factoring in opposing hitter"
        whiff = "selected"
        woba = ""
        inzone = ""
        outofzone = ""
        stuffera = ""
        return render_template("pitchers.html", pitchers=pitchers, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, stuffera=stuffera, pitches=pitches, influence=influence,
                               expected=expected, text=text,start21=start21,start20=start20, start19=start19, start18=start18, start17=start17, start16=start16,
                           start15=start15,
                           end21=end21,end20=end20, end19=end19, end18=end18, end17=end17, end16=end16, end15=end15, values = values,percentile = percentile)
    elif type == "In-Zone":
        pitchers = pitchers[["player_name","Season", "IZ.Swing", "IZ.xSwing", "IZ"]]
        pitchers = pitchers.rename(columns={"player_name": "Name"})
        pitchers = pitchers.round(3)
        pitchers = pitchers.sort_values(by='IZ', ascending=True)
        expected = "IZ.xSwing (AVG - 0.654) - Average expected swing rate of all pitches thrown In the Strike Zone by the pitcher based on count/pitch type/location"
        influence = "IZ (AVG - 0) - How much more or less likely a pitcher is to generate a swing In the Zone factoring in opposing hitter"
        whiff = ""
        woba = ""
        inzone = "selected"
        outofzone = ""
        stuffera = ""
        return render_template("pitchers.html", pitchers=pitchers, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, stuffera=stuffera, pitches=pitches, influence=influence,
                               expected=expected, text=text,start21=start21,start20=start20, start19=start19, start18=start18, start17=start17, start16=start16,
                           start15=start15,
                           end21=end21,end20=end20, end19=end19, end18=end18, end17=end17, end16=end16, end15=end15, values = values,percentile = percentile)
    elif type == "Out Of Zone":
        pitchers = pitchers[["player_name", "Season", "OOZ.Swing", "OOZ.xSwing", "OOZ"]]
        pitchers = pitchers.rename(columns={"player_name": "Name"})
        pitchers = pitchers.round(3)
        pitchers = pitchers.sort_values(by='OOZ', ascending=False)
        expected = "OOZ.xSwing (AVG - 0.292) - Average expected swing rate of all pitches thrown Out of the Strike Zone by the pitcher based on count/pitch type/location"
        influence = "OOZ (AVG - 0) - How much more or less likely a pitcher is to generate a swing Out of the Zone factoring in opposing hitter"
        whiff = ""
        woba = ""
        inzone = ""
        outofzone = "selected"
        stuffera = ""
        return render_template("pitchers.html", pitchers=pitchers, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, stuffera=stuffera, pitches=pitches, influence=influence,
                               expected=expected, text=text,start21=start21,start20=start20, start19=start19, start18=start18, start17=start17, start16=start16,
                           start15=start15,
                           end21=end21,end20=end20, end19=end19, end18=end18, end17=end17, end16=end16, end15=end15, values = values,percentile = percentile)
    elif type == "wOBA":
        pitchers = pitchers[["player_name","Season", "wOBA", "xwOBA", "In_wOBA"]]
        pitchers = pitchers.rename(columns={"player_name": "Name", "xwOBA" : "xLwOBA"})
        pitchers = pitchers.round(3)
        pitchers = pitchers.sort_values(by='In_wOBA', ascending=True)
        expected = "XLwOBA (AVG - 0.336) - Average expected wOBACon of all pitches thrown by the pitcher based on count/pitch type/location"
        influence = "In_wOBA (AVG - 0) - Amount above a below the expected wOBACon that we can attribute to the pitcher factoring in opposing hitter"
        whiff = ""
        woba = "selected"
        inzone = ""
        outofzone = ""
        stuffera = ""
        return render_template("pitchers.html", pitchers=pitchers, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, stuffera=stuffera, pitches=pitches, influence=influence,
                               expected=expected, text=text,start21=start21,start20=start20, start19=start19, start18=start18, start17=start17, start16=start16,
                           start15=start15,
                           end21=end21,end20=end20, end19=end19, end18=end18, end17=end17, end16=end16, end15=end15,values = values,percentile = percentile)
    else:
        pitchers = pitchers[["player_name","Season", "Command", "S_ERA"]]
        pitchers = pitchers.rename(columns={"player_name": "Name", "S_ERA": "StuffERA", "Command" : "rfCommand"})
        pitchers = pitchers.round(2)
        pitchers = pitchers.sort_values(by='StuffERA', ascending=True)
        expected = "Command (AVG - 0) - z-Score based metric that evaluates how much better than the average a given pitcher's location was based on expected outcomes"
        influence = "StuffERA (AVG 4.07) - ERA Based estimator that factors in all of the influence metrics and command"
        whiff = ""
        woba = ""
        inzone = ""
        outofzone = ""
        stuffera = "selected"
        return render_template("pitchers.html", pitchers=pitchers, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, stuffera=stuffera, pitches=pitches, influence=influence,
                               expected=expected, text=text,start21=start21,start20=start20, start19=start19, start18=start18, start17=start17, start16=start16,
                           start15=start15,
                           end21=end21,end20=end20, end19=end19, end18=end18, end17=end17, end16=end16, end15=end15, values = values,percentile = percentile)


@application.route("/hitters")
def hitters_page():
    hitters = pd.read_csv('all_seasons_hitters.csv', encoding = 'utf_8')
    values = "selected"
    percentile = ""
    hitters = hitters[hitters['Season'] == 2021]
    pitches = 250
    hitters = hitters[hitters["Pitches"] >= pitches]
    hitters = hitters[["Name","Season", "Whiff", "xWhiff", "In_Whiff"]]
    hitters = hitters.round(3)
    hitters = hitters.sort_values(by='In_Whiff', ascending=True)
    expected = "xWhiff (AVG - 0.105) - Average expected swing and miss rate of all pitches seen by the hitter based on count/pitch type/location"
    influence = "In_Whiff (AVG - 0) - How much more or less likely a hitter is to generate a swinging strike factoring in opposing pitcher"
    whiff = "selected"
    woba = ""
    inzone = ""
    outofzone = ""
    plate = ""
    start21 = "selected"
    start20 = ""
    start19 = ""
    start18 = ""
    start17 = ""
    start16 = ""
    start15 = ""
    end21 = "selected"
    end20 = ""
    end19 = ""
    end18 = ""
    end17 = ""
    end16 = ""
    end15 = ""
    return render_template("hitters.html", hitters=hitters, whiff=whiff, woba=woba, inzone=inzone,
                           outofzone=outofzone, plate=plate, pitches=pitches, influence=influence, expected=expected,
                           start21=start21,start20=start20, start19=start19, start18=start18, start17=start17, start16=start16,
                           start15=start15,
                           end21=end21,end20=end20, end19=end19, end18=end18, end17=end17, end16=end16, end15=end15, values = values,percentile = percentile)


@application.route("/hitters", methods=['POST'])
def hitters_table():
    pitches = int(request.form['pitches'])
    type = request.form['type']
    search = request.form['search']
    display = request.form['display']
    text = search
    search = search.strip()
    year = int(request.form['year'])
    yearend = int(request.form['yearend'])
    if year > yearend:
        end = year
        year = yearend
        yearend = end
    if year == 2021:
        start21 = "selected"
        start20 = ""
        start19 = ""
        start18 = ""
        start17 = ""
        start16 = ""
        start15 = ""
    elif year == 2020:
        start21 = ""
        start20 = "selected"
        start19 = ""
        start18 = ""
        start17 = ""
        start16 = ""
        start15 = ""
    elif year == 2019:
        start21 = ""
        start20 = ""
        start19 = "selected"
        start18 = ""
        start17 = ""
        start16 = ""
        start15 = ""
    elif year == 2018:
        start21 = ""
        start20 = ""
        start19 = ""
        start18 = "selected"
        start17 = ""
        start16 = ""
        start15 = ""
    elif year == 2017:
        start21 = ""
        start20 = ""
        start19 = ""
        start18 = ""
        start17 = "selected"
        start16 = ""
        start15 = ""
    elif year == 2016:
        start21 = ""
        start20 = ""
        start19 = ""
        start18 = ""
        start17 = ""
        start16 = "selected"
        start15 = ""
    else:
        start21 = ""
        start20 = ""
        start19 = ""
        start18 = ""
        start17 = ""
        start16 = ""
        start15 = "selected"
    if yearend == 2021:
        end21 = "selected"
        end20 = ""
        end19 = ""
        end18 = ""
        end17 = ""
        end16 = ""
        end15 = ""
    elif yearend == 2020:
        end21 = ""
        end20 = "selected"
        end19 = ""
        end18 = ""
        end17 = ""
        end16 = ""
        end15 = ""
    elif yearend == 2019:
        end21 = ""
        end20 = ""
        end19 = "selected"
        end18 = ""
        end17 = ""
        end16 = ""
        end15 = ""
    elif yearend == 2018:
        end21 = ""
        end20 = ""
        end19 = ""
        end18 = "selected"
        end17 = ""
        end16 = ""
        end15 = ""
    elif yearend == 2017:
        end21 = ""
        end20 = ""
        end19 = ""
        end18 = ""
        end17 = "selected"
        end16 = ""
        end15 = ""
    elif yearend == 2016:
        end21 = ""
        end20 = ""
        end19 = ""
        end18 = ""
        end17 = ""
        end16 = "selected"
        end15 = ""
    else:
        end21 = ""
        end20 = ""
        end19 = ""
        end18 = ""
        end17 = ""
        end16 = ""
        end15 = "selected"
    if display == "Percentile":
        hitters = pd.read_csv('all_seasons_hitters_percentile.csv', encoding = 'ISO-8859-1')
        percentile = "selected"
        values = ""
    else:
        hitters = pd.read_csv('all_seasons_hitters.csv', encoding = 'utf_8')
        percentile = ""
        values = "selected"
    hitters = hitters[hitters['Season'] <= yearend]
    hitters = hitters[hitters['Season'] >= year]
    if search is not None:
        hitters = hitters[hitters['Name'].str.contains(search, case=False)]
    hitters = hitters[hitters["Pitches"] >= pitches]
    if type == "Whiffs":
        hitters = hitters[["Name","Season", "Whiff", "xWhiff", "In_Whiff"]]
        hitters = hitters.round(3)
        hitters = hitters.sort_values(by='In_Whiff', ascending=True)
        expected = "xWhiff (AVG - 0.105) - Average expected swing and miss rate of all pitches seen by the hitter based on count/pitch type/location"
        influence = "In_Whiff (AVG - 0) - How much more or less likely a hitter is to generate a swinging strike factoring in opposing pitcher"
        whiff = "selected"
        woba = ""
        inzone = ""
        outofzone = ""
        plate = ""
        return render_template("hitters.html", hitters=hitters, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, plate=plate, pitches=pitches, influence=influence,
                               expected=expected, text = text,
                               start21=start21,start20=start20, start19=start19, start18=start18, start17=start17, start16=start16,
                               start15=start15,
                               end21=end21,end20=end20, end19=end19, end18=end18, end17=end17, end16=end16, end15=end15, values = values,percentile = percentile)
    elif type == "In-Zone":
        hitters = hitters[["Name","Season", "IZ.Swing", "IZ.xSwing", "IZ"]]
        hitters = hitters.round(3)
        hitters = hitters.sort_values(by='IZ', ascending=False)
        expected = "IZ.xSwing (AVG - 0.654) - Average expected swing rate of all pitches seen In the Strike Zone by the hitter based on count/pitch type/location"
        influence = "IZ (AVG - 0) - How much more or less likely a hitter is to generate a swing In the Zone factoring in opposing pitcher"
        whiff = ""
        woba = ""
        inzone = "selected"
        outofzone = ""
        plate = ""
        return render_template("hitters.html", hitters=hitters, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, plate=plate, pitches=pitches, influence=influence,
                               expected=expected, text = text,
                               start21=start21, start20=start20, start19=start19, start18=start18, start17=start17,
                               start16=start16,
                               start15=start15,
                               end21=end21, end20=end20, end19=end19, end18=end18, end17=end17, end16=end16, end15=end15, values = values,percentile = percentile)
    elif type == "Out Of Zone":
        hitters = hitters[["Name","Season", "OOZ.Swing", "OOZ.xSwing", "OOZ"]]
        hitters = hitters.round(3)
        hitters = hitters.sort_values(by='OOZ', ascending=True)
        expected = "OOZ.xSwing (AVG - 0.292) - Average expected swing rate of all pitches seen Out of the Strike Zone by the hitter based on count/pitch type/location"
        influence = "OOZ (AVG - 0) - How much more or less likely a hitter is to generate a swing Out of the Zone factoring in opposing pitcher"
        whiff = ""
        woba = ""
        inzone = ""
        outofzone = "selected"
        plate = ""
        return render_template("hitters.html", hitters=hitters, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, plate=plate, pitches=pitches, influence=influence,
                               expected=expected, text = text,
                               start21=start21, start20=start20, start19=start19, start18=start18, start17=start17,
                               start16=start16,
                               start15=start15,
                               end21=end21, end20=end20, end19=end19, end18=end18, end17=end17, end16=end16, end15=end15, values = values,percentile = percentile)
    elif type == "wOBA":
        hitters = hitters[["Name","Season", "wOBA", "xwOBA", "In_wOBA"]]
        hitters = hitters.rename(columns={"xwOBA": "xLwOBA"})
        hitters = hitters.round(3)
        hitters = hitters.sort_values(by='In_wOBA', ascending=False)
        expected = "xLwOBA (AVG - 0.336) - Average expected wOBACon of all pitches seen by the hitter based on count/pitch type/location"
        influence = "In_wOBA (AVG - 0) - Amount above a below the expected wOBACon that we can attribute to the hitter factoring in opposing pitcher"
        whiff = ""
        woba = "selected"
        inzone = ""
        outofzone = ""
        plate = ""
        return render_template("hitters.html", hitters=hitters, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, plate=plate, pitches=pitches, influence=influence,
                               expected=expected, text = text,
                               start21=start21, start20=start20, start19=start19, start18=start18, start17=start17,
                               start16=start16,
                               start15=start15,
                               end21=end21, end20=end20, end19=end19, end18=end18, end17=end17, end16=end16, end15=end15, values = values,percentile = percentile)
    else:
        hitters = hitters[["Name", "Season", "xwOBA_Swing", "xwOBA_Take", "SAE"]]
        hitters = hitters.rename(columns={"xwOBA_Swing": "xLwOBA_Swing","xwOBA_Take": "xLwOBA_Take" })
        hitters = hitters.round(3)
        hitters = hitters.sort_values(by='SAE', ascending=False)
        expected = "xLwOBA_Swing/xLwOBA_Take - Average expected wobaCon of all pitches either swung at or taken by a hitter based on location/count/pitch type"
        influence = "SAE - Percentage increase of the expected wOBACon a hitter swung at versus all pitches saw. 110 means a hitter swung at pitches with a expected wOBACon 10% better than all pitches he saw"
        whiff = ""
        woba = ""
        inzone = ""
        outofzone = ""
        plate = "selected"
        return render_template("hitters.html", hitters=hitters, whiff=whiff, woba=woba, inzone=inzone,
                               outofzone=outofzone, plate=plate, pitches=pitches, influence=influence,
                               expected=expected, text = text,
                               start21=start21, start20=start20, start19=start19, start18=start18, start17=start17,
                               start16=start16,
                               start15=start15,
                               end21=end21, end20=end20, end19=end19, end18=end18, end17=end17, end16=end16, end15=end15, values = values,percentile = percentile)

@application.route("/pitchergamelog")
def pitcher_game_log():
    by_game = pd.read_csv('by_game.csv', encoding="ISO-8859-1")
    list = by_game["player_name"].tolist()
    list = set(list)
    list = sorted(list)
    p1 = 'Jacob deGrom'
    stats = by_game[by_game['player_name'] == p1]
    stats = stats[["player_name", "game_date", "offense", "Pitches", "xWhiff", "xSwing_IZ",
                   "xSwing_OOZ",
                   "xLwOBA"]]
    stats = stats.rename(columns={"player_name": "Name",
                                  "offense": "Opp",
                                  "xSwing_IZ": "In-Zone",
                                  "xSwing_OOZ": "Out-Of-Zone",
                                  "game_date": "Date"})
    x = by_game[by_game['player_name'] == p1]['game_date'].to_list()
    y = by_game[by_game['player_name'] == p1]['xWhiff'].to_list()
    temp = by_game[by_game['player_name'] == p1]['Pitches'].to_list()
    names = [p1]
    fig = plt.figure()
    plt.scatter(x, y, c="blue", s=temp, figure=fig)
    plt.plot(x, y, c="blue")
    plt.suptitle('Game By Game Location Metrics')
    plt.title(p1)
    plt.xlabel("Game Date")
    plt.xticks(rotation=45)
    plt.ylabel("xWhiff")
    plt.axhline(y=10.5, color="black", linestyle="dotted")
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    whiff = "selected"
    woba = ""
    inzone = ""
    outofzone = ""
    selected = []
    for i in list:
        if i == p1:
            selected.append("selected")
        else:
            selected.append("")
    players = zip(list, selected)
    return render_template("game_plot.html", players=players,
                           plot=encoded,
                           stats=stats,
                           whiff=whiff,
                           woba=woba,
                           inzone=inzone,
                           outofzone=outofzone
                           )


@application.route("/pitchergamelog",methods=['POST'])
def pitcher_game_log_chart():
    type = request.form['type']
    player = request.form['player']
    by_game = pd.read_csv('by_game.csv', encoding="ISO-8859-1")
    list = by_game["player_name"].tolist()
    list = set(list)
    list = sorted(list)
    p1 = player
    stats = by_game[by_game['player_name'] == p1]
    stats = stats[["player_name", "game_date", "offense", "Pitches", "xWhiff", "xSwing_IZ",
                   "xSwing_OOZ",
                   "xLwOBA"]]
    stats = stats.rename(columns={"player_name": "Name",
                                  "offense": "Opp",
                                  "xSwing_IZ": "In-Zone",
                                  "xSwing_OOZ": "Out-Of-Zone",
                                  "game_date": "Date"})
    x = by_game[by_game['player_name'] == p1]['game_date'].to_list()
    temp = by_game[by_game['player_name'] == p1]['Pitches'].to_list()
    if type == "xWhiff":
        whiff = "selected"
        woba = ""
        inzone = ""
        outofzone = ""
        stat_avg = 10.5
        y = by_game[by_game['player_name'] == p1]['xWhiff'].to_list()
    elif type == "xLwOBA":
        whiff = ""
        woba = "selected"
        inzone = ""
        outofzone = ""
        stat_avg = 0.336
        y = by_game[by_game['player_name'] == p1]['xLwOBA'].to_list()
    elif type == "In-Zone":
        whiff = ""
        woba = ""
        inzone = "selected"
        outofzone = ""
        stat_avg = 65.4
        y = by_game[by_game['player_name'] == p1]['xSwing_IZ'].to_list()
    elif type == "Out-Of-Zone":
        whiff = ""
        woba = ""
        inzone = ""
        outofzone = "selected"
        stat_avg = 29.2
        y = by_game[by_game['player_name'] == p1]['xSwing_OOZ'].to_list()
    else:
        whiff = "selected"
        woba = ""
        inzone = ""
        outofzone = ""
        stat_avg = 10.5
        y = by_game[by_game['player_name'] == p1]['xWhiff'].to_list()
    names = [p1]
    fig = plt.figure()
    plt.scatter(x, y, c="blue", s=temp, figure=fig)
    plt.plot(x, y, c="blue")
    plt.suptitle('Game By Game Location Metrics')
    plt.title(p1)
    plt.xlabel("Game Date")
    plt.xticks(rotation=45)
    plt.ylabel(type)
    plt.axhline(y=stat_avg, color="black", linestyle="dotted")
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    selected = []
    for i in list:
        if i == p1:
            selected.append("selected")
        else:
            selected.append("")
    players = zip(list, selected)
    return render_template("game_plot.html", players=players,
                           plot=encoded,
                           stats=stats,
                           whiff=whiff,
                           woba=woba,
                           inzone=inzone,
                           outofzone=outofzone
                           )


@application.route("/prospects")
def prospects_page():
    prospects = pd.read_csv('prospects_2021.csv', encoding = 'utf_8')
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
    search = request.form['search']
    text = search
    search = search.strip()
    prospects = pd.read_csv('prospects_2021.csv', encoding = 'utf_8')
    if search is not None:
        prospects = prospects[prospects['Name'].str.contains(search,case=False)]
    if type == "Minors":
        prospects = prospects[prospects["PlayerID"].str.contains("sa")]
        prospects = prospects[["Name", "Value", "Adjusted Value", "Elite Rate"]]
        prospects = prospects.round(2)
        prospects = prospects.sort_values(by='Elite Rate', ascending=False)
        minors = "selected"
        all = ""
        return render_template("prospects.html", prospects=prospects, minors=minors, all=all, val = text)
    else:
        prospects = prospects[["Name", "Value", "Adjusted Value", "Elite Rate"]]
        prospects = prospects.round(2)
        prospects = prospects.sort_values(by='Elite Rate', ascending=False)
        minors = ""
        all = "selected"
        return render_template("prospects.html", prospects=prospects, minors=minors, all=all, val = text)


@application.route("/prospectchart")
def prospects_chart():
    comps = pd.read_csv('comps.csv', encoding="ISO-8859-1")
    milb = pd.read_csv('milb.csv', encoding="ISO-8859-1")
    colors = pd.read_csv('colors.csv', encoding="ISO-8859-1")
    list = comps["Key"].tolist()
    list = set(list)
    list = sorted(list)
    p1 = 'Jarren Duran BOS-AAA'
    p2 = ""
    zero = "selected"
    nonzero = ""
    team1 = milb[milb['PlayerList'] == p1]['Team'].values[0]
    x1 = comps[comps['Key'] == p1]['Total Val'].to_list()
    w1 = comps[comps['Key'] == p1]['W'].to_list()
    comps1 = comps[comps['Key'] == p1]
    comps1 = comps1[["Name", "Total Val", "Dist"]]
    w1 = [i / sum(w1) for i in w1]
    color = [colors[colors['name'] == team1]['primary'].values[0]]
    names = [p1]
    fig = plt.figure()
    plt.hist(x1, weights=w1, bins=20, color=color, label=names, edgecolor='black', linewidth=1.2, figure=fig)
    plt.suptitle('Comp Based Range Of Outcomes')
    plt.title(p1)
    plt.xlabel("Future Fantasy Impact")
    plt.ylabel("Weighted Probability")
    plt.axvline(x=round(np.average(x1, weights=w1), 2), color=colors[colors['name'] == team1]['primary'].values[0],
                linestyle="dotted")
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
    return render_template("prospect_chart.html", players=players, players2=players2, plot=encoded, zero=zero,
                           nonzero=nonzero, comps1 = comps1)


@application.route("/prospectchart", methods=['POST'])
def prospects_compare():
    p1 = request.form['player']
    p2 = request.form['player2']
    type = request.form['type']
    comps = pd.read_csv('comps.csv', encoding="ISO-8859-1")
    zero = "selected"
    nonzero = ""
    if type == "nonzero":
        comps = comps[comps['Total Val'] != 0]
        zero = ""
        nonzero = "selected"
    milb = pd.read_csv('milb.csv', encoding="ISO-8859-1")
    colors = pd.read_csv('colors.csv', encoding="ISO-8859-1")
    list = comps["Key"].tolist()
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
    team1 = milb[milb['PlayerList'] == p1]['Team'].values[0]
    x1 = comps[comps['Key'] == p1]['Total Val'].to_list()
    w1 = comps[comps['Key'] == p1]['W'].to_list()
    w1 = [i / sum(w1) for i in w1]
    comps1 = comps[comps['Key'] == p1]
    comps1 = comps1[["Name", "Total Val", "Dist"]]
    if p2 == "":
        color = [colors[colors['name'] == team1]['primary'].values[0]]
        names = [p1]
        fig = plt.figure()
        plt.hist(x1, weights=w1, bins=20, color=color, label=names, edgecolor='black', linewidth=1.2, figure=fig)
        plt.suptitle('Comp Based Range Of Outcomes')
        plt.title(p1)
        plt.xlabel("Future Fantasy Impact")
        plt.ylabel("Weighted Probability")
        plt.axvline(x=round(np.average(x1, weights=w1), 2),
                    color=colors[colors['name'] == team1]['primary'].values[0],
                    linestyle="dotted")
        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
        return render_template("prospect_chart.html", players=players, players2=players2, plot=encoded, comps1 = comps1)
    else:
        team2 = milb[milb['PlayerList'] == p2]['Team'].values[0]
        x2 = comps[comps['Key'] == p2]['Total Val'].to_list()
        w2 = comps[comps['Key'] == p2]['W'].to_list()
        w2 = [i / sum(w2) for i in w2]
        color = [colors[colors['name'] == team1]['primary'].values[0],
                 colors[colors['name'] == team2]['secondary'].values[0]]
        names = [p1, p2]
        fig = plt.figure()
        plt.hist([x1, x2], weights=[w1, w2], bins=20, color=color, label=names, edgecolor='black', linewidth=1.2,
                 figure=fig)
        plt.suptitle('Comp Based Range Of Outcomes')
        plt.title(p1 + " vs " + p2)
        plt.xlabel("Future Fantasy Impact")
        plt.ylabel("Weighted Probability")
        plt.axvline(x=round(np.average(x1, weights=w1), 2),
                    color=colors[colors['name'] == team1]['primary'].values[0],
                    linestyle="dotted")
        plt.axvline(x=round(np.average(x2, weights=w2), 2),
                    color=colors[colors['name'] == team2]['secondary'].values[0],
                    linestyle="dashed")
        plt.legend(loc='upper right', fontsize="small")
        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
        comps2 = comps[comps['Key'] == p2]
        comps2 = comps2[["Name", "Total Val", "Dist"]]
        return render_template("prospect_chart.html", players=players, players2=players2, plot=encoded, zero=zero,
                               nonzero=nonzero, comps1= comps1, comps2 = comps2)

@application.route("/projections")
def projections():
    catcher = ""
    first = ""
    second = ""
    third = ""
    short = ""
    outfield = ""
    all = "selected"
    projections = pd.read_csv('projections.csv', encoding = 'utf_8')
    list = projections["Team"].tolist()
    list = set(list)
    list = sorted(list)
    list.insert(0, "All")
    team = 'All'
    selected = []
    for i in list:
        if i == team:
            selected.append("selected")
        else:
            selected.append("")
    teams = zip(list, selected)
    return render_template("projections.html", projections=projections, catcher = catcher,
                           first = first,
                           second = second,
                           third = third,
                           short = short,
                           outfield = outfield,
                           all = all,
                           teams = teams)

@application.route("/projections",methods=['POST'])
def projections_filter():
    position = request.form['position']
    search = request.form['search']
    team = request.form['team']
    text = search
    search = search.strip()
    projections = pd.read_csv('projections.csv', encoding = 'utf_8')
    list = projections["Team"].tolist()
    list = set(list)
    list = sorted(list)
    list.insert(0, "All")
    selected = []
    for i in list:
        if i == team:
            selected.append("selected")
        else:
            selected.append("")
    teams = zip(list, selected)
    if team != "All":
        projections = projections[projections['Team'].str.contains(team, case=False)]
    if search is not None:
        projections = projections[projections['Player'].str.contains(search, case=False)]
    if position == "C":
        catcher = "selected"
        first = ""
        second = ""
        third = ""
        short = ""
        outfield = ""
        all = ""
        projections = projections[projections['Pos'].str.contains(position, case=False)]
        return render_template("projections.html", projections=projections, catcher=catcher,
                               first=first,
                               second=second,
                               third=third,
                               short=short,
                               outfield=outfield,
                               all=all,
                               teams=teams)
    elif position == "1B":
        catcher = ""
        first = "selected"
        second = ""
        third = ""
        short = ""
        outfield = ""
        all = ""
        projections = projections[projections['Pos'].str.contains(position, case=False)]
        return render_template("projections.html", projections=projections, catcher=catcher,
                               first=first,
                               second=second,
                               third=third,
                               short=short,
                               outfield=outfield,
                               all=all,
                               teams=teams)
    elif position == "2B":
        catcher = ""
        first = ""
        second = "selected"
        third = ""
        short = ""
        outfield = ""
        all = ""
        projections = projections[projections['Pos'].str.contains(position, case=False)]
        return render_template("projections.html", projections=projections, catcher=catcher,
                               first=first,
                               second=second,
                               third=third,
                               short=short,
                               outfield=outfield,
                               all=all,
                               teams = teams)
    elif position == "3B":
        catcher = ""
        first = ""
        second = ""
        third = "selected"
        short = ""
        outfield = ""
        all = ""
        projections = projections[projections['Pos'].str.contains(position, case=False)]
        return render_template("projections.html", projections=projections, catcher=catcher,
                               first=first,
                               second=second,
                               third=third,
                               short=short,
                               outfield=outfield,
                               all=all,
                               teams=teams)
    elif position == "SS":
        catcher = ""
        first = ""
        second = ""
        third = ""
        short = "selected"
        outfield = ""
        all = ""
        projections = projections[projections['Pos'].str.contains(position, case=False)]
        return render_template("projections.html", projections=projections, catcher=catcher,
                               first=first,
                               second=second,
                               third=third,
                               short=short,
                               outfield=outfield,
                               all=all,
                               teams=teams)
    elif position == "OF":
        catcher = ""
        first = ""
        second = ""
        third = ""
        short = ""
        outfield = "selected"
        all = ""
        projections = projections[projections['Pos'].str.contains(position, case=False)]
        return render_template("projections.html", projections=projections, catcher=catcher,
                               first=first,
                               second=second,
                               third=third,
                               short=short,
                               outfield=outfield,
                               all=all,
                               teams=teams)
    else:
        catcher = ""
        first = ""
        second = ""
        third = ""
        short = ""
        outfield = ""
        all = "selected"
        return render_template("projections.html", projections=projections, catcher=catcher,
                               first=first,
                               second=second,
                               third=third,
                               short=short,
                               outfield=outfield,
                               all=all,
                               teams=teams)

if __name__ == "__main__":
    application.run(port=4500)
