from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def main(req):
    _ = requests.get("https://ipfind.co/?ip=196.21.104.1&auth=7b98da30-ff64-4429-ae6a-10d87d82ed4e")
    data = _.json()
    return render(req, 'index.html', {"data": data})