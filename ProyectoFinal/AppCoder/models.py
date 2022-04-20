from dataclasses import Field

from django.db import models

class Articulos(models.Model):
   Codigo=models.CharField("codigo", max_length=50)
   descripcion=models.CharField("descripcion", max_length=50)
   stock = models.IntegerField("stock")


class Clientes(models.Model):
   nombre=models.CharField("nombre", max_length=50)
   apellido=models.CharField("apellido", max_length=50)
   razonsocial = models.CharField("razonsocial", max_length=50)
   cuit=models.IntegerField("cuit")
   

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
   pedido= models.ForeignKey(Pedido, on_delete=models.CASCADE)
   articulo= models.ForeignKey(Articulos, on_delete=models.CASCADE)
   cantidad=models.IntegerField("cantidad")

class Pedido_temp(models.Model):
   idcliente=models.IntegerField("idcliente")
   idarticulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
   cantidad=models.IntegerField("cantidad", default="0")
   cerrado=models.BooleanField(default=False)
   #idarticulo = models.ForeignKey(Articulos)
   idarticulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
   fecha=models.DateField("fecha")
