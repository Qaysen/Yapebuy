import mongoengine
import datetime


class Categoria(mongoengine.Document):
    nombre = mongoengine.StringField(max_length=50, unique=True)
    padre = mongoengine.ReferenceField('self')


class PrecioPasado(mongoengine.EmbeddedDocument):
    precio = mongoengine.DecimalField(min_value=0.00)
    fecha_inicio = mongoengine.DateTimeField()
    fecha_termino = mongoengine.DateTimeField()


class Producto(mongoengine.Document):
    sku = mongoengine.StringField(
        max_length=8, min_length=8, primary_key=True, unique=True)
    nombre = mongoengine.StringField(max_length=120)
    marca = mongoengine.StringField(max_length=50)
    precio = mongoengine.DecimalField(min_value=0.00)
    categoria = mongoengine.ReferenceField('Categoria')
    detalles = mongoengine.DictField()
    historial_precios = mongoengine.ListField(PrecioPasado())
