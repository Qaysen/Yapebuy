#from django.contrib.auth.models import User, Group
from tastypie.utils.timezone import now
from django.db import models
from django.template import defaultfilters
import datetime
from django.db.models import signals
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyUserManager(BaseUserManager):
	def create_user(self, username, email , password=None):
		if not email:
			raise ValueError('The given email must be set')
		

		user = self.model( username=username, 
						email = MyUserManager.normalize_email(email))

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,username, email ,password):
		user = self.create_user(username, password=password, email=email)
		user.is_admin = True
		user.save(using=self._db)
		return user


class MyUser(AbstractBaseUser):
	usuarios = (
		('Administrador','Administrador'),
		('Vendedor','Vendedor'),
		('Cliente','Cliente'),
	)
	username = models.CharField(max_length=200 , unique=True)
	email = models.EmailField(db_index=True)
	tipo_usuario=models.CharField(choices=usuarios,max_length=12)
	dni = models.CharField(max_length=8,null=True,blank=True)
	direccion =models.CharField(max_length=100,null=True,blank=True)
	distrito =models.CharField(max_length=20,null=True,blank=True)
	provincia=models.CharField(max_length=20,null=True,blank=True)
	departamento=models.CharField(max_length=20,null=True,blank=True)
	telefono=models.CharField(max_length=7,null=True,blank=True)
	slug = models.SlugField()


	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	
	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_full_name(self):
		return self.email
 
	def get_short_name(self):
		return self.email
 
	def __unicode__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin



"""
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
"""

class Producto(models.Model):		
	sku =models.CharField(max_length=8)
	slug = models.SlugField()
	def __unicode__(self):
		return unicode(self.sku)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.sku)
		super(Producto, self).save(*args, **kwargs)


class Carrito(models.Model):
	#cliente = models.ForeignKey(Cliente)
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

"""
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
"""