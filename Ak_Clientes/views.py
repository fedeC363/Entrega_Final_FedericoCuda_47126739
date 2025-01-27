from django.shortcuts import render

def index(request):
    return render(request, 'Ak_Clientes/index.html')

def about(request):
    return render(request, 'Ak_Clientes/about_me.html')