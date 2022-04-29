from dataclasses import Field
from email.policy import default

from django.db import models
#para vincular modelo auth_user
from django.conf import settings
#para vincular modelo avatar a modelo user
from django.contrib.auth.models import User
#para el delete de archivos
import os


class Articulos(models.Model):
   Codigo=models.CharField("codigo", max_length=50)
   descripcion=models.CharField("descripcion", max_length=50)
   stock = models.IntegerField("stock")
   habilitado=models.BooleanField(default=True)
   image = models.ImageField(upload_to='images', null=True, blank=True, default="images/engranaje.jpg")
   def __str__(self) -> str:
      return f"{self.Codigo} {self.descripcion} {self.stock} {self.habilitado} {self.image}"


class Clientes(models.Model):
   
   #apellido=models.CharField("apellido", max_length=50)
   razonsocial = models.CharField("razonsocial", max_length=50)
   cuit=models.IntegerField("cuit")
   domicilio=models.CharField("domicilio", default="-", max_length=50)
   contacto=models.CharField("contacto", default="-", max_length=50)
   #ceo relacion con auth_user
   usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, unique=True)
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

class Avatar(models.Model):
   user=models.ForeignKey(User, on_delete=models.CASCADE)
   imagen=models.ImageField(upload_to= "avatares", null=True, blank=True, default="avatares/images.png")
   def __str__(self) -> str:
      return f"{self.user} {self.imagen}"


class Document(models.Model):
   title = models.CharField(max_length = 200)
   uploadedFile = models.FileField(upload_to = "Uploaded")
   dateTimeOfUpload = models.DateTimeField(auto_now = True)
   def delete(self, *args, **kwargs):
      if self.uploadedFile:
         self.uploadedFile.delete()
         super().delete(*args, **kwargs)
# class AlbumImage(models.Model):
#    album = models.ForeignKey(Articulos, related_name='images', on_delete=models.CASCADE)
#    image = models.ImageField(upload_to='images', null=True, blank=True, default="images/engranaje.jpg")

#     #def __unicode__(self,):
#    def __str__(self) -> str:
#       return str(self.image)