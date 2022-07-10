from django.db import models

# Create your models here.
class producto(models.Model):
  nombre = models.CharField(max_length=30)
  descripcion = models.CharField(max_length=500)
  precio = models.IntegerField()
  precioDcto = models.IntegerField(default = 0)
  disponible = models.BooleanField()
  fechaIncorporacion = models.DateField()
  idProveedor = models.IntegerField()
  rutaImg = models.CharField(max_length=500, default = 'ruta')
  tamano = models.IntegerField(default = 0)
   
class pedido(models.Model):
  codPedido = models.IntegerField()
  fechaPedido = models.DateField()
  fechaPago = models.DateField()
  tipoPedido = models.IntegerField()
  codFactura = models.IntegerField()
  totalPedido = models.IntegerField()
  estadoPedido = models.IntegerField()
  codCliente = models.IntegerField()

class detallePedido(models.Model):
  codPedido = models.IntegerField()
  codProducto = models.IntegerField()
  cantidad = models.IntegerField()
  url = models.CharField(max_length=500)
  descripcion = models.CharField(max_length=50)
  precioProducto = models.IntegerField()
  subtotalPedido = models.IntegerField()
  fechaEntrega = models.DateField()
  estadoEntrega = models.IntegerField()
  
class tipoPedido(models.Model):
  codigo = models.IntegerField()
  descripcion = models.CharField(max_length=20)

class estadoPedido(models.Model):
  codigo = models.IntegerField()
  descripcion = models.CharField(max_length=20)

class estadoEntrega(models.Model):
  codigo = models.IntegerField()
  descripcion = models.CharField(max_length=20)

class cliente(models.Model):
  rut = models.IntegerField()
  dvRut = models.CharField(max_length=1)
  nombreFantasia = models.CharField(max_length=30)
  razonSocial = models.CharField(max_length=100)
  giro = models.IntegerField()
  direccionCasaMatriz = models.CharField(max_length=100)
  direccionFacturacion = models.CharField(max_length=100)
  correoContacto = models.EmailField()
  telefonoContacto = models.IntegerField()

class giro(models.Model):
  codigo = models.IntegerField()
  descripcion = models.CharField(max_length=20)

class proveedor(models.Model):
  rut = models.IntegerField()
  dvRut = models.CharField(max_length=1)
  nombreFantasia = models.CharField(max_length=30)
  razonSocial = models.CharField(max_length=100)
  giro = models.IntegerField()
  direccionCasaMatriz = models.CharField(max_length=100)
  correoContacto = models.EmailField()
  telefonoContacto = models.IntegerField()

class usuario(models.Model):
  nombreUsuario = models.CharField(max_length=20)
  password = models.CharField(max_length=20)
  suscripcion = models.BooleanField()
  logueado = models.BooleanField(default = 0)
