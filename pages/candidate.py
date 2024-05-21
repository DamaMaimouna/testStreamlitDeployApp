import streamlit as st
import pandas as pd 
import json
import utils as ul
import datetime as dt

# Site bar canva
with st.sidebar:

    st.title('FILE READER')
    # Upload a JSON file
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")

    if uploaded_file is not None:
            # Read the JSON file
            data = json.load(uploaded_file)

            # Display the JSON data
            st.json(data)

#Main canva / central
st.title('Candidate dashboard')


# creation des visuels
#creation des sliders pour interagir
# lecture/ chargement de la donnée
candidate = ul.load_json('data/dataset.json')
st.button("Rerun")
candidate['year'] = pd.to_datetime(candidate['start_date']).dt.year
candidate['month'] = pd.to_datetime(candidate['start_date']).dt.month

start_date_slider = st.slider("Selectionnez la date de debut" , min_value=candidate['month'].unique().min()\
                              , max_value = candidate['month'].unique().max(), value = candidate['month'].unique().min())
st.write("Start date:", start_date_slider)
end_date_slider = st.slider("Selectionnez la date de fin" , min_value=candidate['month'].unique().min(), \
                            max_value = candidate['month'].unique().max(), value = candidate['month'].unique().max())
st.write("end date:", end_date_slider)

def filter_df (df, start, end):
      filtered_df = df[(df['month']>= start) &( df['month'] <=end)]
      return filtered_df



filtered_candidate = filter_df( candidate, start_date_slider,end_date_slider )
st.line_chart(filtered_candidate,x='start_date', y = ['nbr_refused', 'nbr_validated'], color=[ "#ff0000" ,"#a3ffb4"]  )