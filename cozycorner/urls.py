from django.urls import path
from . import views

urlpatterns = [
    path ('', views.bouquet_list, name='bouquet_list'),
    path('accounts/signup', views.signup, name='signup'),
]