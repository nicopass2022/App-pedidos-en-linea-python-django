
from django.urls import path

#para el logout
from django.contrib.auth.views import LogoutView

#from Entrega1.ProyectoFinal.ProyectoPrueba.settings import MEDIA_URL

from .views import agregaarticulos, agregaclientes, consultapedido, contacto, generapedido1, agregapedido, clientes, importar, importarMedia, inicio, editar_perfil, cierrapedido, generapedido, login_request, modificaPedido,  pedidos, recuperar_articulos, productos, buscar, register, uploadFile
# from .views import curso, cursoformulario, estudiantes, entregables, inicio, profesores

#para el utl pattern de imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('inicio/', inicio, name="Inicio"),
    # path('agrega-curso/<nombre>/<camada>', curso),
    path('clientes/', clientes, name="clientes"),
    path('recuperar_articulos/', recuperar_articulos, name="recuperar_articulos"),
    path('agregaarticulos/', agregaarticulos, name="agregaarticulos"),
    path('agregaclientes/', agregaclientes, name="agregaclientes"),
    path('agregapedido/', agregapedido, name="agregapedido"),
    # path('entregables/', entregables, name="Entregables"),
    path('pedidos/', pedidos, name="pedidos"),
    path('productos/', productos, name="productos"),
    path('busquedaarticulos/', buscar, name="busquedaarticulos"),
    #genera pedido sin form
    path('generapedido1/<codigo>', generapedido1, name="generapedido1"),
    #generapedido con form
    path('generapedido/', generapedido, name="generapedido"),
    path('cierrapedido/', cierrapedido, name="cierrapedido"),
    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('editarperfil/', editar_perfil, name="editarperfil"),
    path('logout/', LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    path('contacto/', contacto, name="contacto"),
    path('consultapedido/<id_pedido>', consultapedido, name="consultapedido"),
    path('importar/', importar, name="importar"),
    path('uploadFile/', uploadFile, name="uploadFile"),
    path('importarMedia/', importarMedia, name="importarMedia"),
    path('modificapedido/', modificaPedido, name="modificapedido"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 