from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from principal.models import *

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL_WITH_RELATIONS,
        }

class AdministradorResource(ModelResource):
    user= fields.ForeignKey(UserResource,'usuario')
    class Meta:
        queryset = Administrador.objects.all()
        resource_name = 'administradores'
        authorization = Authorization()
        filtering = {
            'user': ALL_WITH_RELATIONS,
        }

class ClienteResource(ModelResource):
    user=fields.ForeignKey(UserResource, 'usuario')
    class Meta:
        queryset = Cliente.objects.all()
        resource_name = 'clientes'
        authorization = Authorization()

class ProductoResource(ModelResource):
    class Meta:
        queryset = Producto.objects.all()
        resource_name = 'productos'
        authorization = Authorization()

class CarritoResource(ModelResource):
    cliente=fields.ForeignKey(ClienteResource,'cliente')
    class Meta:
        queryset = Carrito.objects.all()
        resource_name = 'carrito'
        authorization = Authorization()

class ProductoCarritoResource(ModelResource):
    carrito=fields.ForeignKey(CarritoResource,'carrito')
    producto=fields.ForeignKey(ProductoResource,'producto')
    class Meta:
        #falta ver una relacion entre carrito y produto para realizar el llamado
        queryset = ProductoCarrito.objects.all()
        resource_name = 'productocarrito'
        authorization = Authorization()

class VentasResource(ModelResource):
    carrito=fields.ForeignKey(CarritoResource,'carrito')
    class Meta:
        queryset = Ventas.objects.all()
        resource_name = 'ventas'
        authorization = Authorization()