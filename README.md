# Modulo-Asistencia

Este proyecto es una prueba tecnica de una aplicación web desarrollada con el framework Django.

## Requisitos previos

Asegúrate de tener instaladas las siguientes herramientas antes de comenzar:

- Python 3.8 o superior
- pip (el gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado)

## Configuración del entorno

### 1. Clonar el repositorio

Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/acardenasor/Modulo-Asistencia.git
cd Modulo-Asistencia
```

### 2. Crear y activar un entorno virtual

Es recomendable utilizar un entorno virtual para gestionar las dependencias del proyecto. Si no lo tienes instalado, puedes hacerlo con pip:

```bash
pip install virtualenv
```

Luego, crea y activa el entorno virtual:

```bash
# En sistemas Unix/macOS
virtualenv venv
source venv/bin/activate

# En Windows
virtualenv venv
.\venv\Scripts\activate
```

### 3. Instalar las dependencias

Instala las dependencias del proyecto usando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Migraciones de la base de datos

Aplica las migraciones para configurar la base de datos:

```bash
python manage.py migrate
```


### 5. Ejecución de datos por defecto

Aplica las migraciones para configurar la base de datos con datos por defecto:

```bash
python manage.py loaddata asistencia_estudiantil/fixtures/users
python manage.py loaddata asistencia_estudiantil/fixtures/asistencias
python manage.py loaddata asistencia_estudiantil/fixtures/cursos
python manage.py loaddata asistencia_estudiantil/fixtures/estudiantes
```

### 6. Crear un superusuario

Si necesitas acceso al panel de administración de Django, crea un superusuario:

```bash
python manage.py createsuperuser
```
O usar el superusuario existente
```bash
username: admin
password: admin2024
```

### 7. Ejecutar el servidor de desarrollo

Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

El proyecto estará disponible en [http://127.0.0.1:8000/asistente/login/](http://127.0.0.1:8000/asistente/login/).

## Capturas de pantalla

![image](https://github.com/user-attachments/assets/849971ab-3217-4642-a0cd-a1d287cf00ba)

![image](https://github.com/user-attachments/assets/31a21fd8-2b8f-4566-8226-78e237e0b0d4)


## Desarrollado por

Angela Maria Cardenas Orjuela
