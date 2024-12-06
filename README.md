
# Proyecto de Encuestas

Este proyecto es una aplicación web de encuestas que utiliza Django como framework principal. A continuación se explican los pasos para clonar el repositorio, crear una imagen Docker llamada `encuestas`, y luego crear un contenedor basado en esa imagen con el mismo nombre.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas en tu máquina:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/get-started)

## Pasos para ejecutar la aplicación con Docker

### 1. Clonar el repositorio

Primero, clona este repositorio a tu máquina local:

```bash
git clone https://github.com/hanz-saenz/encuestas.git
```

Navega al directorio del proyecto:

```bash
cd encuestas
```

### 2. Crear la imagen Docker

A continuación, crea la imagen Docker. Asegúrate de tener un archivo `Dockerfile` en la raíz del proyecto con las instrucciones necesarias para construir la imagen.

Para crear la imagen, ejecuta el siguiente comando en la terminal:

```bash
docker build -t encuestas .
```

Esto construirá una imagen Docker con el nombre `encuestas`. El punto `.` indica que el `Dockerfile` está en el directorio actual.

### 3. Crear el contenedor basado en la imagen

Una vez que la imagen se haya creado correctamente, puedes crear un contenedor basado en esa imagen y darle el mismo nombre `encuestas`. Ejecuta el siguiente comando:

```bash
docker run --name encuestas -d -p 8001:8001 encuestas
```

Este comando hará lo siguiente:
- **--name encuestas**: Asigna el nombre `encuestas` al contenedor.
- **-d**: Ejecuta el contenedor en modo "detached" (en segundo plano).
- **-p 8001:8001**: Mapea el puerto 8000 de tu máquina local al puerto 8000 del contenedor.
- **encuestas**: El nombre de la imagen a partir de la cual se va a crear el contenedor.

### 4. Acceder a la aplicación

Una vez que el contenedor esté ejecutándose, puedes acceder a la aplicación visitando `http://localhost:8001` en tu navegador.

### 5. Verificar los contenedores en ejecución

Para ver los contenedores en ejecución, puedes usar el siguiente comando:

```bash
docker ps
```

### 6. Detener el contenedor

Si necesitas detener el contenedor, usa el siguiente comando:

```bash
docker stop encuestas
```

### 7. Eliminar el contenedor

Si deseas eliminar el contenedor, ejecuta:

```bash
docker rm encuestas
```

### 8. Eliminar la imagen

Si deseas eliminar la imagen Docker, puedes hacerlo con el siguiente comando:

```bash
docker rmi encuestas
```

## Notas

- Asegúrate de tener configurados correctamente los archivos de dependencias como `requirements.txt` si tu proyecto lo requiere, para que el `Dockerfile` los instale al momento de construir la imagen.
- Si tienes volúmenes de datos, asegúrate de mapearlos correctamente en el contenedor.

