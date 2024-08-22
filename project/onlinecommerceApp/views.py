from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import CrearUsuarioForm
from .models import Usuario

def register(request):

    if request.method == 'POST': # Verifica si la solicitud es de tipo POST
        form = CrearUsuarioForm(request.POST) # Crea una instancia del formulario con los datos del POST
        if form.is_valid():
            user = form.save() # Guarda el usuario en la base de datos
            role = form.cleaned_data.get('role') # Solo asigna el usuario al grupo si se eligió un rol

            if role:
                if role == 'comprador':
                    group = Group.objects.get(name='Comprador')
                elif role == 'tendero':
                    group = Group.objects.get(name='Tendero')

                user.groups.add(group) # Añade el usuario al grupo correspondiente

            login(request, user) # Inicia sesión al usuario recién registrado
            return redirect('home')
    else:
        form = CrearUsuarioForm()

    # Renderiza la plantilla 'register.html' pasando el formulario como contexto
    return render(request, 'register.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import LoginForm

def login_view(request):
    error_message = None  # Inicializa el mensaje de error como None
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # Autentica al usuario con el nombre de usuario y la contraseña proporcionados
            user = form.get_user()
            if user is not None:
                # Inicia sesión al usuario
                auth_login(request, user)
                # Redirige a la página de inicio después del login
                return redirect('home')
        # Solo se establece el mensaje de error si el POST es inválido
        error_message = "Nombre de usuario o contraseña incorrectos."

    else:
        form = LoginForm()
        error_message = None  # Inicializa el mensaje de error como None

    # Renderiza la plantilla 'login.html' pasando el formulario y el mensaje de error como contexto
    return render(request, 'login.html', {'form': form, 'error_message': error_message})