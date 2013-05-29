from tastypie import authorization as tastypie_authorization
from tastypie import fields as tastypie_fields
from tastypie.resources import ALL, ALL_WITH_RELATIONS

from tastypie_mongoengine import fields, paginator, resources

from principal import mongomodels


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
