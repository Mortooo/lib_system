from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Borrow(models.Model):
    
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    borrower = models.ForeignKey('borrowers.Borrower', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=False, null=False)
    is_returned = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.book.title} borrowed by {self.borrower.name}"