from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from django.urls import reverse_lazy
from .models import Borrow
from .forms import BorrowForm
# Create your views here.

class BorrowListView(ListView):
    template_name = 'borrows_list.html'
    context_object_name = 'borrows'
    model = Borrow
    
class BorrowCreateView(CreateView):
    template_name = 'borrow_add.html'
    model = Borrow
    form_class = BorrowForm
    success_url = reverse_lazy('borrows_list')
    
class BorrowUpdateView(UpdateView):
    model = Borrow
    template_name = 'borrow_add.html'
    form_class = BorrowForm
    success_url = reverse_lazy('borrows_list')
    context_object_name = 'borrows'
