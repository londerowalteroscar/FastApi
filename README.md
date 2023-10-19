# FastApi
¡Hola! FastAPI es un marco de desarrollo web de Python de alto rendimiento y fácil de usar. Está diseñado para crear API rápidas y escalables con documentación automática. FastAPI utiliza el tipado estático de Python, lo que lo hace muy rápido y eficiente. Además, es compatible con la especificación OpenAPI y proporciona una generación automática de documentación interactiva.
FastAPI ofrece una serie de características de seguridad para ayudarte a crear APIs seguras y proteger tus aplicaciones. Algunas de las medidas de seguridad que puedes implementar en FastAPI incluyen:

1. Validación de datos: FastAPI utiliza el tipado estático de Python y la validación automática de datos, lo que ayuda a prevenir errores y vulnerabilidades relacionados con la entrada de datos.

2. Autenticación: Puedes implementar diferentes métodos de autenticación, como tokens JWT (JSON Web Tokens) o esquemas OAuth, para asegurarte de que solo los usuarios autorizados puedan acceder a tus APIs.

3. Autorización: FastAPI te permite definir permisos y roles para controlar qué usuarios tienen acceso a determinadas rutas o funciones dentro de tu API.

4. Protección contra ataques de seguridad conocidos: FastAPI incluye protecciones integradas contra ataques comunes, como ataques de inyección SQL, ataques de cross-site scripting (XSS) y ataques de falsificación de solicitudes entre sitios (CSRF).

Sin embargo, es importante tener en cuenta que la seguridad de tu API no solo depende del marco de desarrollo que utilices, sino también de cómo diseñes y implementes tus propias capas de seguridad. Es recomendable seguir buenas prácticas de seguridad, como validar y sanitizar la entrada de datos, utilizar conexiones seguras (HTTPS), implementar políticas de control de acceso adecuadas y mantener tus dependencias actualizadas para mitigar posibles vulnerabilidades.

# Creación de Entorno virtual:
1. Comando para crear el entorno, la ultima palabra es el nombre que le asignamos nosotros.
    - python -m venv venv
2. Activamos el entorno virtual:
    - ./venv/Scripts/activate
3. Actualizamos pip:
    - python -m pip install --upgrade pip
4. Instalar FastApi:
    - pip install fastapi
5. Instalamos uvicorn:
    - pip install uvicorn
6. Instalar las demas librerias que se necesiten en el proyecto, pues el entorno virtual esta limpio y no contiene ninguna libreria del entorno Global.
7. Uvicorn:
Uvicorn es un servidor ASGI (Asynchronous Server Gateway Interface) de alto rendimiento, diseñado específicamente para trabajar con aplicaciones web desarrolladas en Python. Algunas de las cualidades destacadas de Uvicorn son:

    1. Rendimiento: Uvicorn está construido sobre el bucle de eventos asincrónicos de Python, lo que le permite manejar múltiples solicitudes simultáneamente de manera eficiente y escalable. Esto lo convierte en una opción ideal para aplicaciones web de alta carga.

    2. Compatibilidad con ASGI: Uvicorn sigue la especificación ASGI, que es un estándar para el desarrollo de aplicaciones web asincrónicas en Python. Esto significa que es compatible con una amplia gama de marcos y bibliotecas basadas en ASGI, como FastAPI, Django, Starlette, entre otros.

    3. Fácil de usar: Uvicorn es fácil de configurar y utilizar. Solo necesitas especificar el archivo de entrada de tu aplicación y ejecutar el servidor Uvicorn para poner en marcha tu aplicación web.

    4. Soporte para recarga en caliente (hot-reloading): Uvicorn tiene la capacidad de recargar automáticamente tu aplicación cuando detecta cambios en los archivos fuente. Esto facilita el desarrollo y la depuración, ya que no necesitas reiniciar el servidor manualmente cada vez que realices cambios en tu código.

    En resumen, Uvicorn es un servidor ASGI de alto rendimiento y fácil de usar que te permite ejecutar aplicaciones web Python de manera eficiente y escalable. Es una opción popular para el despliegue de aplicaciones web modernas y asincrónicas.

    Ya lo tenemos instalado, procedemos a inicializarlo:
    - uvicorn main:app --reload
8. Para cerrar el cervidor es:
    - Ctrl + c
9. Para cambiar el puerto:
    - uvicorn main:app --reload --port 50000
10. Para cambiar puerto y host y hacer con que la api sea consumible por cualquier ordenador de la red es:
    - uvicorn main:app --reload --port 50000 --host 0.0.0.0

Preparación y subida del repositorio:

1. Crea un repositorio en GitHub: Inicia sesión en tu cuenta de GitHub y crea un nuevo repositorio. Puedes darle un nombre, una descripción y elegir si quieres que sea público o privado. 

2. Configura Git: Asegúrate de tener Git instalado en tu computadora y configura tu nombre de usuario y dirección de correo electrónico en Git utilizando los siguientes comandos en tu terminal:

    - git config --global user.name "Tu Nombre"
    - git config --global user.email "tu@email.com"

3. Inicializa tu repositorio local: Abre la terminal, navega hasta el directorio raíz de tu proyecto y ejecuta el siguiente comando para inicializar un repositorio Git local:
    - git init

4. Agrega los archivos y realiza el commit inicial: Utiliza el siguiente comando para agregar todos los archivos de tu proyecto al área de preparación de Git:
    - git add .
    Luego, realiza el commit inicial con un mensaje descriptivo:
    - git commit -m "Commit inicial"

5. Conecta tu repositorio local con el repositorio remoto en GitHub: Copia la URL del repositorio remoto que creaste en GitHub. Luego, ejecuta el siguiente comando para conectar tu repositorio local con el remoto:
    - git remote add origin <URL_del_repositorio>

6. Sube tu proyecto a GitHub: Finalmente, utiliza el siguiente comando para subir tu proyecto al repositorio remoto en GitHub:
    - git push -u origin master
    Esto enviará tus archivos al repositorio remoto y establecerá una relación de seguimiento entre tu repositorio local y el remoto. 
# Ramas en GitHub
Para solucionar el problema de tener dos ramas en tu repositorio y no haber obtenido los resultados esperados, puedes seguir estos pasos: 
 
1. Verifica las ramas existentes: Utiliza el siguiente comando en tu terminal para ver las ramas actuales en tu repositorio:
    - git branch
Este comando mostrará una lista de todas las ramas en tu repositorio local y resaltará la rama actual con un asterisco (*). 
 
2. Cambia a la rama deseada: Si deseas trabajar en una rama específica, puedes cambiar a ella utilizando el siguiente comando:
    - git checkout nombre_de_la_rama
Reemplaza "nombre_de_la_rama" con el nombre de la rama en la que deseas trabajar. 
 
3. Fusiona las ramas o realiza cambios necesarios: Si tienes cambios en ambas ramas y deseas fusionarlos, puedes utilizar el comando  git merge  para combinar los cambios de una rama en otra. Por ejemplo, si deseas fusionar los cambios de la rama "rama1" en la rama "rama2", ejecuta el siguiente comando:
    - git checkout rama2.
    - git merge rama1.
    
Si solo deseas descartar una de las ramas y trabajar solo en una, puedes eliminar la rama no deseada utilizando el siguiente comando:    
    - git branch -d nombre_de_la_rama.
Reemplaza "nombre_de_la_rama" con el nombre de la rama que deseas eliminar. 
 
Recuerda que estos comandos se aplican a tu repositorio local. Si deseas reflejar los cambios en tu repositorio remoto en GitHub, deberás utilizar el comando  git push  después de realizar los cambios necesarios. 
 
Espero que estos pasos te ayuden a solucionar el problema con las ramas en tu repositorio. Si tienes alguna otra pregunta, no dudes en preguntar.

# Documentación Automática

A la dirección http://127.0.0.1:8000 le agregamos "docs":
- http://127.0.0.1:8000/docs

Titulo de la Aplicación de FastAPI:
app.title = "Tutorial FastApi"

Versión de la Aplicación de FastAPI:
app.version = "1.0.1"

Crear punto de entreada o endpoint:
@app.get("/", tags = ["Bienvenida"]) # Cambio de etiqueta en documentación.

Para devolver diccionarios en FastApi importamos:   
    - from fastapi.responses import HTMLResponse

# Métodos

## El método GET
El método GET es uno de los métodos HTTP más comunes. Se utiliza para recuperar información de un servidor. En FastAPI, el método GET se utiliza para definir una ruta que permite a los usuarios obtener datos de un recurso.

Para utilizar el método GET en FastAPI, debemos usar la anotación @app.get() para definir una ruta. Por ejemplo, el siguiente código define una ruta que permite a los usuarios obtener la lista de todos los usuarios:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"},
    ]
```

Este código define una ruta llamada `/users`. Cuando un usuario realiza una petición GET a esta ruta, FastAPI devolverá una lista de todos los usuarios.

El método GET también se puede utilizar para recuperar datos de un recurso específico. Para ello, podemos utilizar parámetros en la ruta. Por ejemplo, el siguiente código define una ruta que permite a los usuarios obtener un usuario específico por su ID:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": "John Doe"}
```

Este código define una ruta llamada `/users/{user_id}`. El parámetro `user_id` es un parámetro de ruta obligatorio. Cuando un usuario realiza una petición GET a esta ruta, FastAPI devolverá los datos del usuario con el ID especificado.

El método GET se utiliza en una amplia gama de aplicaciones. Por ejemplo, se puede utilizar para:

* Recuperar la lista de productos de una tienda online.
* Recuperar la lista de noticias de un sitio web.
* Recuperar la información de un usuario de una base de datos.

En resumen, el método GET en FastAPI se utiliza para definir rutas que permiten a los usuarios obtener datos de un recurso.

## El método POST

El método POST es un método HTTP que se utiliza para crear o actualizar datos en un recurso. En FastAPI, el método POST se utiliza para definir rutas que permiten a los usuarios crear o actualizar datos.

Para utilizar el método POST en FastAPI, debemos usar la anotación @app.post() para definir una ruta. Por ejemplo, el siguiente código define una ruta que permite a los usuarios crear un nuevo usuario:

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users")
def create_user(name: str, email: str):
    return {"name": name, "email": email}
```

Este código define una ruta llamada `/users`. Cuando un usuario realiza una petición POST a esta ruta, FastAPI creará un nuevo usuario con los datos especificados en los parámetros `name` y `email`.

El método POST también se puede utilizar para actualizar datos en un recurso existente. Para ello, podemos utilizar parámetros en la ruta. Por ejemplo, el siguiente código define una ruta que permite a los usuarios actualizar el nombre de un usuario:

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users/{user_id}")
def update_user_name(user_id: int, name: str):
    return {"id": user_id, "name": name}
```

Este código define una ruta llamada `/users/{user_id}`. El parámetro `user_id` es un parámetro de ruta obligatorio. Cuando un usuario realiza una petición POST a esta ruta, FastAPI actualizará el nombre del usuario con el ID especificado con el valor especificado en el parámetro `name`.

El método POST se utiliza en una amplia gama de aplicaciones. Por ejemplo, se puede utilizar para:

* Crear un nuevo usuario en una aplicación web.
* Crear una nueva orden de compra en una tienda online.
* Crear una nueva entrada en un blog.

En resumen, el método POST en FastAPI se utiliza para definir rutas que permiten a los usuarios crear o actualizar datos en un recurso.

## El método PUT

El método PUT es un método HTTP que se utiliza para actualizar datos en un recurso. En FastAPI, el método PUT se utiliza para definir rutas que permiten a los usuarios actualizar datos en un recurso existente.

Para utilizar el método PUT en FastAPI, debemos usar la anotación @app.put() para definir una ruta. Por ejemplo, el siguiente código define una ruta que permite a los usuarios actualizar la fecha de una venta:

```python
from fastapi import FastAPI

app = FastAPI()

@app.put("/ventas/{id}")
def actualiza_fecha_venta(id: int, fecha: str):
    # Recorrer elementos de una lista.
    for elem in ventas:
        if elem["id"] == id:
            elem["fecha"] = fecha
    return ventas
```

Este código define una ruta llamada `/ventas/{id}`. El parámetro `id` es un parámetro de ruta obligatorio. Cuando un usuario realiza una petición PUT a esta ruta, FastAPI actualizará la fecha de la venta con el ID especificado con el valor especificado en el parámetro `fecha`.

El método PUT se utiliza en una amplia gama de aplicaciones. Por ejemplo, se puede utilizar para:

* Actualizar la fecha de una reserva en una aplicación de viajes.
* Actualizar el precio de un producto en una tienda online.
* Actualizar la contraseña de un usuario en una aplicación web.

En resumen, el método PUT en FastAPI se utiliza para definir rutas que permiten a los usuarios actualizar datos en un recurso existente.

En comparación con el método POST, el método PUT tiene las siguientes ventajas:

* Es más eficiente, ya que no es necesario crear un nuevo recurso.
* Es más seguro, ya que el recurso existente se puede validar antes de actualizarlo.

Sin embargo, el método PUT tiene una desventaja:

* No se puede utilizar para crear nuevos recursos.

Para crear nuevos recursos, debemos utilizar el método POST.

El método DELETE es un método HTTP que se utiliza para eliminar un recurso. En FastAPI, el método DELETE se utiliza para definir rutas que permiten a los usuarios eliminar un recurso existente.

Para utilizar el método DELETE en FastAPI, debemos usar la anotación @app.delete() para definir una ruta. Por ejemplo, el siguiente código define una ruta que permite a los usuarios eliminar una venta:

```python
from fastapi import FastAPI

app = FastAPI()

@app.delete("/ventas/{id}")
def elimina_venta(id: int):
    # Recorrer elementos de una lista.
    for elem in ventas:
        if elem["id"] == id:
            ventas.remove(elem)
    return ventas
```

Este código define una ruta llamada `/ventas/{id}`. El parámetro `id` es un parámetro de ruta obligatorio. Cuando un usuario realiza una petición DELETE a esta ruta, FastAPI eliminará la venta con el ID especificado.

## El método DELETE

El método DELETE es un método HTTP que se utiliza para eliminar un recurso. En FastAPI, el método DELETE se utiliza para definir rutas que permiten a los usuarios eliminar un recurso existente.

Para utilizar el método DELETE en FastAPI, debemos usar la anotación @app.delete() para definir una ruta. Por ejemplo, el siguiente código define una ruta que permite a los usuarios eliminar una venta:

```python
from fastapi import FastAPI

app = FastAPI()

@app.delete("/ventas/{id}")
def elimina_venta(id: int):
    # Recorrer elementos de una lista.
    for elem in ventas:
        if elem["id"] == id:
            ventas.remove(elem)
    return ventas
```

Este código define una ruta llamada `/ventas/{id}`. El parámetro `id` es un parámetro de ruta obligatorio. Cuando un usuario realiza una petición DELETE a esta ruta, FastAPI eliminará la venta con el ID especificado.

El método DELETE se utiliza en una amplia gama de aplicaciones. Por ejemplo, se puede utilizar para:

* Eliminar una publicación de un blog.
* Eliminar una cuenta de usuario.
* Eliminar un archivo.

En resumen, el método DELETE en FastAPI se utiliza para definir rutas que permiten a los usuarios eliminar un recurso existente.

En comparación con el método PUT, el método DELETE tiene las siguientes ventajas:

* Es más eficiente, ya que no es necesario actualizar un recurso existente.
* Es más seguro, ya que el recurso existente se puede validar antes de eliminarlo.

Sin embargo, el método DELETE tiene una desventaja:

* No se puede utilizar para actualizar datos en un recurso existente.

Para actualizar datos en un recurso existente, debemos utilizar el método PUT.
