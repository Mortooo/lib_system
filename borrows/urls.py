
from django.urls import path
from django.contrib.auth.decorators import login_required
from borrows.views import BorrowListView, BorrowCreateView, BorrowUpdateView
from . import views

urlpatterns = [
    path('list/', login_required(views.BorrowListView.as_view()), name='borrows_list'),
    path('add/', login_required(views.BorrowCreateView.as_view()), name='borrow_add'),
    path('update/<int:pk>/', login_required(views.BorrowUpdateView.as_view()), name='borrow_update'),   
]
