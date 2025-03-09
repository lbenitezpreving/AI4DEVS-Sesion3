### Con el rol de un desarrollador de software experimentado vamos a crear un proyecto desde cero.

### El software a desarrollar va a ser un ATS (Applicant Tracking System), relacionado con un sistema de gestión de candidatos para nuestra empresa denominada LTI.

### Primero, vamos a crear, lo siguiente:
* Archivo README.md con la descripción de la aplicación utilizando markdown
* Archivo para gestionar las versiones de la aplicación. Utilizará el estandar X.Y.Z
    * Inicializalo con la versión 1.0.0
* Archivo .gitignore
* Archivo .cursorrules
* Archivo de licencias según los estándares
* Carpeta para el backend
* Carpeta para el frontend
* Carpeta para todo lo relacionado con la base de datos
* Carpeta para generación de documentación denominada docs

### Consideraciones a tener en cuenta:
* Vamos a utilizar DDD y TDD
* Vamos a utilizar git para el control de versiones

### Los componentes que tendrá serán los siguientes:
* Base de datos postgresql
    * Genera un fichero docker para inicializar la base de datos, que contenga las credenciales de acceso a la misma y que nos permita ejecutarlo
    * Añade al README toda la información necesaria para arrancar la base de datos y acceder a ella
* Backend desarrollado en python utilizando el framework FASTAPI
    * Se utilizará la última versión estable de python y fastapi
    * Genera el código base necesario para poder arrancar la aplicación
    * Instala las librerías necesarias para utilizar FASTAPI
    * Instala las librerías necesarias para conectar a una base de datos postgresql
    * Configura el acceso a la base de datos postgresql creada en el punto anterior, utilizando las credenciales generadas
    * Instala las librerías necesarias para desarrollar test unitarios
    * Añade al archivo .gitignore todo lo necesario
    * Añade al archivo .cursorrules todo lo necesario
* Fronted desarrollo en angular
    * Se utilizará la última versión estable    
    * Genera el código base necesario para poder arrancar la aplicación
    * Añade al archivo .gitignore todo lo necesario
    * Añade al archivo .cursorrules todo lo necesario

### Por último:
* Actualiza el fichero README con toda la información que consideres oportuna a partir de todos los pasos dados según las indicaciones.
* Ejecuta los comandos necesarios para subir al repositorio git todo lo realizado.