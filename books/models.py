from django.db import models

from authors.models import Author


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100,blank=False,null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    total_copies = models.PositiveIntegerField(max_length=10)
    available_copies = models.IntegerField(blank=True, null=True)
    cover = models.ImageField(upload_to='books/cover',blank=True,null=True)
    isbn = models.CharField(max_length=11,blank=True,null=True)

    def __str__(self):
        return self.title

