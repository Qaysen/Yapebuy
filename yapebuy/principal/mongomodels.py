from mongoengine import *
import datetime

connect('yapebuy')


class Categoria(Document):
    nombre = StringField(max_length=50, unique=True)
    padre = ReferenceField('self')


class PrecioPasado(EmbeddedDocument):
    precio = DecimalField(min_value=0.00)
    fecha_inicio = DateTimeField()
    fecha_termino = DateTimeField()


class Producto(Document):
    sku = StringField(
        max_length=8, min_length=8, primary_key=True, unique=True)
    nombre = StringField(max_length=120)
    marca = StringField(max_length=50)
    precio = DecimalField(min_value=0.00)
    categoria = ReferenceField('Categoria')
    detalles = DictField()
    historial_precios = ListField(PrecioPasado())
