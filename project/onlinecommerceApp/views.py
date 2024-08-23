from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import LoginForm
from .forms import CrearUsuarioForm, ProductForm
from .models import Producto
from django.views.generic import TemplateView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
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
            return redirect('dashboard')
    else:
        form = CrearUsuarioForm()
    # Renderiza la plantilla 'register.html' pasando el formulario como contexto
    return render(request, 'register.html', {'form': form})



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
                return redirect('crear_producto')
        # Solo se establece el mensaje de error si el POST es inválido
        error_message = "Nombre de usuario o contraseña incorrectos."
    else:
        form = LoginForm()
        error_message = None  # Inicializa el mensaje de error como None
    # Renderiza la plantilla 'login.html' pasando el formulario y el mensaje de error como contexto
    return render(request, 'login.html', {'form': form, 'error_message': error_message})


class ProductUpdateView(UpdateView):
    model = Producto
    form_class = ProductForm
    template_name = 'productUpdate.html'
    success_url = reverse_lazy('listar_producto')

    def get_form_kwargs(self):
        kwarg = super().get_form_kwargs()
        kwarg['user'] = self.request.user
        return kwarg

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
class ProductCreateView(CreateView):
    model = Producto
    form_class = ProductForm
    template_name = 'createProduct.html'
    success_url = reverse_lazy('listar_producto')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Añadir el usuario actual a los argumentos del formulario
        kwargs['user'] = self.request.user
        return kwargs
    def form_valid(self, form):
        # Llamar al método de guardado del formulario
        response = super().form_valid(form)
        # Puedes hacer algo adicional después de que el formulario se haya guardado si es necesario
        return response

class ProductListView(ListView):
    model = Producto
    template_name = 'product_list.html'  # Nombre del archivo HTML para renderizar la lista
    context_object_name = 'productos'  # Nombre del contexto para acceder a los productos en la plantilla
    def get_queryset(self):
        # Personaliza la consulta si es necesario
        return Producto.objects.all()



class ProductDetailView(DetailView):
    model = Producto
    template_name = 'productDetail.html'


class ProductDeleteView(DeleteView):
    model = Producto
    template_name = 'productDelete.html'
    success_url = reverse_lazy('listar_producto')
