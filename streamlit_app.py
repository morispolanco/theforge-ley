import streamlit as st
from streamlit_chat import Chat as sc
import json, requests

# Set up the chatbot
st.title("The Forge AI Chatbot")
chat = sc()

# Define the API endpoint and headers
endpoint = "https://api.theforgeai.com/v1/apps/64a8eeb6bd770b33fdae84fc/view"
headers = {
    "X-API-KEY": "sk_RxYG4kgIdeL6N9KdXBD5JIHwhMpPr_FKOfIetVj2y40",
    # Add Content-Type header for sending JSON data
    "Content-Type": "application/json"
}

# Define the initial state of the chatbot
state = {}

text_input = st.text_input("Enter your message here", "")
button = st.button("Send Message")

def send_message():
    text_input_value = text_input.value
    payload = json.dumps({"user_inputs": {"text_input_3": {"value": text_input_value}}})
    response = requests.post(
        endpoint,
        headers=headers,
        data=payload
    )
    print(response.json())

if button:
    send_message()
