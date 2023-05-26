from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from posts.views import (
    hello, now_date, goodbye, main_view, products_view,
    product_detail_view, create_product, create_review
)
from djangoProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello, name='hello'),
    path('now_date/', now_date, name='now_date'),
    path('goodbye/', goodbye, name='goodbye'),
    path('', main_view),
    path('posts/', products_view, name='product_list'),
    path('posts/<int:id>/', product_detail_view, name='product_detail'),
    path('posts/create/', create_product, name='product_create'),
    path('posts/<int:product_id>/review/', create_review, name='review_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
