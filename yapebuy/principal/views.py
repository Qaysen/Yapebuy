# encondig:utf-8
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from principal import mongomodels

# from pymongo import MongoClient

# client = MongoClient('127.0.0.1', 27017)
# db = client.e_commerce


def inicio(request):
    return render_to_response(
        'base.html',
        context_instance=RequestContext(request)
    )


# def crear_producto(request):
#     if request.method == 'POST':
#         nombre_producto = request.POST["nombre"]
#         with client.start_request():
#             db.productos.insert({"nombre": nombre_producto})

#         return HttpResponseRedirect('productos')

#     return render_to_response(
#         'crear_producto.html',
#         {},
#         context_instance=RequestContext(request)
#     )


# def lista_productos(request):
#     productos = None
#     with client.start_request():
#         productos = [producto for producto in db.productos.find()]

#     print productos
#     return render_to_response(
#         'lista_productos.html',
#         {"productos": productos},
#         context_instance=RequestContext(request)
#     )


# def editar_categorias(request):
#     if request.is_ajax():
#         accion = request.POST['accion']

#         if accion == 'ver_subcategorias':
#             cat_id = request.POST['cat_id']
#             subcategorias = Categoria.objects(
#                 padre=cat_id
#             ).tojson()

#             return HttpResponse(
#                 subcategorias,
#                 mimetype="application/json"
#             )

#         if accion == 'guardar_categoria':
#             if request.POST['padre_id']:
#                 parametros = {
#                     'nombre': request.POST['categoria'],
#                     'padre': request.POST['padre_id']
#                 }
#             else:
#                 parametros = {
#                     'nombre': request.POST['categoria']
#                 }

#             nueva_categoria = Categoria(**parametros)
#             nueva_categoria.save()

#     categorias = Categoria.objects(padre__exists=False)
#     return render_to_response(
#         'categorias.html',
#         {"categorias": categorias},
#         RequestContext(request)
#     )
