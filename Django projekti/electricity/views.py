from django.shortcuts import render
from django.conf import settings
import requests

def electricity(request):
    #response = requests.get('https://api.ipify.org/?format=json')
    response = requests.get(
    url="https://api.fingrid.fi/v1/variable/event/json/188%2C181",
    headers={
        "x-api-key": settings.FINGRID_API_KEY,
    },
    )

    data = response.json()
    return render(request, 'electricity/energy.html', {
        'Value': data[0]['value'],
    })
