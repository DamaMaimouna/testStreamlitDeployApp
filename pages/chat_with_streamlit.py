import streamlit as st
import utils  as u
import openai



st.title("Votre assistant Chatbot ")
st.image('images/chatbot.jpeg')
user_input = st.text_input("Que puis-je pour vous aujourd'hui ?")
if st.button("Entrer"):
    chatbot_response = u.get_openai_response(user_input) if user_input else st.write("Veuillez poser votre question ? ")
    st.write(f"Chatbot: {chatbot_response}")