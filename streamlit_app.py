import streamlit as st
import json
import requests

# Define the API endpoint, headers and the data
api_url = "https://api.theforgeai.com/v1/apps/64a8eeb6bd770b33fdae84fc/view/run"
headers = {
    "X-API-KEY": "sk_RxYG4kgIdeL6N9KdXBD5JIHwhMpPr_FKOfIetVj2y40",
    "Content-Type": "application/json"
}

def send_message(message):
    data = {
      "user_inputs": {
        "text_input_3": {
          "value": message
        }
      }
    }

    response = requests.post(
        api_url,
        headers=headers,
        data=json.dumps(data)
    )

    return response.json()

# Streamlit app
st.title('Streamlit Chatbot')

user_message = st.text_input("Enter your message")
if st.button("Send"):
    response = send_message(user_message)
    st.write(response) # Display the response received from the API
