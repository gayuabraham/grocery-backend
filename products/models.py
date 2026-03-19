from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image1 = models.CharField(max_length=500)
    image2 = models.CharField(max_length=500)
    stock = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name