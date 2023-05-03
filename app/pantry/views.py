from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def index(req):
        return HttpResponse("Main Page.")

def show(req, pantry_id):
        return HttpResponse(f'viewing pantry with id: {pantry_id}')

def modify(req, pantry_id):
        return HttpResponse(f'Where ingredients can be modified to pantry with id: {pantry_id}')