from dataclasses import Field

from django.db import models
#para vincular modelo auth_user
from django.conf import settings


class Articulos(models.Model):
   Codigo=models.CharField("codigo", max_length=50)
   descripcion=models.CharField("descripcion", max_length=50)
   stock = models.IntegerField("stock")
   habilitado=models.BooleanField(default=True)
   def __str__(self) -> str:
      return f"{self.Codigo} {self.descripcion} {self.stock} {self.habilitado}"


class Clientes(models.Model):
   
   #apellido=models.CharField("apellido", max_length=50)
   razonsocial = models.CharField("razonsocial", max_length=50)
   cuit=models.IntegerField("cuit")
   domicilio=models.CharField("domicilio", default="-", max_length=50)
   contacto=models.CharField("contacto", default="-", max_length=50)
   #ceo relacion con auth_user
   usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
   def __str__(self) -> str:
      return f"{self.razonsocial} {self.cuit} {self.domicilio} {self.contacto}"

class Pedido(models.Model):
   idcliente=models.IntegerField("idcliente")
   #idarticulo = models.IntegerField("idarticulo")
   #cantidad=models.IntegerField("cantidad", default="0")
   entregado=models.BooleanField(default=False)
   #idarticulo = models.ForeignKey(Articulos)
   #idarticulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
   fecha=models.CharField("fecha", max_length=50)
   cerrado=models.BooleanField(default=True)
   #detalle=models.ManyToManyField(Articulos)
class Detalle(models.Model):
   pedido= models.ForeignKey(Pedido, on_delete=models.PROTECT)
   articulo= models.ForeignKey(Articulos, on_delete=models.PROTECT)
   cantidad=models.IntegerField("cantidad")

class Pedido_temp(models.Model):
   idcliente=models.IntegerField("idcliente")
   idarticulo = models.ForeignKey(Articulos, on_delete=models.PROTECT)
   cantidad=models.IntegerField("cantidad", default="0")
   cerrado=models.BooleanField(default=False)
   #idarticulo = models.ForeignKey(Articulos)
   idarticulo = models.ForeignKey(Articulos, on_delete=models.PROTECT)
   fecha=models.DateField("fecha")
