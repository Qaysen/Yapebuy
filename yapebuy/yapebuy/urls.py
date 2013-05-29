from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from tastypie import api
from principal.api import resources

admin.autodiscover()

v1_api = api.Api(api_name='v1')
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
)
