from django.conf.urls.defaults import *
from django.contrib import admin
from tastypie.api import Api
from django.conf import settings
from principal.api.resources import *

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(AdministradorResource())
v1_api.register(ClienteResource())
v1_api.register(ProductoResource())
v1_api.register(CarritoResource())
v1_api.register(ProductoCarritoResource())
v1_api.register(VentasResource())


urlpatterns = patterns(
    '',
    # Prueba para nueva forma de cargas plantillas
    # plantillas y archivos estaticos
    url(r'^$', "principal.views.inicio"),

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

    url(
        r'^productos/nuevo$',
        'principal.views.crear_producto'
    ),

    url(
        r'^productos$',
        'principal.views.lista_productos'
    ),

    url(
        r'^categorias/editar$',
        'principal.views.editar_categorias'
    ),
    (r'^api/', include(v1_api.urls)),
)

