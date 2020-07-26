from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "bday/index.html", {
        "bday": now.month == 7 and now.day == 2
    })


