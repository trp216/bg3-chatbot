import streamlit as st
import requests
from streamlit_chat import message
import requests

API_URL = "http://127.0.0.1:5000/chat"

# Custom CSS
st.markdown("""
<style>
.main {
  background-color: black;
  display: flex;
  flex-direction: column-reverse; /* Reverse the order of elements */
  height: 100vh; /* Set full viewport height */
}

.chat-history {
  flex: 1; /* Allocate remaining space to chat history */
  overflow-y: scroll; /* Enable scrolling for long chat history */
  color: white; /* Adjust text color for better visibility */
  padding: 10px;
}

.user-message, .bot-message {
  padding: 10px;
  border-radius: 10px;
  margin: 5px 0;
}

.user-message {
  background-color: #4CAF50;
  color: white;
  text-align: right;
  margin-left: auto;
}

.bot-message {
  background-color: #555;
  color: white;
  text-align: left;
  margin-right: auto;
}

.chat-input {
  display: flex;
  justify-content: space-between; /* Align input and button to sides */
  align-items: center; /* Center align items vertically */
  margin-top: auto; /* Position at bottom */
  padding: 10px;
  background-color: black;
}

.stTextInput > div > div > input {
  background-color: black;
  border-radius: 10px;
  padding: 10px;
  color: white; /* Adjust text color for better visibility */
  flex: 1; /* Take up remaining space */
  margin-right: 10px; /* Space between input and button */
}

.stButton > button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  border-radius: 10px;
  cursor: pointer;
}

.stButton > button:hover {
  background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display chat header
st.title("Chatbox IA")

# Chat logic
def get_response(user_input):
    response = requests.post(API_URL, json={"user_input": user_input}).json()
    return response['response'] if response else None

def display_chat():
    # Chat history container
    with st.container():
        st.markdown('<div class="chat-history">', unsafe_allow_html=True)
        for chat in st.session_state['chat_history']:
            user, message = chat["user"], chat["message"]
            if user == "user":
                st.markdown(f'<div class="user-message"><strong>{user}:</strong> {message}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bot-message"><strong>{user}:</strong> {message}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Chat input container (placed at bottom)
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input("", key="user_input", placeholder="Type your message here...")
        submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            st.session_state['chat_history'].append({"user": "user", "message": user_input})
            response = get_response(user_input)
            if response:
                st.session_state['chat_history'].append({"user": "Minthara", "message": response})
            st.experimental_rerun()

# Display chat
display_chat()
