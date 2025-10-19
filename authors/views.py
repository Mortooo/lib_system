from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Author
from django.urls import reverse_lazy
from .forms import AuthorForm


# Create your views here.

class AuthorsListView(ListView):
    template_name='authors_list.html'
    model=Author
    context_object_name='authors'
    
    
class AuthorCreateView(CreateView):
    template_name='author_add.html'
    model=Author
    success_url=reverse_lazy('authors_list')
    form_class=AuthorForm
    
class AuthorUpdateView(UpdateView):
    template_name='author_add.html'
    model=Author
    success_url=reverse_lazy('authors_list')
    form_class=AuthorForm
    
class AuthorDeleteView(DeleteView):
    template_name='author_delete.html'
    model=Author
    success_url=reverse_lazy('authors_list')
    
    
    
