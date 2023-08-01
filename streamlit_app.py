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

# Input del usuario
user_input = st.text_input("Escribe tu mensaje:")

# Cuando el usuario presiona el botón "Enviar", se envía la solicitud a la API
if st.button("Enviar"):
    if user_input:
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
            st.write("Respuesta del bot:", response_data.get('outputs', {}).get('text_output_1', {}).get('value', ''))
        else:
            st.write("Ha ocurrido un error al procesar la solicitud.")
    else:
        st.write("Por favor, escribe un mensaje.")
