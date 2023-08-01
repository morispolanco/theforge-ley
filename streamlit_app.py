import streamlit as st
import requests
import json

# Configura tu API key
headers = {
    "X-API-KEY": "sk_RxYG4kgIdeL6N9KdXBD5JIHwhMpPr_FKOfIetVj2y40",
    "Content-Type":"application/json"
}

# URL base de la API
base_url = "https://api.theforgeai.com/v1/apps/64a8eeb6bd770b33fdae84fc/view"

# Configuración de la aplicación Streamlit
st.title("Chatbot basado en TheForgeAI")

# Creación de una lista para almacenar los mensajes del chat
chat_history = []

# Input del usuario
user_input = st.text_input("Escribe tu mensaje:")

# Cuando el usuario presiona el botón "Enviar", se envía la solicitud a la API
if st.button("Enviar"):
    if user_input:
        # Agrega el mensaje del usuario al historial del chat
        chat_history.append({"user": user_input})

        data = {
            "user_inputs": {
                "text_input_3": {
                    "value": user_input
                }
            }
        }

        response = requests.post(
            f"{base_url}/run",
            headers=headers,
            data=json.dumps(data)
        )

        if response.status_code == 200:
            response_data = response.json()
            bot_response = response_data.get('user_outputs', {}).get('text_output_5', {}).get('value', '')
            
            # Agrega la respuesta del bot al historial del chat
            chat_history.append({"bot": bot_response})
        else:
            st.write("Ha ocurrido un error al procesar la solicitud.")
    else:
        st.write("Por favor, escribe un mensaje.")

# Muestra el historial del chat
for chat in chat_history:
    if "user" in chat:
        st.write("Usuario: ", chat["user"])
    else:
        st.write("Bot: ", chat["bot"])
