from django.contrib import admin
from django.urls import path

from posts.views import hello, now_date, goodbye, main_view, products_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', hello, name='hello'),
    path('now_date/', now_date, name='now_date'),
    path('goodbye/', goodbye, name='goodbye'),
    path('', main_view),
    path('posts/', products_view)
]

