from django.conf.urls.defaults import *
from django.contrib import admin
from tastypie.api import Api
from django.conf import settings
from tastypie import api
from principal.api import resources

admin.autodiscover()

v1_api = Api(api_name='v1')
#v1_api.register(resources.UserResource())
#v1_api.register(resources.AdministradorResource())
#v1_api.register(resources.VendedorResource())
#v1_api.register(resources.ClienteResource())
v1_api.register(resources.ProductoResource())
#v1_api.register(resources.CarritoResource())
v1_api.register(resources.ProductoCarritoResource())
v1_api.register(resources.VentasResource())
v1_api.register(resources.CategoriasResource())
v1_api.register(resources.ProductosResource())


urlpatterns = patterns(
    '',
    # Prueba para nueva forma de cargas plantillas
    # plantillas y archivos estaticos
    url(r'^$', "principal.views.inicio"),

    url(r'^api/', include(v1_api.urls)),

    url(
        r'^admin/doc/',
        include('django.contrib.admindocs.urls')
    ),

    url(
        r'^admin/',
        include(admin.site.urls)
    ),

    url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, }
    ),
    (r'^api/', include(v1_api.urls)),

    # url(
    #     r'^productos/nuevo$',
    #     'principal.views.crear_producto'
    # ),

    # url(
    #     r'^productos$',
    #     'principal.views.lista_productos'
    # ),

    # url(
    #     r'^categorias/editar$',
    #     'principal.views.editar_categorias'
    # ),


)
