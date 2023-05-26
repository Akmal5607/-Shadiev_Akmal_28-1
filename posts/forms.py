from django import forms
from posts.models import Product, Review


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'title', 'description', 'rate']


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
