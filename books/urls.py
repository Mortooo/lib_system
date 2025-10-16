from django.contrib import admin
from django.urls import path
from .views import BookListView, BookDeletetView, BookAddView, BookUpdateView

urlpatterns = [
    path('list/',BookListView.as_view(),name='books_list'),
    path('add/', BookAddView.as_view(), name='book_add'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:pk>', BookDeletetView.as_view(), name='book_delete'),

]
