from django.db import models
from django.contrib.auth.models import User, Group
from django.template import defaultfilters
import datetime

class Administrador(models.Model):
	usuario = models.OneToOneField(User)
	
	def __unicode__(self):
		return unicode(self.usuario)

class Cliente(models.Model):
	usuario = models.OneToOneField(User)
	direccion =models.CharField(max_length=100,null=True,blank=True)
	distrito =models.CharField(max_length=20,null=True,blank=True)
	provincia=models.CharField(max_length=20,null=True,blank=True)
	departamento=models.CharField(max_length=20,null=True,blank=True)
	telefono=models.CharField(max_length=7,null=True,blank=True)

	def __unicode__(self):
		return unicode(self.usuario)


class Categoria (models.Model):
	nombre =models.CharField(max_length=30,null=True,blank=True)
	
	def __unicode__(self):
		return unicode(self.nombre)

class Detalle (models.Model):
	capacidad =models.CharField(max_length=30,null=True,blank=True)
	marca =models.CharField(max_length=30,null=True,blank=True)
	modelo =models.CharField(max_length=30,null=True,blank=True)
	
	def __unicode__(self):
		return unicode(self.marca)


class Producto(models.Model):		
	nombre =models.CharField(max_length=30)
	precio =models.DecimalField(max_digits=3, decimal_places=2)
	categoria = models.OneToOneField(Categoria)
	detalle = models.OneToOneField(Detalle)

	def __unicode__(self):
		return unicode(self.nombre)


class Carrito(models.Model):
	cliente = models.OneToOneField(Cliente)
	cantidad =models.IntegerField()
	
	def __unicode__(self):
		return unicode(self.cliente)

class ProductoCarrito(models.Model):
	carrito = models.OneToOneField(Carrito)
	producto = models.OneToOneField(Producto)	
	
	def __unicode__(self):
		return '%s en %s' %(self.carrito, self.producto)

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

	carrito = models.OneToOneField(Carrito)
	monto =models.DecimalField(max_digits=3, decimal_places=2)
	fecha =models.DateField(auto_now=False)
	est_pedido =models.CharField(choices=pedido,max_length=12)	
	est_pago=models.CharField(choices=pago,max_length=12)

	def __unicode__(self):
		return '%s en %s' %(self.carrito, self.producto)