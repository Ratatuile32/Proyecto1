# Lista de empleados
## Descripcion
Este programa solo funciona como un backend que genera API rest de una base de datos en forma de json
## Instalacion
Para el uso de este servidor recomiendo el uso de un entorno virtula usando "virtualenv".
Usaremos pip para instalarlo en la terminal de visualcode
```bash
pip install virtualenv
```
Luego usaremos virtualenv para crear el entorno virtual usando como lenguaje python3
```bash
virtualenv -p python3 env
```
Esto creara una carpeta en la que se aloja todos los paquetes, para usar la consola del entorno virtual usaremos el siguiente comando
```bash
.\env\Scripts\activate     
```
Luego de esto antes de la linea de comando aparecera (env) esto significara que ya estamos trabajando con la consola del entorno virtual, en ella empezaremos a instalar las dependencias necesarias, para lo cual usaremos pip
```bash
pip install setuptools wheels flask flask_mysqldb
```
luego usaremos "pip list" para revisar la instalacion y deberia quedar como esta lista
# ![alt text](image-1.png)
tras esto la instalacion ya deberia estar completa tan solo faltaria que crees la base de datos o en todo caso exportar la adjunta en este archivo, para modificar el host, user, contraseña y el nombre de la base de datos deberas ir a src/config.py dentro de este archivo esta la configuracion basica del servidor y los datos para la base de datos