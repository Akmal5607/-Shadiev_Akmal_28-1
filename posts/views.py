from django.shortcuts import HttpResponse, render, redirect
from datetime import datetime
from posts.models import Product, Review
from posts.forms import ProductCreateForm, ReviewCreateForm


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
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/main.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        post = Product.objects.get(id=id)
        context = {
            'post': post
        }
        return render(request, 'products/detail.html', context=context)


def create_product(request):
    if request.method == 'GET':
        form = ProductCreateForm()
        context = {
            'form': form
        }
        return render(request, 'products/create.html', context=context)
    elif request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            context = {
                'form': form
            }
            return render(request, 'products/create.html', context=context)


def create_review(request, product_id):
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.post_id = product_id
            review.save()
            return redirect('product_detail', id=product_id)
    else:
        form = ReviewCreateForm()
    context = {
        'form': form
    }
    return render(request, 'products/review_create.html', context=context)
