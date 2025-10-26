from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def diet_list(request):
    return render(request, 'diets/diet_list.html')

@login_required
def diet_create(request):
    return render(request, 'diets/diet_create.html')
