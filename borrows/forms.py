from django import forms
from .models import Borrow
from datetime import date

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['user', 'book','borrower','return_date','is_returned','borrow_date']
        exclude = ['user']
        widgets = {
            'user': forms.Select(attrs={'class': 'border  px-3  py-2 w-full'}),
            'book': forms.Select(attrs={'class': 'border  px-3  py-2 w-full'}),
            'borrower': forms.Select(attrs={'class': 'border  px-3  py-2 w-full'}),
            'borrow_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
            'is_returned': forms.CheckboxInput(attrs={'class': 'border  px-3  py-2 w-6 h-6'}),}
        labels = {
            'user': 'المستخدم',
            'book': 'الكتاب',
            'borrower': 'المقترض',
            'borrow_date': 'تاريخ الاستعارة',
            'return_date': 'تاريخ الإرجاع',
            'is_returned': 'الحالة'
        }
    
  
 
        
   
    def clean(self):

        cleaned_data=super().clean()  
        book=cleaned_data.get('book')       
    
        #check if it's a new borrow  or returning or updating  
        if self.instance.pk is None: # New borrow instance 
            
            if  book.available_copies <=0:
                 raise forms.ValidationError('لا توجد نسخ متاحة من هذا الكتاب !')
            else:
                book.available_copies -= 1
                book.save()
        
        else:# updating  or returning
            
            if cleaned_data.get('is_returned'):# returning the book
                # The book is being returned now
                book.available_copies += 1
                book.save()
            
        return cleaned_data
    
    
    def __init__(self, *args, **kwargs):
        super(BorrowForm, self).__init__(*args, **kwargs)
        
        if not self.instance.pk:
            self.initial['borrow_date']=date.today()
        

        if self.instance.pk:
            # If the instance exists (i.e., it's an update), disable the 'user' and 'book' fields
            self.fields['book'].disabled = True
            self.fields['borrower'].disabled = True

        else:
            self.fields['is_returned'].disabled = True
            
        
    
    
            
            
        
            
            