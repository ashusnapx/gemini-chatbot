import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# load all environmentt variables
load_dotenv()

# configure google model
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
model = genai.GenerativeModel('gemini-pro')

# remember the context of chat
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# heading of page
st.title('Chat with Genie+')

# define role of gemini
def role_to_streamlit(role):
    if role == 'model':
        return 'assistant'
    else:
        return role

for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# start the chat
if prompt := st.chat_input('Mujhe sab aata hai, aap btaiye aapko kya jaan na hai?'):
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
	    st.markdown(response.text)