from .models import Author
from django.forms import ModelForm
from django import forms


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name','biography']
        
        lables = {
            'name' : 'اسم المؤلف',
            'biography' : 'السيرة الذاتية'
        }
        
        widgets = {
            'name':forms.TextInput(attrs={'class': 'border  px-3 rounded-3xl py-2 w-full'}),
            'biography' : forms.Textarea(attrs={'class': 'border  px-3 rounded-3xl py-2 w-full'})}
        
        
