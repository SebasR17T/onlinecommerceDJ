from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Asignar el usuario al grupo correspondiente
            role = form.cleaned_data.get('role')
            if role == 'comprador':
                group = Group.objects.get(name='Comprador')
            elif role == 'tendero':
                group = Group.objects.get(name='Tendero')

            user.groups.add(group)
            login(request, user)  # Autentica al usuario después de registrarse
            return redirect('home')  # Cambia 'home' por la URL de destino tras el registro
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})
