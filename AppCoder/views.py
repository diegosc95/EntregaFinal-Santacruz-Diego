# Aquí están los paquetes que utilizaremos. 

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.contrib.auth.decorators import *
from django.contrib.auth.views import *
from AppCoder.models import *
from AppCoder.forms import *

from django.views.generic import *
from django.views.generic.edit import *
from django.contrib.auth.mixins import *


# Visualizaciones 

def ver_estudiantes(request):
    todos_estudiantes = Estudiantes.objects.all()
    return render(request, "ver_estudiantes.html", {"total": todos_estudiantes})

def ver_curso(request):
    todos_cursos = Curso.objects.all()
    return render(request, "ver_cursos.html", {"total": todos_cursos})

def ver_profesores(request):
    todos_profes = Profesor.objects.all()
    return render(request, "ver_profes.html", {"total": todos_profes})

def ver_entregables(request):
    todas_entregas = Entregable.objects.all()
    return render(request, "ver_entregas.html", {"total": todas_entregas})

def inicio(request):
    usuario = request.user
    imagen_url = None
    if usuario.is_authenticated:
        avatar = usuario.avatar_set.last()
        if avatar:
            imagen_url = avatar.imagen.url
    return render(request, "inicio.html", {"user": usuario, "imagen_url": imagen_url})


def sobremi(request):
    return render(request, "about.html")


# Creación de información.

@login_required
def crear_curso(request):
    if request.method == "POST":
        curso_nuevo = Curso(nombre=request.POST["curso_nombre"], comision=request.POST["curso_comision"])
        curso_nuevo.save()
        return render(request, "ver_cursos.html")
    return render(request, "crear_cursos.html")

@login_required
def crear_entregas(request):
    if request.method == "POST":
        nombre = request.POST["entregable_nombre"]
        fecha_entrega = request.POST["entregable_fecha"]
        entregado = request.POST.get("entregable") == "on"
        entrega_nueva = Entregable(nombre=nombre, fechaEntrega=fecha_entrega, entregado=entregado)
        entrega_nueva.save()
        return render(request, "ver_entregas.html")
    return render(request, "crear_entregas.html")

@login_required
def crear_profesores(request):
    if request.method == "POST":
        profe_nuevo = Profesor(nombre=request.POST["profesor_nombre"], apellido=request.POST["profesor_apellido"], email=request.POST["profesor_email"],profesion=request.POST["curso_profesion"])
        profe_nuevo.save()
        return render(request,"ver_profes.html")  
    return render(request,"crear_profes.html")    

@login_required
def crear_estudiante(request):
    if request.method == "POST":
        estudiante_nuevo = Estudiantes(nombre=request.POST["estudiante_nombre"], apellido=request.POST["estudiante_apellido"], email=request.POST["estudiante_email"],edad=request.POST["estudiante_edad"])
        estudiante_nuevo.save()
        return render(request,"ver_estudiantes.html")   
    return render(request,"crear_estudiantes.html") 


# Búsqueda de información 

def buscar_cursos(request):
    mensaje = None
    cursos = None
    if request.GET:
        nombre = request.GET.get("nombre", None)
        if nombre and nombre.strip(): 
            cursos = Curso.objects.filter(nombre__icontains=nombre)
            if cursos.exists():
                mensaje = f'¡Felicidades, hemos encontrado los siguientes cursos para: {nombre}'
            else:
                mensaje = f'Lo siento, no se encontraron cursos para: {nombre}'
        else:
            mensaje = 'Por favor, ingrese al menos un carácter para realizar la búsqueda.'
    return render(request, "ver_cursos.html", {"mensaje": mensaje, "cursos": cursos})

def buscar_cursos_sin_login(request):
    if request.method == 'GET':
        nombre = request.GET.get("nombre", None)
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, "ver_cursos.html", {"cursos": cursos})

def buscar_entregables(request):
    mensaje = None
    entregables = None
    if request.GET:
        nombre = request.GET.get("nombre", None)
        if nombre and nombre.strip():  # Verificar que el nombre no esté vacío o solo contenga espacios en blanco
            entregables = Entregable.objects.filter(nombre__icontains=nombre)
            if entregables.exists():
                mensaje = f'¡Felicidades, hemos encontrado las siguientes entregas para: {nombre}'
            else:
                mensaje = f'Lo siento, no se encontraron entregas para: {nombre}'
        else:
            mensaje = 'Por favor, ingrese al menos un carácter para realizar la búsqueda.'
    return render(request, "ver_entregas.html", {"mensaje": mensaje, "entregas": entregables})

def buscar_profes(request):
    mensaje = None
    profes = None
    if request.GET:
        apellido = request.GET.get("apellido", None)
        if apellido and apellido.strip():  # Verificar que el nombre no esté vacío o solo contenga espacios en blanco
            profes = Profesor.objects.filter(apellido__icontains=apellido)
            if profes.exists():
                mensaje = f'¡Felicidades, hemos encontrado los siguientes resultados para: {apellido}'
            else:
                mensaje = f'Lo siento, no se encontraron resultados para: {apellido}'
        else:
            mensaje = 'Por favor, ingrese al menos un carácter para realizar la búsqueda.'
    return render(request, "ver_profes.html", {"mensaje": mensaje, "profes": profes})

def buscar_estudiantes(request):
    mensaje = None
    estudiantes = None
    if request.GET:
        apellido = request.GET.get("apellido", None)
        if apellido and apellido.strip():  
            estudiantes = Estudiantes.objects.filter(apellido__icontains=apellido)
            if estudiantes.exists():
                mensaje = f'¡Felicidades, hemos encontrado los siguientes resultados para: {apellido}'
            else:
                mensaje = f'Lo siento, no se encontraron resultados para: {apellido}'
        else:
            mensaje = 'Por favor, ingrese al menos un carácter para realizar la búsqueda.'
    return render(request, "ver_estudiantes.html", {"mensaje": mensaje, "estudiantes": estudiantes})


# Actualización de información 

@login_required
def actualizar_estudiantes(request, id_estudiante):
    estudiante_elegido = Estudiantes.objects.get(id=id_estudiante)
    if request.method == "POST":
        estudiante_elegido.nombre = request.POST["estudiante_nombre"]
        estudiante_elegido.apellido = request.POST["estudiante_apellido"]
        estudiante_elegido.email = request.POST["estudiante_email"]
        estudiante_elegido.edad = request.POST["estudiante_edad"]
        estudiante_elegido.save()
        return redirect('Estudiantes')
    return render(request, "act_estudiantes.html", {"estudiante": estudiante_elegido})

@login_required
def actualizar_curso(request, id_curso):
    curso_elegido = Curso.objects.get(id=id_curso)
    if request.method == "POST":
        curso_elegido.nombre = request.POST["curso_nombre"]
        curso_elegido.comision = request.POST["curso_comision"]
        curso_elegido.save()
        return redirect('Curso')
    return render(request, "act_cursos.html", {"curso": curso_elegido})

@login_required
def actualizar_profesor(request, id_profesor):    
    profesor_elegido = Profesor.objects.get(id=id_profesor)
    if request.method == "POST":
        profesor_elegido.nombre = request.POST["profesor_nombre"]
        profesor_elegido.apellido = request.POST["profesor_apellido"]
        profesor_elegido.email = request.POST["profesor_email"]
        profesor_elegido.profesion = request.POST["profesor_profesion"]
        profesor_elegido.save()
        return redirect('Profes')
    return render(request, "act_profes.html", {"profesor": profesor_elegido})

@login_required
def actualizar_entregas(request, id_entregable):
    entregable_elegido = Entregable.objects.get(id=id_entregable)
    if request.method == "POST":
        entregable_elegido.nombre = request.POST["entregable_nombre"]
        entregable_elegido.fechaEntrega = request.POST["entregable_fechaEntrega"]
        # Convertir el valor del checkbox a un booleano
        entregable_elegido.entregado = request.POST.get("entregable_entregado") == "on"
        entregable_elegido.save()
        return redirect('Entregas')
    return render(request, "act_entregas.html", {"entregable": entregable_elegido})


# Eliminación de información 

@login_required
def borrar_estudiantes(request, id_estudiante):
    estudiante_elegido = Estudiantes.objects.get(id=id_estudiante)
    estudiante_elegido.delete()
    return redirect('Estudiantes')

@login_required
def borrar_entregas(request, id_entregable):  
    entregable_elegido = Entregable.objects.get(id=id_entregable)
    entregable_elegido.delete()
    return redirect('Entregas')

@login_required
def borrar_curso(request, id_curso):    
    curso_elegido = Curso.objects.get(id=id_curso)
    curso_elegido.delete()
    return redirect('Curso')

@login_required
def borrar_profesor(request, id_profesor):
    
    profesor_elegido = Profesor.objects.get(id=id_profesor)
    profesor_elegido.delete()
    return redirect('Profes') 


# Autenticación de usuarios

def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data= request.POST)
        if formulario.is_valid():
            info_dic = formulario.cleaned_data
            usuario = authenticate(username=info_dic["username"],password=info_dic["password"])
            if usuario is not None:
                login(request, usuario)
                return render(request,"inicio.html",{"mensaje":f'Bienvenido {usuario}'})           
        else:
            return render(request,"inicio.html",{"mensaje":"Informacion incorrecta. Por favor intente nuevamente"})
    else:
        formulario = AuthenticationForm()      
    return render(request,"iniciar_sesion.html",{"formu":formulario})

def registarse(request):
    if request.method == 'POST':
        formulario = Registrousuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request, "inicio.html", {"mensaje": f"El Usuario fue registrado correctamente."})
    else:
        formulario = Registrousuario()   
    return render(request, "registro.html", {"formu": formulario})

def cerrar_sesion(request):    
    logout(request)
    return render(request, "inicio.html",{"mensaje": "Tu sesión ha finalizado correctamente. ¡Hasta la próxima!"})

@login_required
def editar_usuario(request): 
    usuario = request.user
    if request.method == 'POST':
        miFormulario = Editarusuario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "inicio.html")
    else:

        miFormulario = Editarusuario(initial={'first_name':usuario.first_name,'last_name':usuario.last_name,'email': usuario.email})
    return render(request, "editar_usuario.html", {"formu": miFormulario, "usuario": usuario})

@login_required
def editar_username(request): 
    usuario = request.user
    if request.method == 'POST':
        miFormulario = Editarusuario_name(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.username = informacion['username']
            usuario.save()
            return render(request, "inicio.html")
    else:
        miFormulario = Editarusuario_name(initial={'username':usuario.username})
    return render(request, "editar_username.html", {"formu": miFormulario, "usuario": usuario})

class CambiarContra(LoginRequiredMixin, PasswordChangeView):
    template_name = "editar_contra.html"
    success_url = "/AppCoder/"

# Creacion de avar

@login_required
def crear_avatar(request):
    if request.method == 'POST':
        formulario = AvatarFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nuevo_avatar = Avatar(usuario=request.user, imagen=info["imagen"])
            nuevo_avatar.save()
            return render(request, "inicio.html", {"mensaje": "Haz agregado un avatar"})
    else:
        formulario = AvatarFormulario()
    return render(request, "nuevo_avatar.html", {"formu": formulario})




