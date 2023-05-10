from django.shortcuts import HttpResponse
from datetime import datetime


def hello(request):
    return HttpResponse("Hello! It's my project")


def now_date(request):
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f"Current date and time: {current_date}")


def goodbye(request):
    return HttpResponse("Goodbye user!")
