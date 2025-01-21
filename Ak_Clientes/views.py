from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Ak_Clientes/index.html')

def fede(request):
    return render(request,'Ak_Clientes/fede.html')  