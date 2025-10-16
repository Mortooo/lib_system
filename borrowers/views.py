from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

from borrowers.models import Borrower
from .forms import BorrowerForm


# Create your views here.
class BorrowerListView(ListView):
    model = Borrower
    context_object_name = 'borrowers'
    template_name = 'borrowers_list.html'
    
    def get_queryset(self):
        
        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            return Borrower.objects.filter(name__icontains=query).order_by('id')
        
        return Borrower.objects.all()
    


class BorrowerCreateView(CreateView):
    
    template_name = 'borrower_add.html'
    context_object_name = 'borrowers'
    model = Borrower
    form_class = BorrowerForm
    success_url = reverse_lazy('borrowers_list')
    
class BorrowerDeleteView(DeleteView):
    model = Borrower
    template_name = 'borrower_delete.html'
    success_url = reverse_lazy('borrowers_list')
    context_object_name = 'borrower'

class BorrowerUpdateView(UpdateView):
    model = Borrower
    template_name = 'borrower_add.html'
    form_class = BorrowerForm
    success_url = reverse_lazy('borrowers_list')
    context_object_name = 'borrowers'
    