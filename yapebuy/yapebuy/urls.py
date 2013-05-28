from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

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
)
