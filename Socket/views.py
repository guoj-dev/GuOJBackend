import json
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,Http404

import GuOJBackend.Databases.models

# Create your views here.

def user(request,user_id):
    pass