"""CLIMA


"""

import streamlit as st
import requests

# Tu clave de API de OpenWeatherMap
api_key = "d5091510bfc557236997dc071e7fdbcf"  # Asegúrate de reemplazar con tu clave de API de OpenWeatherMap

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
    
    # Aquí agregamos un poco de depuración para ver qué devuelve la API
    print(f"Respuesta de la API: {response.text}")  # Esto imprimirá la respuesta completa para depuración
    
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

    # Verificar si los datos están disponibles
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


