import streamlit as st
import requests
import json
import pprint

def obtener_respuesta_api(texto):
    headers = {"X-API-KEY": "sk_RxYG4kgIdeL6N9KdXBD5JIHwhMpPr_FKOfIetVj2y40", "Content-Type": "application/json"}
    data = {
        "user_inputs": {
            "text_input_3": {
                "value": texto
            }
        }
    }
    response = requests.post(
        "https://api.theforgeai.com/v1/apps/64a8eeb6bd770b33fdae84fc/view/run",
        headers=headers,
        data=json.dumps(data)
    )
    return response.json()

def main():
    st.title("Chat con API de The Forge AI")

    # Inicializar la variable donde se guardará el historial de mensajes
    historial_mensajes = []

    # Bucle para mantener la conversación con el usuario
    while True:
        mensaje_usuario = st.text_input("Escribe tu mensaje:", key='input_msg')

        # Si el usuario escribe un mensaje, agregarlo al historial y obtener la respuesta de la API
        if mensaje_usuario:
            historial_mensajes.append(("Tú:", mensaje_usuario))
            respuesta = obtener_respuesta_api(mensaje_usuario)
            historial_mensajes.append(("Bot:", respuesta['response']))

        # Mostrar el historial de mensajes en la app
        if historial_mensajes:
            st.text("Historial de mensajes:")
            for remitente, mensaje in historial_mensajes:
                st.text(f"{remitente} {mensaje}")

if __name__ == "__main__":
    main()
