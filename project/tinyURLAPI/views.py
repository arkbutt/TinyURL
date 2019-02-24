from django.shortcuts import render
from django.http import JsonResponse
import sqlite3
import hashlib
from .models import URL
from mongoengine import *

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def createURL(request):
    if request.method == 'GET':
        return HttpResponse("HELLOWORLD") #URL.objects.all()[0]['hash']
 #       z = int(x) + int(y)
    jsonData = json.loads(request.body)
    hash = computeMD5hash(jsonData["url"])
    url = URL(hash = hash, original_url = jsonData["url"])
    url.save()
 #   return HttpResponse("Hello, world. %s" %(str(z)))
    return JsonResponse({"status": "URL created", "hash": hash})

def getURL(request,hash):
    urls = URL.objects.filter(hash=hash)
    response = HttpResponse(status=302)
    response['Location'] = urls[0]['original_url']
    return response

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()
