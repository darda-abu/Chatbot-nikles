

import streamlit as st
import requests
from datetime import datetime


BACKEND_URL = "http://localhost:8000/chat"

st.html(
"""
    <style>
    .clickable {
        color: rgb(46, 154, 255);
        text-decoration: underline;
    }
    
    div[data-testid="stChatMessageContent"] {
        background-color: white;
        color: black; # Expander content color
    } 
    
    div[data-testid="stChatMessage"] {
        background-color: white;
        color: black; # Adjust this for expander header color
    }
    .st-emotion-cache-janbn0 {
        flex-direction: row-reverse;
        text-align: right;
        background-color: green;
    }
    .user-message {
        background-color: #D1E7DD;
        color: black;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
        text-align: left;
    }
    .bot-message {
        background-color: #F8D7DA;
        color: black;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
        text-align: left;
    }
    </style>
""")
# Function to display messages in chat bubbles
def display_messages(messages):
    for msg in messages:
        # alignment = 'end' if msg['user'] == 'user' else 'start'


        # st.markdown(f"""
        # <div style="display: flex; justify-content: flex-{alignment};">
        #     <div style="border-radius: 15px; background-color: {'#DCF8C6' if msg['user'] == 'user' else '#E5E5EA'}; color:black; padding: 10px; margin: 5px; max-width: 70%;">
        #         <p style="margin: 0;">{msg['message']}</p>
        #         <p style="text-align: right; font-size: 0.7em; margin: 0;">{msg['timestamp']}</p>
        #     </div>
        # </div>
        # """, unsafe_allow_html=True)
        with st.chat_message(msg['user']):
            st.markdown(msg['message'])



# Initialize session state for messages if it doesn't exist
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Streamlit app layout
st.title("Messenger Interface")

# Message display area
st.subheader("Chat Messages")
display_messages(st.session_state.messages)

# Input for new message
with st.form(key='message_form'): 
    cols = st.columns([6, 1, 2])
    with cols[0]:
        message = st.text_area("Ask Something", key='message', height=5)
    with cols[1]:
        st.write("")
        st.write("")
        send_button = st.form_submit_button(label='Send', type="primary")
    with cols[2]:
        st.write("")
        st.write("")
        reset_button = st.form_submit_button(label='Reset Chat')

    if send_button and message:
        new_message = {
            'user': 'user',
            'message': message,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        st.session_state.messages.append(new_message)
        
        response = requests.post(BACKEND_URL, json={'user_query': message})
        
        if response.status_code == 200:
            response_data = response.json()
            bot_message = {
                'user': 'assistant',
                'message': response_data.get('answer', 'No response from bot'),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.messages.append(bot_message)
        else:
            error_message = {
                'user': 'assistant',
                'message': 'Error communicating with the backend.',
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.messages.append(error_message)

        st.session_state.input_message = ""
        st.rerun()

    if reset_button:
        response = requests.post("http://localhost:8000/clear")
        if response.status_code == 200:
            st.session_state.messages = []
        else:
            st.error("Failed to clear chat history.")
        st.session_state.messages = []
        st.session_state.input_message = ""
        st.rerun()
