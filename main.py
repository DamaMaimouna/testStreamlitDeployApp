import streamlit as st
import json

# Set the title of the Streamlit app
with st.sidebar:

    st.title('JSON File Reader')
    # Upload a JSON file
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")

    if uploaded_file is not None:
        # Read the JSON file
        data = json.load(uploaded_file)

        # Display the JSON data
        st.json(data)
