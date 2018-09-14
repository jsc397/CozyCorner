from django.shortcuts import render, redirect
from .models import Bouquet
# from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def bouquet_list(request):
    bouquets = Bouquet.objects.all()
    return render(request, 'bouquet_list.html', {'bouquets': bouquets}) 

# def user_list(request):
#     users = User.objects.all()
#     print(users)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
