from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.models import User
from .forms import UserForm
from django.urls import reverse_lazy


# Create your views here.
class UserListView(ListView):
    template_name = 'users_list.html'
    context_object_name = 'users'
    model = User
    
class UserCreateView(CreateView):
    template_name = 'user_add.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('users_list')
    context_object_name = 'user'
    
class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_add.html'
    form_class = UserForm
    success_url = reverse_lazy('users_list')
    context_object_name = 'users'
    