from django.urls import path
from . import views

urlpatterns = [
    path ('', views.bouquet_list, name='bouquet_list'),
    path('accounts/signup', views.signup, name='signup'),
    path('users', views.users, name="user"),
    path('bouquet/new', views.create_bouquet, name='bouquet'),
]