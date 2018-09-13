from django.shortcuts import render
from .models import Bouquet, Favorite

# Create your views here.
def bouquet_list(request):
    bouquets = Bouquet.objects.all()
    return render(request, 'bouquet_list.html', {'bouquets': bouquets}) 

# def bouquet_detail(request):
#     bouquet = Bou


# Pseudocode : on click, match the 