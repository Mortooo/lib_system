from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from books.forms import BookForm
from books.models import Book


# Create your views here.

def home(request):

    return render(request, 'home.html')

class BookListView(ListView):
    template_name = 'list.html'
    context_object_name = 'books'
    model = Book

    def get_queryset(self):

        all_books = Book.objects.all();

        if self.request.GET.get('q') or self.request.GET.get('status'):
            search_item = self.request.GET.get('q')
            search_status = self.request.GET.get('status')


            all_books = all_books.filter(Q(title__icontains=search_item)|Q(author__name__contains=search_item))

            if(search_status):
                if(search_status == 'available'):
                    all_books = all_books.filter(available_copies__gt=0)
                elif(search_status == 'unavailable'):
                    all_books = all_books.filter(available_copies__lte=0)
                else:
                    pass


        return all_books





class BookDeletetView(DeleteView):
    template_name = 'delete.html'
    context_object_name = 'book'
    model = Book
    success_url = reverse_lazy('books_list')

class BookAddView(CreateView):
    template_name = 'add.html'
    context_object_name = 'book'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books_list')

class BookUpdateView(UpdateView):
    template_name = 'add.html'
    context_object_name = 'book'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books_list')


