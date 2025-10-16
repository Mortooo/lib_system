from django.contrib import admin
from django.urls import path
from .views import BorrowerListView,BorrowerCreateView,BorrowerDeleteView,BorrowerUpdateView

urlpatterns = [
    path('list/',BorrowerListView.as_view(),name='borrowers_list'),
    path('add/', BorrowerCreateView.as_view(), name='borrower_add'),
    path('update/<int:pk>', BorrowerUpdateView.as_view(), name='borrower_update'),
    path('delete/<int:pk>', BorrowerDeleteView.as_view(), name='borrower_delete'),

]
