from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='product',on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField(null=True,blank=True)
    product_available = models.BooleanField()
    image_url = models.URLField(max_length=2083)

    def __str__(self):
        return self.title