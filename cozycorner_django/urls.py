"""cozycorner_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from cozycorner import views as cozycorner_views


# from django.conf.urls import include

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('cozycorner.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', cozycorner_views.signup, name='signup'),
    # path('accounts/login/', auth_views.login, name='login'),
    # path('accounts/logout/', auth_views.logout, name='logout'),
    # path('accounts/signup/', tunr_views.sign_up, name='signup'),
]
