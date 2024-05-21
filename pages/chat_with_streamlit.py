import streamlit as st
 


st.title("Votre assistant Chatbot ")
st.image('images/chatbot.jpeg')
user_input = st.text_input("Que puis-je pour vous aujourd'hui ?")
if st.button("Entrer"):
    chatbot_response = f"Vous avez écris : {user_input}"
    st.write(f"Chatbot: {chatbot_response}")