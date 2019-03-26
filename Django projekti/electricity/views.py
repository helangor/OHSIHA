from django.shortcuts import render
import requests

def electricity(request):
    response = requests.get('https://api.ipify.org/?format=json')
    geodata = response.json()
    return render(request, 'electricity/energy.html', {
        'ip': geodata['ip'],
    })