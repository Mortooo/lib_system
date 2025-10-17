from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Borrow
from .forms import BorrowForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect


# Create your views here.

class BorrowListView(ListView):
    template_name = 'borrows_list.html'
    context_object_name = 'borrows'
    model = Borrow
    
    def get_queryset(self):
        
        borrows = Borrow.objects.all()

        if self.request.GET.get('q') or self.request.GET.get('status'):
            search_item = self.request.GET.get('q')
            search_status = self.request.GET.get('status')


            borrows = borrows.filter(Q(book__title__icontains=search_item)|Q(borrower__name__contains=search_item))

            if(search_status):
                if(search_status == 'returned'):
                    borrows = borrows.filter(is_returned=True)
                elif(search_status == 'not_returned'):
                    borrows = borrows.filter(is_returned=False)
                else:
                    pass


        return borrows
    
class BorrowCreateView(CreateView):
    template_name = 'borrow_add.html'
    model = Borrow
    form_class = BorrowForm
    success_url = reverse_lazy('borrows_list')
    
    def form_valid(self, form):
        
        user=User.objects.get(pk=self.kwargs['pk'])
        form.instance.user = user        
        return super().form_valid(form)
      
class BorrowUpdateView(UpdateView):
    model = Borrow
    template_name = 'borrow_add.html'
    form_class = BorrowForm
    success_url = reverse_lazy('borrows_list')
    context_object_name = 'borrows'
    

def borrowsDeleteView(self, status):
    
   
    if self.method == 'POST':
        if status == 'all':
            Borrow.objects.all().delete()
        elif status == 'some':
            Borrow.objects.filter(is_returned=True).delete()
        else:
            pass
        
        return redirect('borrows_list')
    
    return render(self, 'borrows_delete.html')
    
    
    
    
