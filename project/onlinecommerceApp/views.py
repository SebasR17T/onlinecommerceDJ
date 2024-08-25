from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from .forms import LoginForm, TiendaForm, InventarioForm
from .forms import CrearUsuarioForm, ProductForm
from .models import Producto, Tienda, Inventario
from django.views.generic import TemplateView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin

class TenderoRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Tendero').exists()

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

    def get_queryset(self):
        # Filtra los productos para asegurarse de que el tendero solo pueda editar sus productos
        tienda = get_object_or_404(Tienda, id_usuario=self.request.user)
        return Producto.objects.filter(inventario__id_tienda=tienda)

    def form_valid(self, form):
        form.instance.id_usuario_modificacion = self.request.user
        return super().form_valid(form)

class ProductCreateView(TenderoRequiredMixin, CreateView):
    model = Producto
    form_class = ProductForm
    template_name = 'createProduct.html'
    success_url = reverse_lazy('listar_producto')

    def form_valid(self, form):
        # Asignar el usuario actual al producto
        form.instance.id_usuario_creacion = self.request.user

        # Guarda el producto primero antes de crear una entrada en el inventario
        response = super().form_valid(form)

        # Seleccionar la primera tienda asociada al usuario actual
        tienda = Tienda.objects.filter(id_usuario=self.request.user).first()
        if not tienda:
            # Manejar el caso en el que no hay tiendas asociadas al usuario
            return redirect('error_page')  # Redirige a una página de error o muestra un mensaje

        # Crear una entrada en el inventario para el nuevo producto
        Inventario.objects.create(
            id_tienda=tienda,
            id_producto=form.instance,  # El producto ya está guardado en este punto
            cantidad=0,  # Ajusta la cantidad según sea necesario
            id_usuario_creacion=self.request.user
        )

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


class ProductDeleteView(TenderoRequiredMixin, DeleteView):
    model = Producto
    template_name = 'productDelete.html'
    success_url = reverse_lazy('listar_producto')



class TiendaCreateView(TenderoRequiredMixin, CreateView):
    model = Tienda
    form_class = TiendaForm
    template_name = 'tiendaCreate.html'
    success_url = reverse_lazy('listar_tienda')

    def form_valid(self, form):
        form.instance.id_usuario = self.request.user  # Asigna el usuario actual como gestor de la tienda
        return super().form_valid(form)

class TiendaListView(ListView):
    model = Tienda
    template_name = 'tiendaList.html'  # El nombre del template que se utilizará para renderizar la vista
    context_object_name = 'tiendas'  # Nombre de la variable de contexto en el template

    def get_queryset(self):
        # Puedes personalizar la consulta si es necesario
        return Tienda.objects.all()

class TiendaDetailView(DetailView):
    model = Tienda
    template_name = 'tiendaDetail.html'
    context_object_name = 'tienda'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tienda = self.object
        context['tienda_id'] = tienda.id_tienda  # Agregar el ID de la tienda al contexto
        # Obtener los inventarios de la tienda
        inventarios = Inventario.objects.filter(id_tienda=tienda)
        context['inventarios'] = inventarios
        # Obtener productos de los inventarios de la tienda
        productos = Producto.objects.filter(inventario__id_tienda=tienda).distinct()
        context['productos'] = productos
        return context


class TiendaUpdateView(TenderoRequiredMixin, UpdateView):
    model = Tienda
    form_class = TiendaForm
    template_name = 'tiendaUpdate.html'
    success_url = reverse_lazy('listar_tienda')

    def form_valid(self, form):
        # Puedes realizar acciones adicionales aquí si es necesario
        return super().form_valid(form)

class TiendaDeleteView(TenderoRequiredMixin, DeleteView):
    model = Tienda
    template_name = 'tiendaDelete.html'
    success_url = reverse_lazy('listar_tienda')


class InventarioCreateView(TenderoRequiredMixin, CreateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventarioForm.html'
    def get_success_url(self):
        tienda_id = self.kwargs.get('tienda_id')
        return reverse('listar_inventario', kwargs={'tienda_id': tienda_id})

    def form_valid(self, form):
        tienda_id = self.kwargs.get('tienda_id')
        form.instance.id_tienda = get_object_or_404(Tienda, id_tienda=tienda_id)
        form.instance.id_usuario_creacion = self.request.user
        return super().form_valid(form)


class InventarioListView(ListView):
    model = Inventario
    template_name = 'inventarioList.html'
    context_object_name = 'inventarios'

    def get_queryset(self):
        tienda_id = self.kwargs.get('tienda_id')
        return Inventario.objects.filter(id_tienda=tienda_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tienda_id = self.kwargs.get('tienda_id')
        context['tienda'] = get_object_or_404(Tienda, id_tienda=tienda_id)
        return context


class InventarioUpdateView(UserPassesTestMixin, UpdateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventarioUpdate.html'
    success_url = reverse_lazy('inventarioList')

    def test_func(self):
        inventario = self.get_object()
        try:
            tienda = Tienda.objects.get(id=self.get_object().id_tienda.id)
            return tienda.id_usuario == self.request.user
        except Tienda.DoesNotExist:
            return False

    def form_valid(self, form):
        form.instance.id_usuario_modificacion = self.request.user
        return super().form_valid(form)


class InventarioDeleteView(UserPassesTestMixin, DeleteView):
    model = Inventario
    template_name = 'inventarioDelete.html'
    success_url = reverse_lazy('listar_inventario')

    def test_func(self):
        inventario = self.get_object()
        try:
            tienda = Tienda.objects.get(id=inventario.id_tienda.id)
            return tienda.id_usuario == self.request.user
        except Tienda.DoesNotExist:
            return False
