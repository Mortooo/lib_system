from django.contrib import admin
from django.urls import path
from .views import BorrowerListView,BorrowerCreateView,BorrowerDeleteView,BorrowerUpdateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('list/',login_required(BorrowerListView.as_view()),name='borrowers_list'),
    path('add/', login_required(BorrowerCreateView.as_view()), name='borrower_add'),
    path('update/<int:pk>', login_required(BorrowerUpdateView.as_view()), name='borrower_update'),
    path('delete/<int:pk>', login_required(BorrowerDeleteView.as_view()), name='borrower_delete'),

]
