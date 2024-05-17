import streamlit as st 
import pandas as pd
import openai 


@st.cache_data  
def load_json(path):
    df = pd.read_json(path)
    return df

def get_openai_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
          
            messages = [
                { "role":"system", "content": "You are a helpful assistant."},
                {"role":"user", "content": user_input }
            ]
        )
        return response.choices[0].message['content'].strip()if response.choices else "Pas de reponse du modele."
    except Exception as e:
        return f" Une erreur est survenue : {str(e)}"