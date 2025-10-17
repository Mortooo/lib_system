from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from django.urls import reverse_lazy
from .models import Borrow
from .forms import BorrowForm
from django.contrib.auth.models import User
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
    
    def form_valid(self, form):
        
        user=User.objects.get(pk=self.kwargs['pk'])
        form.instance.user = user        
        return super().form_valid(form)
    
    # def get_context_data(self, **kwargs):
        
    #     context = super().get_context_data(**kwargs)
    #     borrow = self.object
        
    #     if borrow.return_date != None:
    #         context['days'] = (borrow.return_date - borrow.borrow_date).days
            
    #     return context
    
    
    
class BorrowUpdateView(UpdateView):
    model = Borrow
    template_name = 'borrow_add.html'
    form_class = BorrowForm
    success_url = reverse_lazy('borrows_list')
    context_object_name = 'borrows'
    
    
