# EntregaFinal-Santacruz-Diego
Este proyecto Django, llamado "Registro de Cursos", es una aplicación web desarrollada como parte de mi trabajo práctico. Aquí encontrarás las instrucciones para que puedas ejecutar la aplicación localmente y verla en acción.
El mismo me base en gran medida en lo visto en las clases 19 a la 21, sumandole cosas que fui viendo por internet

## Requisitos previos

- Python instalado (versión sugerida: 3.12.2)
- Pip (instalador de paquetes de Python) instalado
- Git instalado

## Pasos para visualizar la aplicación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio

2. Instalar las dependencias:

   `pip install -r requirements.txt`

3. Aplicar migraciones:
  `python manage.py migrate`
   `python .\manage.py makemigrations`
  
4.  Iniciar la aplicación:
   `python manage.py runserver`

5. Visitar la aplicación:
   Abre tu navegador y visita http://127.0.0.1:8000/
   El panel de administración en http://127.0.0.1:8000/admin/.
   usuario: diegoCODER
   Password: Pyhton1234

7. Detener la aplicación:
   En la terminal donde ejecutaste runserver, presiona Ctrl + C para detener el servidor.


# Listado de Elemenos creados

1. Templates
- about.html
- act_cusos.html
- act_entregas.html
- act_estudiantes.html
- act_profes.html
- crear_cursos.html
- crear_entregas.html
- crear_estudiantes.html
- crear_profes.html
- editar_contra.html
- editar_username.html
- editar_usuario.html
- iniciar_sesion.html
- inicio.html
- nuevo_avatar.html
- padre.html
- registro-html
- ver_cursos.html
- ver_entregas.html
- ver_estudiantes.html
- ver_profes.html
  

2. Modelos
- Estudiantes
- Curso
- Profesor
- Entregable
- Avatar

3. URL http://127.0.0.1:8000/
- about/
- ""/
- login/
- logout/
- register/
- edit/
- username/
- password/
- avatar/
- crear_curso/
- crear_entregas/
- crear_profesores/
- crear_estudiantes/
- curso/
- entregas/
- profesores/
- estudiantes/
- buscar_curso/
- buscar_entregas/
- buscar_profesores/
- buscar_estudiantes/
- actualizar_estudiantes/
- actualizar_curso/
- actualizar_profesor/
- actualizar_entregas/
- borrar_estudiantes/
- borrar_entregas/
- borrar_curso/
- borrar_profesores/

4. Forms armados para el modelo
- Registrousuario
- Editarusuario
- Editarusuario_name
- AvatarFormulario 

5. Video explicativo de como funciona la APP
- https://youtu.be/zseXYo-WTi8

# Cualquier duda me avisan. Abrazo!
