from django.shortcuts import render
from django.conf import settings
from datetime import datetime, timedelta
import requests


"""
def electricity(request):
    response = requests.get(
    url="https://api.fingrid.fi/v1/variable/event/json/192%2C193%2C188%2C181%2C191%2C189%2C201%2C205%2C202%2C194",
    headers={"x-api-key": settings.FINGRID_API_KEY},
    )

    data = response.json()
    for x in range(len(data)):
        if data[x]['variable_id'] == 192:
            tuotanto = data[x]['value']
        elif data[x]['variable_id'] == 193:
            kulutus = data[x]['value']
        elif data[x]['variable_id'] == 194:
            tuontivienti = data[x]['value']
        elif data[x]['variable_id'] == 188:
            ydinvoima = data[x]['value']
        elif data[x]['variable_id'] == 181:
            tuulivoima = data[x]['value']
        elif data[x]['variable_id'] == 191:
            vesivoima = data[x]['value']
        elif data[x]['variable_id'] == 202:
            yhteistuotanto = data[x]['value']
        elif data[x]['variable_id'] == 201:
            kauko = data[x]['value']
        else:
            muu = data[x]['value']

    return render(request, 'electricity/energy.html', { 
    'tuotanto' : tuotanto,
    'kulutus' : kulutus,
    'tuontivienti' : tuontivienti,
    'ydinvoima' : ydinvoima,
    'tuulivoima' : tuulivoima,
    'vesivoima' : vesivoima,
    'yhteistuotanto' : yhteistuotanto,
    'kauko' : kauko,
    'muu' : muu,
        })
"""

def timeline(request):
    timenow = datetime.now().strftime("%Y-%m-%d") + "T16%3A46%3A00%2B0000"
    timelastyear = datetime.now() - timedelta(weeks = 25)
    timelastyear = timelastyear.strftime("%Y-%m-%d") + "T16%3A46%3A00%2B0000"

    urli='https://api.fingrid.fi/v1/variable/192/events/json?start_time={}&end_time={}'.format(timelastyear, timenow)
    url2='https://api.fingrid.fi/v1/variable/193/events/json?start_time={}&end_time={}'.format(timelastyear, timenow)

    response = requests.get(
    url=urli,
    headers={"x-api-key": 'uLwMWQp2Lp3RCOj3QjHLG6Bdhm3SjTglyE5d4WV5'},
    )

    data = response.json()
    tuotantoarvot=[]
    for i in range(0, len(data), 480):
        tuotantoarvot.append(data[i]['value'])
    
    response = requests.get(
    url=url2,
    headers={"x-api-key": 'uLwMWQp2Lp3RCOj3QjHLG6Bdhm3SjTglyE5d4WV5'},
    )

    data = response.json()
    kulutusarvot=[]
    for i in range(0, len(data), 480):
        kulutusarvot.append(data[i]['value'])

    return render(request, 'electricity/energy.html', { 
    'tuotantoajalta' : tuotantoarvot,
    'kulutusajalta' : kulutusarvot,
        })

