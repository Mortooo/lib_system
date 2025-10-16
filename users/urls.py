from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('list/', login_required(views.UserListView.as_view()), name='users_list'),
    path('add/', login_required(views.UserCreateView.as_view()), name='user_add'),
    path('delete/<int:pk>/', login_required(views.UserDeleteView.as_view()), name='user_delete'),
    path('update/<int:pk>/', login_required(views.UserUpdateView.as_view()), name='user_update'),
   
]