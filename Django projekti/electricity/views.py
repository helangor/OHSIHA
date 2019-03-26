from django.shortcuts import render
from django.conf import settings
import requests



def electricity(request):
    response = requests.get(
    url="https://api.fingrid.fi/v1/variable/event/json/192%2C193%2C188%2C181%2C191%2C189%2C201%2C205%2C202%2C194",
    headers={"x-api-key": settings.FINGRID_API_KEY},
    )

    data = response.json()
    for x in range(10):
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
