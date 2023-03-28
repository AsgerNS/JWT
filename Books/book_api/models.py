from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


class OrderBook(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
