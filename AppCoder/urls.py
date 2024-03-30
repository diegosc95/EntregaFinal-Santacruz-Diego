from django.urls import path
from AppCoder.views import *

urlpatterns = [
    
    path('about/', sobremi, name="about"),
    path('', inicio, name="Home"),
    path('login/', iniciar_sesion, name="login"),
    path('logout/', cerrar_sesion, name="logout"),
    path('register/', registarse, name="registro"),
    path('edit/', editar_usuario, name="editar_usuario"),
    path('username/', editar_username, name="editar_username"),
    path('password/', CambiarContra.as_view(), name="editar_contra"),
    path('avatar/', crear_avatar, name="avatar"),

    path('crear_curso/', crear_curso, name="Crear_Curso"),
    path('crear_entregas/', crear_entregas, name="Crear_Entregas"),
    path('crear_profesores/', crear_profesores, name="Crear_Profes"),
    path('crear_estudiantes/', crear_estudiante, name="Crear_Estudiantes"),

    path('curso/', ver_curso, name="Curso"),
    path('entregas/', ver_entregables, name="Entregas"),
    path('profesores/', ver_profesores, name="Profes"),
    path('estudiantes/', ver_estudiantes, name="Estudiantes"),

    path('buscar_curso/', buscar_cursos, name="buscar_curso"),
    path('buscar_entregas/', buscar_entregables, name="buscar_entregas"),
    path('buscar_profesores/', buscar_profes, name="buscar_profesores"),
    path('buscar_estudiantes/', buscar_estudiantes, name="buscar_estudiantes"),

    path('actualizar_estudiantes/<int:id_estudiante>/', actualizar_estudiantes, name="actualizar_estudiantes"),
    path('actualizar_curso/<int:id_curso>/', actualizar_curso, name="actualizar_curso"),
    path('actualizar_profesor/<int:id_profesor>/', actualizar_profesor, name="actualizar_profesor"),
    path('actualizar_entregas/<int:id_entregable>/', actualizar_entregas, name="actualizar_entregas"),
    
    path('borrar_estudiantes/<int:id_estudiante>/', borrar_estudiantes, name="borrar_estudiantes"),
    path('borrar_entregas/<int:id_entregable>/', borrar_entregas, name="borrar_entregas"),
    path('borrar_curso/<int:id_curso>/', borrar_curso, name="borrar_curso"),
    path('borrar_profesores/<int:id_profesor>/', borrar_profesor, name="borrar_profesor"), 
    
]
