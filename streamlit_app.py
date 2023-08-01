import streamlit as st
import streamlit_chat as sc


# Set up the chatbot
st.title("The Forge AI Chatbot")
chat = Chat()

# Define the API endpoint and headers
endpoint = "https://api.theforgeai.com/v1/apps/64a8eeb6bd770b33fdae84fc/view"
headers = {
    "X-API-KEY": "sk_RxYG4kgIdeL6N9KdXBD5JIHwhMpPr_FKOfIetVj2y40",
    # Add Content-Type header for sending JSON data
    "Content-Type": "application/json"
}

# Define the initial state of the chatbot
state = {}

# Function to handle incoming messages from the user
def handle_message(message):
    # Parse the message as JSON
    try:
        message_dict = json.loads(message)
    except ValueError:
        return None

    # Check if the message contains text input
    if "text_input_3" in message_dict:
        # Extract the text input value
        text_input = message_dict["text_input_3"]["value"]

        # Make a request to the API with the extracted text input
        response = requests.post(
            endpoint,
            headers=headers,
            data=json.dumps({"user_inputs": message_dict})
        )

        # Print the response from the API
        print(response.json())

# Create the Streamlit app
app = st.App(
    title="The Forge AI Chatbot",
    style={"background-color": "#f2f2f2", "font-family": "Arial, sans-serif"},
    layout="wide"
)

# Add a text input field to the app
text_input = st.text_input("Enter your message here", "")

# Add a button to send the message to the API
button = st.button("Send Message")

# Define the callback function for when the button is clicked
@button.click
def send_message():
    # Get the current text input value
    text_input_value = text_input.value

    # Build the JSON payload for the API request
    payload = json.dumps({"user_inputs": {"text_input_3": {"value": text_input_value}}})

    # Make the API request
    response = requests.post(
        endpoint,
        headers=headers,
        data=payload
    )

    # Print the response from the API
    print(response.json())

# Run the app
app.run()
