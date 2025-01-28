from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'Ak_Clientes/index.html')
@login_required
def about(request):
    return render(request, 'Ak_Clientes/about_me.html')