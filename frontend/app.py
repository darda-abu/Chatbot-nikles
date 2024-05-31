import streamlit as st
import requests
import json
# Define the backend API URL
# BACKEND_URL = "http://localhost:8000/chatbot/"

# def send_input_to_backend(input_text):
#     response = requests.post(BACKEND_URL, json={"input_text": input_text})
#     if response.status_code == 200:
#         return response.json()["response"]
#     else:
#         return "Error: Unable to connect to the chatbot backend."


# def main():
#     st.title("Chatbot")

#     input_text = st.text_input("Enter your message:")
#     if st.button("Send"):
#         print(input_text)
#         if input_text:
#             output_text = send_input_to_backend(input_text)
#             st.text(output_text)

# if __name__ == "__main__":
#     main()

# import streamlit as st
# from datetime import datetime

# # Function to display messages
# def display_messages(messages):
#     for msg in messages:
#         st.write(f"{msg['timestamp']} - **{msg['user']}**: {msg['message']}")

# # Initialize session state for messages if it doesn't exist
# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # Streamlit app layout
# st.title("Messenger Interface")

# # Message display area
# st.subheader("Chat")
# display_messages(st.session_state.messages)

# # Input for new message
# st.subheader("Send a message")
# with st.form(key='message_form'):
#     user = st.text_input("Your name", key='name')
#     message = st.text_area("Your message", key='message')
#     send_button = st.form_submit_button(label='Send')

#     if send_button and user and message:
#         # Add new message to session state
#         new_message = {
#             'user': user,
#             'message': message,
#             'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         }
#         st.session_state.messages.append(new_message)
#         st.experimental_rerun()  # Refresh to display the new message

# # Reset chat button
# if st.button("Reset Chat"):
#     st.session_state.messages = []
#     st.experimental_rerun()

import streamlit as st
import requests
from datetime import datetime

BACKEND_URL = "http://localhost:8000/chat"

# Function to display messages in chat bubbles
def display_messages(messages):
    for msg in messages:
        alignment = 'end' if msg['user'] == 'user' else 'start'
        st.markdown(f"""
        <div style="display: flex; justify-content: flex-{alignment};">
            <div style="border-radius: 15px; background-color: {'#DCF8C6' if msg['user'] == 'user' else '#E5E5EA'}; color:black; padding: 10px; margin: 5px; max-width: 70%;">
                <p style="margin: 0;">{msg['message']}</p>
                <p style="text-align: right; font-size: 0.7em; margin: 0;">{msg['timestamp']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Initialize session state for messages if it doesn't exist
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Streamlit app layout
st.title("Messenger Interface")

# Message display area
st.subheader("Chat")
display_messages(st.session_state.messages)

# Input for new message
st.subheader("Send a message")
with st.form(key='message_form'):
    message = st.text_area("Your message", key='message')
    send_button = st.form_submit_button(label='Send')

    if send_button and message:
        # Add user message to session state
        new_message = {
            'user': 'user',
            'message': message,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        st.session_state.messages.append(new_message)
        
        # Send message to backend
        response = requests.post(BACKEND_URL, json={'user_query': message})
        
        if response.status_code == 200:
            response_data = response.json()
            # Add response message to session state
            bot_message = {
                'user': 'bot',
                'message': response_data.get('answer', 'No response from bot'),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.messages.append(bot_message)
        else:
            # Handle error
            error_message = {
                'user': 'bot',
                'message': 'Error communicating with the backend.',
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
            }
            st.session_state.messages.append(error_message)
        
        st.rerun()  # Refresh to display the new message

# Reset chat button
if st.button("Reset Chat"):
    st.session_state.messages = []
    st.rerun()

