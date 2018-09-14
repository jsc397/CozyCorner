from django.shortcuts import render, redirect
from .models import Bouquet
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def bouquet_list(request):
    bouquets = Bouquet.objects.all()
    # print(bouquets)
    return render(request, 'bouquet_list.html', {'bouquets': bouquets}) 

def users(request):
    users = User.objects.all()
    print(users)
    return render(request, 'user_page.html', {'users':users})

def create_bouquet(request):
    if request.method == 'POST':
        form = BouquetForm(request.POST)
        if form.is_valid():
            bouquet=form.save()
            return redirect('user_page.html', id=user.id)
        else:
            form = BouquetForm()
        return render(request, 'bouquet_form.html', {'form':form})

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
# def sign_up(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('user_list')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})
# def bouquet_detail(request):
#     bouquet = Bou


# Pseudocode : on click, match the 