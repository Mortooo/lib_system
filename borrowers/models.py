from django.db import models

# Create your models here.
class Borrower(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    address = models.CharField(max_length=100,blank=False,null=False)
    telephone = models.CharField(max_length=10,blank=False,null=False)
    email = models.CharField(max_length=50,blank=True,null=True)
    id_image = models.ImageField(upload_to="borrowers/NIDS",blank=True,null=True)

    def __str__(self):
        return self.name
