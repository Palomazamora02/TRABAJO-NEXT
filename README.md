Consulta de Clima con Streamlit 🌦️
![image](https://github.com/user-attachments/assets/d5fdc55b-ad13-42c5-b89f-cdef13199ff2)

Este proyecto consiste en una aplicación web interactiva que consulta el clima en tiempo real de cualquier ciudad utilizando la API de OpenWeatherMap. La aplicación está construida con Streamlit y presenta los datos de manera sencilla y visual a través de un chatbot.

La aplicación permite al usuario consultar el clima de cualquier ciudad, mostrando la temperatura, la humedad y la velocidad del viento. Utiliza una interfaz de chatbot donde el usuario puede ingresar una ciudad y obtener la respuesta en tiempo real.

Pasos Seguidos en el Desarrollo
-Obtención de la clave de API de OpenWeatherMap
Para poder consultar los datos del clima, se utilizó la API pública de OpenWeatherMap. Para acceder a esta API, es necesario crear una cuenta en su sitio web y obtener una clave de API personal.

-Desarrollo de la Aplicación con Streamlit
Streamlit es una biblioteca de Python que permite crear aplicaciones web interactivas de manera sencilla. A través de esta herramienta, se creó una interfaz en la que el usuario puede ingresar el nombre de una ciudad y consultar el clima.

La aplicación muestra un campo de texto donde el usuario puede escribir el nombre de la ciudad.
Luego, al presionar el botón "Consultar clima", se hace una solicitud a la API de OpenWeatherMap con la ciudad ingresada.

-Obtención de los Datos del Clima
Cuando el usuario ingresa una ciudad y presiona el botón de consulta, el sistema hace lo siguiente:

Solicitud HTTP: Realiza una solicitud GET a la API de OpenWeatherMap.
Parámetros: Se pasan los parámetros necesarios como el nombre de la ciudad, la clave de API, y la unidad de medida de temperatura (en grados Celsius).
Respuesta: La API devuelve los datos del clima en formato JSON, que luego se procesan en el código.
Los datos clave extraídos de la API incluyen:

Temperatura
Humedad
Velocidad del viento
Descripción del clima

-Visualización de los Datos
Los datos obtenidos de la API se presentan en la interfaz de la aplicación de la siguiente manera:

Temperatura: La temperatura actual de la ciudad.
Humedad: El porcentaje de humedad en el ambiente.
Viento: La velocidad del viento en metros por segundo.
Descripción: Un breve resumen del estado del clima (por ejemplo, "despejado", "nublado", etc.).

-Interacción del Usuario con el Chatbot
La aplicación está estructurada de forma que simula un chatbot. Esto significa que el usuario puede interactuar con la aplicación como si estuviera conversando con un asistente:

El usuario escribe un mensaje solicitando información sobre el clima.
La aplicación responde con los datos obtenidos de la API, simulando una conversación fluida y amigable.

-Manejo de Errores
Si el usuario ingresa un nombre de ciudad incorrecto o si ocurre algún error al consultar la API, la aplicación muestra un mensaje de error, indicando que no se pudo obtener el clima para esa ciudad y sugiriendo intentar nuevamente.

-Despliegue de la Aplicación
La aplicación se ejecuta en un servidor local, y una vez que se ejecuta con el siguiente comando:

bash
Copiar
Editar
streamlit run clima_app.py
La aplicación estará disponible en un navegador a través de la URL http://localhost:8501.

9. Pruebas
Durante el desarrollo se realizaron pruebas con diferentes ciudades para asegurar que los datos del clima se consultaran correctamente. También se verificó el manejo de errores en caso de que la ciudad no existiera o si la conexión con la API fallaba. Además, se hizo una prueba con otro URL y otraa API pero me daba que no había ningún código y no supe como arreglarlo


CÓDIGO CLIMA

# Tu clave de API de OpenWeatherMap
api_key = "tu_clave_api_aqui"  # Asegúrate de reemplazar con tu clave de API de OpenWeatherMap

# URL base de la API de OpenWeatherMap
url = "https://api.openweathermap.org/data/2.5/weather"

# Título de la app
st.title("🌦️ Consulta el Clima 🌦️")

# Crear un área de conversación para el "chatbot"
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Función para obtener el clima
def obtener_clima(ciudad):
    params = {
        "q": ciudad,
        "appid": api_key,
        "units": "metric",  # Para obtener la temperatura en grados Celsius
        "lang": "es"  # Respuesta en español
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Función para agregar el mensaje al chat
def add_message(message, role='user'):
    st.session_state.messages.append({'role': role, 'content': message})

# Muestra el historial de mensajes
for message in st.session_state.messages:
    if message['role'] == 'user':
        st.markdown(f"**Usuario**: {message['content']}")
    else:
        st.markdown(f"**Chatbot**: {message['content']}")

# Obtener la ciudad de clima del usuario
ciudad = st.text_input("Ingresa el nombre de la ciudad:")

# Cuando el usuario haga clic en el botón, se consulta el clima y se muestran los datos
if st.button("Consultar clima"):
    add_message(f"Quiero saber el clima de {ciudad}.", role='user')  # El mensaje del usuario
    data = obtener_clima(ciudad)  # Obtener los datos del clima

    if data:
        nombre_ciudad = data['name']
        pais = data['sys']['country']
        descripcion = data['weather'][0]['description']
        temperatura = data['main']['temp']
        humedad = data['main']['humidity']
        viento = data['wind']['speed']

        # Responder al usuario con la información del clima
        add_message(f"🌍 El clima en {nombre_ciudad}, {pais} es:\n{descripcion.capitalize()}\n🌡️ Temperatura: {temperatura}°C\n💧 Humedad: {humedad}%\n🌬️ Viento: {viento} m/s", role='chatbot')
    else:
        add_message("Lo siento, no pude obtener el clima de esa ciudad. Verifica el nombre e intenta nuevamente.", role='chatbot')

    # Volver a mostrar los mensajes al final
    for message in st.session_state.messages:
        if message['role'] == 'user':
            st.markdown(f"**Usuario**: {message['content']}")
        else:
            st.markdown(f"**Chatbot**: {message['content']}")
