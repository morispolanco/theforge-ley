import streamlit as st
import requests
import json

# Set up the chatbot
st.title("Streamlit Chatbot")

# Define the API endpoint and headers
endpoint = "https://api.theforgeai.com/v1/apps/64a8eeb6bd770b33fdae84fc/view"
headers = {
    "X-API-KEY": "sk_RxYG4kgIdeL6N9KdXBD5JIHwhMpPr_FKOfIetVj2y40",
    # Add Content-Type header for sending JSON data
    "Content-Type": "application/json"
}

# Define the initial state of the chatbot
state = {}

# Add a text input field to the app
text_input = st.empty()

# Add placeholder for bot response
bot_response = st.empty()

# Add a button to send the message to the API
button_send = st.button("Send Message")

def send_message():
    text_input_value = text_input.text_input("Enter your message here", "")
    payload = json.dumps({"user_inputs": {"text_input_3": {"value": text_input_value}}})
    response = requests.post(
        endpoint,
        headers=headers,
        data=payload
    )
    bot_response.text("Chatbot: " + response.json()["message"])

# On button click
if button_send:
    send_message()
