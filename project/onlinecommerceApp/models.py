# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser





class Usuario(AbstractUser):

    apellido = models.CharField(max_length=200)
    estado = models.IntegerField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    fecha_creacion = models.DateField(blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    cedula = models.IntegerField(blank=True, null=True)
    tipo_cedula = models.CharField(max_length=30, blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.CharField(max_length=250)

    class Meta:
        managed = True
        db_table = 'Usuario'

class CategoriaProducto(models.Model):
    id_categoria =  models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = 'categoria_producto'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_producto =  models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    id_categoria_producto = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    id_usuario_modificacion = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='producto_modificado')
    fecha_modificado = models.DateTimeField(default=timezone.now)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    id_usuario_creacion = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='producto_creado')
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'producto'



class Carrito(models.Model):
    id_carrito =  models.AutoField(primary_key=True)
    fecha_creacion = models.DateField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    estado_carrito = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'carrito'



class CategoriaTienda(models.Model):
    id_categoria =  models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'categoria_tienda'



class Direccion(models.Model):
    id_direccion =  models.AutoField(primary_key=True)
    barrio = models.CharField(max_length=60)
    direccion = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'direccion'


class Tienda(models.Model):
    id_tienda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    telefono = models.IntegerField()
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    correo = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    id_categoria = models.ForeignKey(CategoriaTienda, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    fecha_modificacion = models.DateField(blank=True, null=True)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=250)

    class Meta:
        managed = True
        db_table = 'tienda'


class Pedido(models.Model):
    id_pedido =  models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    id_tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    estado = models.CharField(max_length=250, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    tipo_entrega = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pedido'


class MetodoPago(models.Model):
    id_metodo_pago =  models.AutoField(primary_key=True)
    nombre = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'metodo_pago'


class Pagos(models.Model):
    id_pagos = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    fecha_pago = models.DateField(blank=True, null=True)
    monto_pago = models.IntegerField(blank=True, null=True)
    moneda = models.CharField(max_length=50, blank=True, null=True)
    estado_pago = models.IntegerField(blank=True, null=True)
    detalle_pago = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pagos'


class DetalleDomicilio(models.Model):
    id =  models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    fecha_hora_pedido_listo = models.DateTimeField()
    fecha_hora_pedido_recogido = models.DateTimeField()
    id_usuario_domiciliario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_hora_pedido_entrega = models.DateTimeField()
    estado = models.CharField(max_length=50)
    novedades = models.CharField(max_length=250, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'detalle_domicilio'


class DetalleFisico(models.Model):
    id_fisico = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_recoger_inicio = models.DateField(blank=True, null=True)
    fecha_recoger_fin = models.DateField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'detalle_fisico'





class InteraccionSolicitud(models.Model):
    id_interaccion =  models.AutoField(primary_key=True)
    id_usuario_creacion = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    interaccion = models.CharField(max_length=300, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion = models.DateField()

    class Meta:
        managed = True
        db_table = 'interaccion_solicitud'


class Inventario(models.Model):
    id_inventario =  models.AutoField(primary_key=True)
    id_tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=45)
    fecha_creacion = models.DateField(blank=True, null=True)
    id_usuario_creacion = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inventario_creado')
    fecha_modificado = models.DateField(blank=True, null=True)
    id_usuario_modificacion = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inventario_modificado')

    class Meta:
        managed = True
        db_table = 'inventario'


class ProductoHasPedido(models.Model):
    id =  models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    precio_unitario = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    subtotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'producto_has_pedido'


class Ventas(models.Model):
    id_venta =  models.AutoField(primary_key=True)
    fecha_creacion = models.DateField()
    id_usuario_creacion = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    total = models.IntegerField(blank=True, null=True)
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ventas'


class ProductoHasVenta(models.Model):
    id =  models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    precio_unitario = models.FloatField(blank=True, null=True)
    catidad = models.IntegerField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'producto_has_venta'



class TipoSolicitud(models.Model):
    id_tipo_solicitud = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'tipo_solicitud'

class Solicitud(models.Model):
    id_solicitud =  models.AutoField(primary_key=True)
    fecha_solicitud = models.DateField()
    estado = models.CharField(max_length=50)
    id_tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    id_usuario_creacion = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitud_creada')
    id_tipo_solicitud = models.ForeignKey(TipoSolicitud, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_respuesta = models.DateField(blank=True, null=True)
    id_usuario_respuesta = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitud_respondida')
    id_usuario_modificacion = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitud_modificada')
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    asunto = models.CharField(max_length=250, blank=True, null=True)
    respuesta_cierre = models.CharField(max_length=250, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'solicitud'





