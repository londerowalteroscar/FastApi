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