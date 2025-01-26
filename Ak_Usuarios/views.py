from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

#Crear un usuario
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente. ¡Ahora puedes iniciar sesión!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Ak_Usuarios/registro.html', {'form': form})

