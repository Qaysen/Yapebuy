from django.contrib.auth.models import User, Group
from tastypie.utils.timezone import now
from django.db import models
from django.template import defaultfilters
import datetime
from django.db.models import signals

class Administrador(models.Model):
	usuario = models.ForeignKey(User)
	slug = models.SlugField()
	def __unicode__(self):
		return unicode(self.usuario)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.usuario)
		super(Administrador, self).save(*args, **kwargs)


class Vendedor(models.Model):
	usuario = models.ForeignKey(User)
	dni = models.CharField(max_length=8,null=True,blank=True)
	direccion =models.CharField(max_length=200,null=True,blank=True)
	telefono = models.CharField(max_length=7,null=True,blank=True)
	slug = models.SlugField()

	def __unicode__(self):
		return unicode(self.usuario)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.usuario)
		super(Vendedor, self).save(*args, **kwargs)

class Cliente(models.Model):
	usuario = models.ForeignKey(User)
	direccion =models.CharField(max_length=100,null=True,blank=True)
	distrito =models.CharField(max_length=20,null=True,blank=True)
	provincia=models.CharField(max_length=20,null=True,blank=True)
	departamento=models.CharField(max_length=20,null=True,blank=True)
	telefono=models.CharField(max_length=7,null=True,blank=True)
	slug = models.SlugField()

	def __unicode__(self):
		return unicode(self.usuario)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.usuario)
		super(Cliente, self).save(*args, **kwargs)


class Producto(models.Model):		
	sku =models.CharField(max_length=8)
	slug = models.SlugField()
	def __unicode__(self):
		return unicode(self.sku)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.sku)
		super(Producto, self).save(*args, **kwargs)


class Carrito(models.Model):
	cliente = models.ForeignKey(Cliente)
	slug = models.SlugField()

	def __unicode__(self):
		return unicode(self.cliente)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.cliente)
		super(Carrito, self).save(*args, **kwargs)



class ProductoCarrito(models.Model):
	carrito = models.ForeignKey(Carrito)
	producto = models.ForeignKey(Producto)	
	cantidad =models.IntegerField()
	slug = models.SlugField()

	def __unicode__(self):
		return '%s en %s' %(self.carrito, self.producto)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.carrito)
		super(ProductoCarrito, self).save(*args, **kwargs)



class Ventas(models.Model):

	pedido = (
		('Realizandose','Realizandose'),
		('Enviado','Enviado'),
		('Entregado/Finalizado','Entregado/Finalizado')
		
	)

	pago = (
		('espera','espera'),
		('pagado','pagado')	
		
	)

	carrito = models.ForeignKey(Carrito)
	monto =models.DecimalField(max_digits=3, decimal_places=2)
	fecha =models.DateField(auto_now=False)
	est_pedido =models.CharField(choices=pedido,max_length=12)	
	est_pago=models.CharField(choices=pago,max_length=12)
	slug = models.SlugField()

	def __unicode__(self):
		return '%s en %s' %(self.carrito, self.carrito)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.carrito)
		super(Ventas, self).save(*args, **kwargs)


def guardando_usuario(sender, **kwargs):
    modelos_validos = ["Vendedor", "Cliente", "Administrador"]
    modelo = str(sender.__name__)

    if modelo in modelos_validos:
        instancia = kwargs['instance']
        grupo, creado = Group.objects.get_or_create(name=modelo)
        instancia.usuario.groups.add(grupo)

signals.pre_save.connect(guardando_usuario, sender=Vendedor)
signals.pre_save.connect(guardando_usuario, sender=Cliente)
signals.pre_save.connect(guardando_usuario, sender=Administrador)