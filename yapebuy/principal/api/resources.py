from django.contrib.auth.models import User
from principal import mongomodels
from principal.models import *
from tastypie import authorization as tastypie_authorization
from tastypie import fields as tastypie_fields
from tastypie.authorization import Authorization
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie_mongoengine import fields, paginator, resources

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL_WITH_RELATIONS,
        }

class AdministradorResource(ModelResource):
    user= tastypie_fields.ForeignKey(UserResource,'usuario')
    class Meta:
        queryset = Administrador.objects.all()
        resource_name = 'administradores'
        authorization = Authorization()
        filtering = {
            'user': ALL_WITH_RELATIONS,
        }

class ClienteResource(ModelResource):
    user=tastypie_fields.ForeignKey(UserResource, 'usuario')
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
    cliente=tastypie_fields.ForeignKey(ClienteResource,'cliente')
    class Meta:
        queryset = Carrito.objects.all()
        resource_name = 'carrito'
        authorization = Authorization()

class ProductoCarritoResource(ModelResource):
    carrito=tastypie_fields.ForeignKey(CarritoResource,'carrito')
    producto=tastypie_fields.ForeignKey(ProductoResource,'producto')
    class Meta:
        #falta ver una relacion entre carrito y produto para realizar el llamado
        queryset = ProductoCarrito.objects.all()
        resource_name = 'productocarrito'
        authorization = Authorization()

class VentasResource(ModelResource):
    carrito=tastypie_fields.ForeignKey(CarritoResource,'carrito')
    class Meta:
        queryset = Ventas.objects.all()
        resource_name = 'ventas'
        authorization = Authorization()




class CategoriasResource(resources.MongoEngineResource):

    class Meta:
        queryset = mongomodels.Categoria.objects.all()
        allowed_methods = ('get', 'post', 'put', 'patch', 'delete')
        filtering = {
            'padre': ('exists',),
        }


class ProductosResource(resources.MongoEngineResource):

    class Meta:
        queryset = mongomodels.Producto.objects.all()
        allowed_methods = ('get', 'post', 'put', 'patch', 'delete')
        filtering = {
            'precio': ALL_WITH_RELATIONS
        }

