# ProyectoCoder

Proyecto Django: AppCoder

Este proyecto es una aplicación web desarrollada con Django que permite gestionar cursos, estudiantes, profesores y entregables. Incluye funcionalidades para crear, editar, eliminar y buscar registros, así como formularios para la entrada de datos.

# Características Principales:

Gestión de Cursos: Crear, listar, editar y eliminar cursos.

Gestión de Estudiantes: Registrar y listar estudiantes.

Gestión de Profesores: Registrar y listar profesores.

Gestión de Entregables: Listar entregables asociados.

Búsqueda de Cursos: Buscar cursos por nombre.

Formularios Personalizados: Utilización de formularios para la entrada de datos.


# Tecnologías Utilizadas:

Backend: Django 3.x

Frontend: HTML5, CSS3

Base de Datos: SQLite (por defecto de Django)

Otros: Bootstrap (opcional para estilos)


# Estructura del Proyecto:

AppCoder/views.py: Contiene las vistas para manejar las operaciones CRUD y formularios.

AppCoder/models.py: Define los modelos Curso, Estudiante, Profesor y Entregable.

AppCoder/forms.py: Formularios personalizados para cada modelo.

AppCoder/templates/AppCoder/: Plantillas HTML para cada sección de la aplicación.

AppCoder/static/assets/img: Contiene las imágenes de la platilla descargada de Bootstraps.

AppCoder/static/css: Contiene los códigos css para los estilos de las páginas HTML.

AppCoder/static/js: Contiene los códigos js para darle dinamismo a las páginas HTML.


# Funcionalidades Detalladas:

Inicio: Página principal de la aplicación.

Cursos:

Listado de cursos.

Alta de cursos mediante formulario o URL.

Edición y eliminación de cursos.

Estudiantes:

Listado de estudiantes.

Alta de estudiantes mediante formulario.

Profesores:

Listado de profesores.

Alta de profesores mediante formulario.

Entregables:

Listado de entregables. No se han desarrollado las altas y modificaciones
de los entregables, porque queda fuera del alcance de este final. Porque
se debería analizar el login con el tipo de usuario profesor solamente.

Este README.md proporciona una visión general clara y concisa de tu proyecto, facilitando a otros desarrolladores la comprensión y contribución al mismo.

# Testing del Proyecto:

Se crearon dos tipos de usuarios para las pruebas:

Tipo admnistrador: tiene la facultad de poder listar todos los usuarios
cargados en la base de datos, y puede editar solo su perfil. Y tiene permisos totales sobre todas las funciones.

Tipo operador: tiene permisos de cargar y modificar en todas las funciones, pero no tiene permitido borrar.
También puede editar su perfil.

Listado de Usuarios para testing:
Administrador: eneue2025
Clave: Pass1234$2

Operador: operador2
Clave: Pass4321


