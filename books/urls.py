from django.contrib import admin
from django.urls import path
from .views import BookListView, BookDeletetView, BookAddView, BookUpdateView,home
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('list/', login_required(BookListView.as_view()),name='books_list'),
    path('add/', login_required(BookAddView.as_view()), name='book_add'),
    path('update/<int:pk>', login_required(BookUpdateView.as_view()), name='book_update'),
    path('delete/<int:pk>', login_required(BookDeletetView.as_view()), name='book_delete'),
]
