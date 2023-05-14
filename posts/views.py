from django.shortcuts import HttpResponse, render
from datetime import datetime
from posts.models import Product


def hello(request):
    return HttpResponse("Hello! It's my project")


def now_date(request):
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f"Current date and time: {current_date}")


def goodbye(request):
    return HttpResponse("Goodbye user!")


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        posts = Product.objects.all()

        context = {
            'posts': posts
        }

        return render(request, 'products/main.html', context=context)
