from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import PageCount

def index(request):
    row, create = PageCount.objects.get_or_create(page='index')
    row.visits += 1
    row.save()
    document = ""
    return HttpResponse("Hello, visiter #" + str(row.visits) + " at " + time.strftime("%c"))