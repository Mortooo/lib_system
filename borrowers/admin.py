from django.contrib import admin

from books.models import Book
from borrowers.models import Borrower

# Register your models here.
admin.site.register(Borrower)
