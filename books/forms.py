from django.forms import ModelForm
from django import forms

from books.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'total_copies','cover','available_copies']
        labels = {
            'title': 'العنوان',
            'author': 'المؤلف',
            'isbn': 'رقم ISBN',
            'total_copies': 'إجمالي النسخ',
            'available_copies': 'النسخ المتاحة',
            'cover': 'صورة الغلاف',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'border  px-3 rounded-3xl py-2 w-full'}),
            'author': forms.Select(attrs={'class': 'border  px-3 rounded-3xl py-2 w-full'}),
            'isbn': forms.TextInput(attrs={'class': 'border  px-3 rounded-3xl py-2 w-full'}),
            'total_copies': forms.NumberInput(attrs={'class': 'border  px-3 rounded-3xl py-2 w-full'}),
            'cover': forms.ClearableFileInput(attrs={'class': 'border  rounded-3xl px-3 py-2 w-full'})}

    def clean(self):
        cleaned_data = super().clean()
        total = cleaned_data.get('total_copies')
        available = cleaned_data.get('available_copies')

        print(f" total: {total}, available: {available}")
        #  If available_copies is empty, set it equal to total_copies
        if total is not None and (available is None or available == ''):
            cleaned_data.update({'available_copies': total})

        # if user add empty title for the book
        if not cleaned_data.get('title'):
            raise forms.ValidationError('الرجاء ادخال عنوان الكتاب')

        #if the user add more than 1,000,000 copy
        if cleaned_data.get('total_copies')>=1000000:
            raise forms.ValidationError('أقصى عدد مسموح به اقل من مليون نسخة !')


        return cleaned_data




