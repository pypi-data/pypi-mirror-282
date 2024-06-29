# Flask Auto

Flask Auto es una librería para generar proyectos Flask automáticamente con una estructura básica de carpetas y archivos, incluyendo soporte para Docker y configuración de base de datos.

## Instalación

Para instalar Flask Auto, usa pip:

```sh
pip install flask_auto

```

## Uso

Para crear un nuevo proyecto Flask, ejecuta el siguiente comando:

```sh
    create_flask_app <project_name> <destination_directory>

```

- <project_name>: Nombre del proyecto.
- <destination_directory>: Directorio donde se creará el proyecto.



## Ejemplo 

Para crear un proyecto llamado my_flask_project en el directorio actual, puedes usar el siguiente comando:

```sh
    create_flask_app my_flask_project .

```

Este comando generara la siguiente estructura de carpetas y archivos

my_flask_project/
│
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── __init__.py
│   ├── views/
│   │   └── __init__.py
│   ├── controllers/
│   │   └── __init__.py
│   ├── templates/
│   ├── utils/
│       └── __init__.py
│
├── venv/
├── requirements.txt
├── run.py
├── .gitignore
├── Dockerfile
├── .dockerignore
└── .env


Detalles de los Archivos Generados
app/: Contiene la aplicación Flask.
models/: Carpeta para definir los modelos de la base de datos.
views/: Carpeta para las vistas de la aplicación.
controllers/: Carpeta para los controladores de la aplicación.
templates/: Carpeta para las plantillas HTML.
utils/: Carpeta para utilidades y funciones auxiliares.
venv/: Entorno virtual para la instalación de dependencias.
requirements.txt: Archivo con las dependencias de la aplicación.
run.py: Script principal para ejecutar la aplicación.
.gitignore: Archivo para excluir ciertos archivos y carpetas del control de versiones.
Dockerfile: Archivo de configuración para Docker.
.dockerignore: Archivo para excluir ciertos archivos y carpetas de la imagen de Docker.
.env: Archivo para variables de entorno, como la configuración de la base de datos.
Ejecución del Proyecto
Después de crear el proyecto, sigue estos pasos para ejecutarlo:

Activa el entorno virtual (si no está ya activado):

En Windows:

``` sh
    my_flask_project\venv\Scripts\activate

```

En macOS o Linux

``` sh
    source my_flask_project/venv/bin/activate
```

Navega al directorio:

cd my_flask_project


Ejecuta la app: 

python run.py





