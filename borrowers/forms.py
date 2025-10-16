from django.forms import ModelForm
from .models import Borrower
from django import forms

class BorrowerForm(ModelForm):
    class Meta:
        model=Borrower
        fields=['name','address','email','telephone','id_image']
        
        labels = {
            'name': 'الإسم ',
            'address': 'العنوان',
            'telephone': 'رقم الهاتف ',
            'email': 'البريد الإلكتروني ',
            'id_image': 'اثبات الهوية ',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border  px-3 rounded-3xl py-2 w-full'}),
            'address': forms.TextInput(attrs={'class': 'border  px-3 rounded-3xl py-2 w-full'}),
            'telephone': forms.TextInput(attrs={'class': 'border  px-3 rounded-3xl py-2 w-full'}),
            'email': forms.TextInput(attrs={'class': 'border  px-3 rounded-3xl py-2 w-full'}),
            'id_image': forms.ClearableFileInput(attrs={'class': 'border  rounded-3xl px-3 py-2 w-full'})}
    