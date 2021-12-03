from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    category = models.ForeignKey(Category,
                                 on_delete=models.RESTRICT,
                                 related_name='products')

    def __str__(self):
        return self.name
