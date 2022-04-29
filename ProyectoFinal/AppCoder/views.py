from datetime import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from django.template import loader
from django.db.models import Q

from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from pkg_resources import require

from AppCoder.forms import UserEdithForm
#Import OS para acceder a carpetas 
import os


#Para el login

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

#from AppCoder.forms import cursoformulario

from .models import  Articulos, Avatar, Clientes, Detalle, Document, Pedido, Pedido_temp

#requerir loguearse para acceder a las view o las clases 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#----para eliminar archivos antiguos
from django.conf import settings
from django.conf.global_settings import MEDIA_ROOT
#PARA LAS IMAGENES EN LOS ARTICULOS

#from django.shortcuts import render_to_response, RequestContext

#from .forms import UploadImageForm

@login_required
def clientes(request):
            clientes=Clientes.objects.all()
 
            #contexto= Context({"p":profe})
            return render(request,"AppCoder/clientes.html",{"clientes":clientes})



    #return render(request,"AppCoder/clientes.html")
    

@login_required
def agregaclientes(request):
    
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        razonsocial=request.POST["razonsocial"]
        cuit=request.POST["cuit"]
        cliente=Clientes(nombre=nombre, apellido=apellido, razonsocial=razonsocial, cuit=cuit)
        cliente.save()
        #return HttpResponse(f"se genero curso {articulo.Codigo} y la camada {articulo.descripcion}")
        
        clientes=Clientes.objects.all()
 
        #contexto= Context({"productos":articulos} )

        return render(request,"AppCoder/clientes.html",{"clientes":clientes, "razonsocial": razonsocial, "cuit": cuit})



def inicio(request):
    #return render(request,"appcoder/inicio.html")
    
    return render(request,"AppCoder/padre.html")
 

# #agregar articulos
def agregaarticulos(request):
    
        codigo=request.POST["codigo"]
        descripcion=request.POST["descripcion"]
        stock=request.POST["stock"]
        articulo=Articulos(Codigo=codigo, descripcion=descripcion,stock=stock)
        articulo.save()
        #return HttpResponse(f"se genero curso {articulo.Codigo} y la camada {articulo.descripcion}")
        
        articulos=Articulos.objects.all()
 
        #contexto= Context({"productos":articulos} )

        return render(request,"AppCoder/productos.html",{"productos":articulos, "descripcion": descripcion, "codigo": codigo})
        
        #return render(request, "AppCoder/productos.html", {"codigo": codigo, "descripcion":descripcion})

    # articulo=Articulos(Codigo=codigo,descripcion=descripcion,stock=stock)
    # articulo.save()
    # return HttpResponse(f"se agrego el articulo {articulo.codigo} , {articulo.descipcion}")

def recuperar_articulos(request):
    articulos=Articulos.objects.all()
 
    #contexto= Context({"p":profe})
    return render(request,"AppCoder/recuperar_articulos.html",{"familia":articulos})

@login_required
def pedidos( request):
    #carga listado de articulos
    # articulos=Articulos.objects.all()
    # pedidos=Pedido.objects.all()
 
    #contexto= Context({"p":profe})
    #return render(request,"AppCoder/recuperar_articulos.html",{"familia":articulos})
   
   
    #--------------renderiza formulario -------
    # if request.method=="POST":
    #     #busco el formulario en forms.py
    #     miformulario=cursoformulario(request.POST)
    #     if miformulario.is_valid():
    #         informacion=miformulario.cleaned_data
    #         cuit=informacion["cuit"]
    #         articulo=informacion["articulo"]
    #         cantidad=informacion["cantidad"]
    #-----------fin renderiza formulario------------
                

    #-----recupero el id cliente
    usuario = request.user.id
    try:  
        #Clientes.objects.get(usuario_id=usuario)
        

        cliente=Clientes.objects.get(usuario_id=usuario)
        idc=cliente.id

    
    
        #---- Filtro estado del pedido, abierto o cerrado y filtro por idcliente
        
        pedidos_temp=Pedido_temp.objects.filter(cerrado=0, idcliente=idc)
     
        #pedidos_temp=Pedido_temp.objects.filter(cerrado=0)
        #pedidos=Pedido.objects.all()
        pedidos=Pedido.objects.filter(idcliente=idc)
        detalle=Detalle.objects.all()
        id_art=Pedido_temp.objects.values("idarticulo_id")
        articulos=Articulos.objects.all()
        

       
        contexto={"pedidos_temp":pedidos_temp, "articulos":articulos, "detalle":detalle, "pedidos":pedidos}
        return render(request, "AppCoder/pedidos.html",contexto)
    except:
        if request.user.id ==1:
            pedidos_temp=Pedido_temp.objects.filter(cerrado=0)
            pedidos=Pedido.objects.all()
            detalle=Detalle.objects.all()
            articulos=Articulos.objects.all()
            #descripcion=articulos.values("descripcion")
            cliente=Clientes.objects.all()
            contexto={"pedidos_temp":pedidos_temp, "articulos":articulos, "detalle":detalle, "pedidos":pedidos,  "cliente":cliente}
            return render(request, "AppCoder/pedidos.html",contexto)
        else:
            return HttpResponse("Este suario no puede ver esta seccion o no tiene una empresa asignada") 

@login_required
def agregapedido(request):

        cuit=request.POST["cuit"]
        articulo=request.POST["articulo"]
        cantidad=request.POST["cantidad"]
        descripcion=Pedido(idcliente=cuit, idarticulo=articulo,cantidad=cantidad)
        descripcion.save()

        pedidos=Pedido.objects.all()
        productos=Articulos.objects.all()
        return render(request, "AppCoder/pedidos.html",{"pedidos":pedidos, "productos":productos, "descripcion":descripcion, "articulo":articulo, })
        #return HttpResponse(f"se genero pedido")
        #return render(request, "AppCoder/cursos.html", {"codigo": codigo, "descripcion":descripcion})

@login_required
def productos(request):

            #articulos=Articulos.objects.all()
            articulos=Articulos.objects.filter(habilitado=True)
 
            #contexto= Context({"p":profe})

            #---cargo imagenes--
            #imagenes=AlbumImage.objects.all()

            return render(request,"AppCoder/productos.html",{"productos":articulos})
    #return render(request,"appcoder/productos.html")
    #return HttpResponse("vista de profesores")

def buscar(request):

      if  request.GET["articulo"]:
           

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
                articulo = request.GET['articulo'] 
                #articulos = Articulos.objects.filter(descripcion__contains=articulo)
                articulos = Articulos.objects.filter(Q(descripcion__contains=articulo) | Q(Codigo__contains=articulo))
            # return HttpResponse("articulo")
            # return render(request, "AppCoder/inicio.html", {"cursos":articulos, "camada":articulo})
                return render(request,"AppCoder/productos.html",{"productos":articulos})

      else: 
	        # respuesta = "No enviaste datos"
            return render(request, "AppCoder/productos.html")

      #No olvidar from django.http import HttpResponse

def savePedido(usuario, codigo, cantidad):    
        try:
            cliente=Clientes.objects.get(usuario_id=usuario)
            
        except:
            return {"status":"error", "description":"Este usuario no puede generar pedidos o no tiene una empresa asignada"} 

        codigo_art=Articulos.objects.filter(Codigo=codigo)
        id_cod=codigo_art.values_list('pk', flat=True)
        artdescripcion=codigo_art.values_list("descripcion")
        
        cliente=Clientes.objects.filter(usuario_id=usuario)
        clienteid=cliente.values("id")
        fecha=datetime.now()
        pedido=Pedido_temp(idcliente=clienteid, idarticulo_id=id_cod,cantidad=cantidad, fecha=fecha)
        pedido.save()
        return {"status":"ok", "description":artdescripcion} 


@login_required
def generapedido(request):
        codigos = request.POST.getlist("codigo[]")
        cantidades=request.POST.getlist("cantidad[]")
        userId = request.user.id
        output = []
        i = 0
        while i < len(codigos):
            if len(cantidades[i]) > 0:
                rta = savePedido(userId, codigos[i], cantidades[i])
                if rta['status'] == "ok":
                    output.append(rta['description'])
            i = i + 1

        if len(output) == 0:
            output.append("No se generaron pedidos")

        return render(request, "AppCoder/productoconfirmado.html", {"artdescripcion":output, "productos":output})
        
        """
        codigo=(request.POST["codigo"])[0]
        cantidad=request.POST["cantidad"][0]
        print(codigo)
        print (cantidad)
       
        # descripcion=Pedido(idcliente=cuit, idarticulo=articulo,cantidad=cantidad)
        # descripcion.save()


        codigo_art=Articulos.objects.filter(Codigo=codigo)
        id_cod=codigo_art.values_list('pk', flat=True)
        artdescripcion=codigo_art.values_list("descripcion")
        usuario = request.user.id
        
        #idc=cliente.id
        try:
            cliente=Clientes.objects.get(usuario_id=usuario)
            
        except:
            return HttpResponse("Este usuario no puede generar pedidos o no tiene una empresa asignada") 
        cliente=Clientes.objects.filter(usuario_id=usuario)
        clienteid=cliente.values("id")
        #clienteid=cliente.values_list("id")
        
        #idarticulo = models.IntegerField("idarticulo")
        #cantidad="1"
        fecha=datetime.now()
        
        # codigo=request.POST["codigo"]
        # cuit=request.POST["cuit"]
        # articulo=request.POST["articulo"]
        # cantidad=request.POST["cantidad"]
        pedido=Pedido_temp(idcliente=clienteid, idarticulo_id=id_cod,cantidad=cantidad, fecha=fecha)
        pedido.save()

        # pedidos=Pedido.objects.all()
        # productos=Articulos.objects.all()
        #return render(request,return HttpResponse(f"se agrego el articulo {articulo.codigo} , {articulo.descipcion}")return render(request,)
        
        
        return render(request, "AppCoder/productoconfirmado.html", {"artdescripcion":artdescripcion, "cantidad":cantidad})
        
        #return render(request, "AppCoder/articulos.html")
        """
        
        #return HttpResponse(f"se agrego el articulo {id_cod}, {cuit}, {descripcion} ")
        #return render_to_response('template_name', message='Save complete')
        #return messages.add_message(request, messages.INFO, 'Hello world.')
def cierrapedido(request):
        idcliente=Pedido_temp.objects.filter(cerrado=False)
        
        # codigo_art=Articulos.objects.filter(Codigo=codigo)
        # id_cod=codigo_art.values_list('pk', flat=True)
        # artdescripcion=codigo_art.values_list("descripcion")
        usuario = request.user.id
        correo= request.user.email

        try:  
        #Clientes.objects.get(usuario_id=usuario)
        

            cliente=Clientes.objects.get(usuario_id=usuario)
            idc=cliente.id
        except:
            return HttpResponse("Este usuario no puede ver esta seccion o no tiene una empresa asignada") 


        #cuit="2"
        fecha= datetime.now()
        pedido=Pedido(idcliente=idc, fecha=fecha)
        pedido.save()
        obj = pedido.pk


        #guardo el detalle
        detalle_tmp=Pedido_temp.objects.filter(cerrado=False, idcliente=idc)


        #---Loop , itero sobre queryset para guardar el detalle
        for n in detalle_tmp:
                     
            id_art= n.idarticulo_id
            cantidad= n.cantidad
            detalle=Detalle(articulo_id=id_art, pedido_id=obj, cantidad=cantidad)
            detalle.save()

        #cambio el estado del pedido a cerrado
        cerrado=1
        Pedido_temp.objects.filter(idcliente=idc).update(cerrado=cerrado)
        
        
        #----elimino de la tabla temp los cerrados del cliente----------
        #detalle_tmp=Pedido_temp.objects.filter(cerrado=True, idcliente=idc)
        Pedido_temp.objects.filter(cerrado=True, idcliente=idc).delete()

        #---Loop , itero sobre queryset para eliminar registros del temp
        # for n in detalle_tmp:
                     
        #     id_art= n.idarticulo_id
        #     cantidad= n.cantidad
        #     detalle=Detalle(articulo_id=id_art, pedido_id=obj, cantidad=cantidad)
        #     detalle.save()

        #******************envia correos texto plano
        destinatarios=["testpedidos2022@gmail.com"]
        destinatarios.append(correo)
        
        numpedido=str(obj)
        mensaje=("Se ha generado el pedido nro: "+numpedido)
        #destinatarios=[]
        send_mail(
            'Nuevo pedido ingresado',
            mensaje,
            settings.EMAIL_HOST_USER,
            destinatarios,
             fail_silently=False
            )
        #**********************************
        


        return render(request, "AppCoder/pedidoconfirmado.html", {"obj":obj})
                #return HttpResponse(f"se genero el pedido Nro:  {obj} ")

#@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario= UserEdithForm(request.POST)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            usuario.email=informacion["email"]
            usuario.password1=informacion["password1"]
            usuario.password2=informacion["password2"]
            usuario.save()

            return render(request, "AppCoder/padre.html")
    else:
        miFormulario= UserEdithForm(initial={"email":usuario.email})

    return render(request, "AppCoder/editarperfil.html", {"miFormulario":miFormulario})

def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                        #cargo avatar
                        avatar=Avatar.objects.get(user=request.user.id)
                        return render(request,"AppCoder/padre.html",  {"mensaje":f"Bienvenido {usuario}", "avatar":avatar} )
                  else:
                        
                        return render(request,"AppCoder/login.html", {"mensaje":"Error, formulario erroneo",'form':form } )
                        #return render(request,"AppCoder/padre.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        return render(request,"AppCoder/login.html", {"mensaje":"Error, formulario erroneo",'form':form } )
                        #return render(request,"AppCoder/padre.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppCoder/login.html", {'form':form} )
      #return render(request,"AppCoder/padre.html", {'form':form} )

def register(request):

      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            #form = UserRegisterForm(request.POST)
            if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                #--recupero id usuario para agregarle un avatar por defecto
                #usuario=form.pk
                usuario=User.objects.get(username=username)
                id=usuario.pk
                print("-----------------------------------")
                print (id)
                
                avatar=Avatar(user_id=id)
                avatar.save()
                  
                mensaje=(f"Nuevo registro de usuario {username}" )
                destinatarios=["testpedidos2022@gmail.com"]
                send_mail(
                    'Nuevo resgistro de usuario',
                    mensaje,
                    settings.EMAIL_HOST_USER,
                    destinatarios,
                    fail_silently=False
                )
        #**********************************
                  
                  
                return render(request,"AppCoder/padre.html" ,  {"mensaje":"Usuario Creado :). aguarde a que el administrador le confirme la finalización del alta",})


      else:
            form = UserCreationForm()       
            #form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})


#-----------------------generapedido1 sin formulario-----
@login_required
def generapedido1(request, codigo,cantidad):


        codigo_art=Articulos.objects.filter(Codigo=codigo)
        id_cod=codigo_art.values_list('pk', flat=True)
        artdescripcion=codigo_art.values_list("descripcion")
        usuario = request.user.id
        
        #idc=cliente.id
        try:
            cliente=Clientes.objects.get(usuario_id=usuario)
            
        except:
            return HttpResponse("Este usuario no puede generar pedidos o no tiene una empresa asignada") 
        cliente=Clientes.objects.filter(usuario_id=usuario)
        clienteid=cliente.values("id")
        #clienteid=cliente.values_list("id")
        
        #idarticulo = models.IntegerField("idarticulo")
        cantidad="1"
        fecha=datetime.now()
        
        # codigo=request.POST["codigo"]
        # cuit=request.POST["cuit"]
        # articulo=request.POST["articulo"]
        # cantidad=request.POST["cantidad"]
        pedido=Pedido_temp(idcliente=clienteid, idarticulo_id=id_cod,cantidad=cantidad, fecha=fecha)
        pedido.save()

        # pedidos=Pedido.objects.all()
        # productos=Articulos.objects.all()
        #return render(request,return HttpResponse(f"se agrego el articulo {articulo.codigo} , {articulo.descipcion}")return render(request,)
        
        
        return render(request, "AppCoder/productoconfirmado.html", {"artdescripcion":artdescripcion, "cantidad":cantidad})
        
        #return render(request, "AppCoder/articulos.html")
        
        
        #return HttpResponse(f"se agrego el articulo {id_cod}, {cuit}, {descripcion} ")
        #return render_to_response('template_name', message='Save complete')
        #return messages.add_message(request, messages.INFO, 'Hello world.')

@login_required
def generapedidoAll(request, codigo,cantidad):


        
        codigo_art=Articulos.objects.filter(Codigo=codigo)
        id_cod=codigo_art.values_list('pk', flat=True)
        artdescripcion=codigo_art.values_list("descripcion")
        usuario = request.user.id
        
        #idc=cliente.id
        try:
            cliente=Clientes.objects.get(usuario_id=usuario)
            
        except:
            return HttpResponse("Este usuario no puede generar pedidos o no tiene una empresa asignada") 
        cliente=Clientes.objects.filter(usuario_id=usuario)
        clienteid=cliente.values("id")
        #clienteid=cliente.values_list("id")
        
        #idarticulo = models.IntegerField("idarticulo")
        cantidad="1"
        fecha=datetime.now()
        


        # codigo=request.POST["codigo"]
        # cuit=request.POST["cuit"]
        # articulo=request.POST["articulo"]
        # cantidad=request.POST["cantidad"]
        pedido=Pedido_temp(idcliente=clienteid, idarticulo_id=id_cod,cantidad=cantidad, fecha=fecha)
        pedido.save()

        # pedidos=Pedido.objects.all()
        # productos=Articulos.objects.all()
        #return render(request,return HttpResponse(f"se agrego el articulo {articulo.codigo} , {articulo.descipcion}")return render(request,)
        
        
        return render(request, "AppCoder/productoconfirmado.html", {"artdescripcion":artdescripcion, "cantidad":cantidad})
        
        #return render(request, "AppCoder/articulos.html")
        
        
        #return HttpResponse(f"se agrego el articulo {id_cod}, {cuit}, {descripcion} ")
        #return render_to_response('template_name', message='Save complete')
        #return messages.add_message(request, messages.INFO, 'Hello world.')














def contacto(request):
            #******************envia correos texto plano
        nombre=request.POST["nombre"]
        correo=request.POST["correo"]
        cel=request.POST["cel"]
        msj=request.POST["mensaje"]

        destinatarios=["testpedidos2022@gmail.com"]
        print(nombre)
        print(correo)
        print(cel)
        print(msj)
       
        mensaje=(f"Se ha generado un formulario de contacto de {nombre} correo {correo} celular {cel} con el mensaje:{msj}" )
        #destinatarios=[]
        send_mail(
            'Nuevo pedido ingresado',
            mensaje,
            settings.EMAIL_HOST_USER,
            destinatarios,
             fail_silently=False
            )
        #**********************************
        return HttpResponse("se envio el correo")

def consultapedido(request, id_pedido):
    
        
        pedido=Pedido.objects.get(id=id_pedido)
        print(pedido)
        print(pedido.fecha)
        cli= pedido.idcliente
        print(cli)
        detalle=Detalle.objects.filter(pedido_id=id_pedido)
        print (detalle)
        #id_art=Pedido_temp.objects.values("idarticulo_id")
        #articulos=Articulos.objects.all()
        cliente=Clientes.objects.get(id=cli)
        articulos=Articulos.objects.all()
        print(detalle)
        contexto={"articulos":articulos, "detalle":detalle, "pedidos":pedido, "cliente":cliente}
        print(contexto)
        return render(request, "AppCoder/consultapedidos.html",contexto)


#--Importacion de articulos por archivo
def importar(request): 
    path = "c:\\articulos"
    os.chdir(path) 
# file="script\articulos.txt"
    lista=[]
    lista_final=[]
    dir = os.listdir(path) 
  
    if len(dir) == 0: 
        return HttpResponse("no hay archivos para inmportar")
    for file in os.listdir(): 
    #     archivo = open(path + '/' + file, 'r')      
    #     lectura= archivo.read()
    #     lista_final=[]
        with open (file) as lectura:
            for linea in lectura:
                #print(linea.rstrip())
                # separador=","
                # string_list=lectura.split(separador)
                # print(string_list)   
                # lista_final=[]
                lista.append(linea)
  
       
    # while(True):
    # #     linea = lectura.readline()
    # #     print("acaaaa")
    # #     print(linea)
    # #     if not linea:
    # #         break
    # # lectura.close()
    for x in range(len(lista)):
        texto=lista[x]
    #     #     #fecha= texto[2:21]
        separador1=","
        lista_datos=texto.split(separador1)
        lista_final.append(lista_datos)
   

    #     #lista_final.pop(0)

    for valor in range(len(lista_final)):   
        codigo=lista_final[valor][0]
        descripcion=lista_final[valor][1]
        stock=lista_final[valor][2]
        print(codigo)
        print(descripcion)
        print(stock)

    
    #           if "BACKUP DATABASE successfully processed" in lista_final[valor][3]:
    #             resultado="satisfactorio"
    #         else:
    #             resultado="revisar"
    #         fecha= lista_final[valor][0]
    #         emp=lista_final[valor][1]
    #         ruta=lista_final[valor][2]
    #         estado=resultado
        if Articulos.objects.filter(Codigo=codigo):
            Articulos.objects.filter(Codigo=codigo).update(stock=stock)
            #return HttpResponse("se actualizaron articulos")   
                
        else:
            articulo=Articulos(Codigo=codigo, descripcion=descripcion, stock=stock)
            articulo.save()

    #             mibkp=backup(fecha=fecha, empresa=emp,ruta=ruta, estado=estado)
            
    #             mibkp.save()

    return HttpResponse("se agregaron articulos")
    # backups=backup.objects.all()
    # return render(request, "AppCoder/backup.html",{"backups":backups,'time':datetime.now()})

#------------Importacion desde media--------------
def importarMedia(request): 
    # path = "c:\\articulos"
    # os.chdir(path) 
# file="script\articulos.txt"
    lista=[]
    lista_final=[]
    # dir = os.listdir(path) 
  
    # if len(dir) == 0: 
    #     return HttpResponse("no hay archivos para inmportar")
    # for file in os.listdir(): 
    # #     archivo = open(path + '/' + file, 'r')      
    # #     lectura= archivo.read()
   
    with open ("media/Uploaded/articulos.txt") as lectura:
            for linea in lectura:
                #print(linea.rstrip())
                # separador=","
                # string_list=lectura.split(separador)
                # print(string_list)   
                # lista_final=[]
                lista.append(linea)
  
       
    # while(True):
    # #     linea = lectura.readline()
    # #     print("acaaaa")
    # #     print(linea)
    # #     if not linea:
    # #         break
    # # lectura.close()
    for x in range(len(lista)):
        texto=lista[x]
    #     #     #fecha= texto[2:21]
        separador1=","
        lista_datos=texto.split(separador1)
        lista_final.append(lista_datos)
   

    #     #lista_final.pop(0)
    nuevo=0
    actualizado=0
    for valor in range(len(lista_final)):   
        codigo=lista_final[valor][0]
        descripcion=lista_final[valor][1]
        stock=lista_final[valor][2]


    
    #           if "BACKUP DATABASE successfully processed" in lista_final[valor][3]:
    #             resultado="satisfactorio"
    #         else:
    #             resultado="revisar"
    #         fecha= lista_final[valor][0]
    #         emp=lista_final[valor][1]
    #         ruta=lista_final[valor][2]
    #         estado=resultado
        if Articulos.objects.filter(Codigo=codigo):
            Articulos.objects.filter(Codigo=codigo).update(stock=stock)
            #return HttpResponse("se actualizaron articulos")   
            actualizado+=1    
        else:
            articulo=Articulos(Codigo=codigo, descripcion=descripcion, stock=stock)
            articulo.save()
            nuevo+=1


    #-------------ELIMINA ARCHIVO de actualizacion de articulos de la carpeta /media/uploaded-----------
    documents = Document.objects.all()
    for document in documents:
        document.delete()   


    return HttpResponse(f"se agregaron, {nuevo} articulos. Se actualizaron ,{actualizado} articulos")
#-------subir archivos--------------

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        #fileTitle = request.POST["fileTitle"]
        fileTitle = ""
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = Document.objects.all()

    return render(request, "AppCoder/uploadfile.html", context = {
        "files": documents
    })


#---------------Modifica estado de pedido / entregado
@login_required
def modificaPedido(request):
       
        #verifico si es un admin para continuar con la modificacion del estado del pedido

        if request.user.id == 1:
            if request.method == "POST":
                pedido=request.POST["pedido"]
                #entregado=request.POST["preparado"]
                entregado = request.POST.get('preparado')
                if not entregado:
                    entregado = False
                print(entregado)
                if entregado== "on":
                    
                    Pedido.objects.filter(id=pedido).update(entregado=1)
                    idp=Pedido.objects.get(id=pedido)
                    mensaje=(f"su pedido nro {pedido}, ya se encuentra preparado, listo para retirar" )
                else:
                    print("-------------------------------------")
                    Pedido.objects.filter(id=pedido).update(entregado=0)
                    idp=Pedido.objects.get(id=pedido)
                    mensaje=(f"su pedido nro {pedido}, esta en proceso de preparación" )
                #--consulto el correo del usuario
                
                
                cliente=Clientes.objects.get(id=idp.idcliente)
                
                usuario=User.objects.get(id=cliente.usuario_id)
                
                correo=usuario.email
                
                #----envio correo---------
                
                destinatarios=["testpedidos2022@gmail.com"]
                destinatarios.append(correo)
                send_mail(
                    'Estado de su pedido',
                    mensaje,
                    settings.EMAIL_HOST_USER,
                    destinatarios,
                    fail_silently=False
                )
                mensaje="el pedido se modifico correctamente"
                #return pedidos( request)
                return render(request, "AppCoder/pedido_modificacion.html", {"mensaje":mensaje})
                
                return HttpResponse("el pedido cambio su estado")
            else:
                return HttpResponse("get") 
        else:
            return HttpResponse("otro usuario") 
#------fin modifica pedido




#------IMAGENES DE ARTICULOS-------------


# #@login_required
# def upload_image_view(request):
#     if request.method == 'POST':
#         form = UploadImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             message = "Image uploaded succesfully!"
#     else:
#         form = UploadImageForm()
#     return httpresponse("111")
#     #return render_to_response('albums/upload.html', locals(), context_instance=RequestContext(request))


# def home_view(request):
#     return httpresponse("222")
#     #return render_to_response('base.html')
