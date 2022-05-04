# NIFERTINA WEBAPP
---

## Grupo 16: Nicolas Passarini - Agostina Fregossi - Fernando Reyna.- Camada:27600

## Entrega Final



NIFERTINA WebApp Admin es una aplicación que está pensada para los equipos de ventas que recorren distintas zonas geográficas en búsqueda de nuevos clientes. Estos clientes son un target muy particular ya que no son amigables con la tecnologia y prefieren el contacto face to face.


La aplicación cuenta con tres módulos principales:

- Alta y Consulta de Pedidos
- Alta y Consulta de Productos
- Alta y Consulta de Clientes


### URL: www.nifertina.com


### Base de Datos:

SQL
Diagrama de Entidad Relación (DER): https://drive.google.com/drive/folders/1GWaDdk8k3SF8M_T0izPKAThDAmNjFrxz?usp=sharing


### Tecnologías:

- Python
- Django 
- CSS
- HTML

---

### Funcionalidades:

- ABM Usuarios/clientes
- Perfil Administrador y Cliente
- Permisos
- Listado de productos
- Importación de productos mediante un archivo .txt (*)
- Búsqueda de productos por código o descripción
- Alta de pedidos (estados: abierto, pendiente, cerrado)
- Notificaciones via email

---
(*) 

***Importacion / Actualización masiva de articulos y stock***

Se realiza mediante un archivo .txt se puede hacer un alta, o modificacion de articulos.

Si el codigo del articulo no existe, el articulo se da de alta, junto con la descripción y su correspondiente stock
Si el codigo existe, se actualiza la descripcion del articulo y el stock

##### Formato archivo:
codigoarticulo,descripcion,stock

##### Ejemplo:
p2001, Articulo1, 50.
p2002, Articulo2, 199.
p2003, Articulo3, 201.
p2004, Articulo4, 120.
p2005, Articulo5, 38.
p2006, Articulo6, 15.
p2007, Articulo7, 7.

---

