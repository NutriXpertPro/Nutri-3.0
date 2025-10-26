from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def evaluation_list(request):
    return render(request, 'evaluations/evaluation_list.html')
