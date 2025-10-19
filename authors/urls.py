from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AuthorsListView,AuthorDeleteView,AuthorCreateView,AuthorUpdateView


urlpatterns = [
    path('list',login_required(AuthorsListView.as_view()),name='authors_list'),
    path('delete/<int:pk>',login_required(AuthorDeleteView.as_view()),name='author_delete'),
    path('update/<int:pk>',login_required(AuthorUpdateView.as_view()),name='author_update'),
    path('add',login_required(AuthorCreateView.as_view()),name='author_add'),
    
]
