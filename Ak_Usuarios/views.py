from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserEditForm, ProfileEditForm
from .models import Profile


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

#Editar un usuario
def editarPerfil(request):
    usuario = request.user
    try:
        perfil = usuario.profile
    except Profile.DoesNotExist:
        perfil = Profile.objects.create(user=usuario)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=usuario)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('menu')
    else:
        user_form = UserEditForm(instance=usuario)
        profile_form = ProfileEditForm(instance=perfil)

    return render(request, "Ak_Usuarios/editar_perfil.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "usuario": usuario,
    })




