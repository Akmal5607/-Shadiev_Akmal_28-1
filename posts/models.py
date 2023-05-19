from django.db import models


class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(null=True, max_length=255)
    description = models.TextField(null=True)
    created_date = models.DateTimeField(null=True, auto_now_add=True)
    modified_date = models.DateTimeField(null=True, auto_now=True)
    rate = models.FloatField(null=True, default=0)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=256)
    post = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} - {self.text}'

