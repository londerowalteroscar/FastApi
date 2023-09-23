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


