import streamlit as st
 

#st.header("IMC ")
#st.subheader("IMC ")
st.image('images/imc1.jpeg', use_column_width = True )
st.title ("calculateur de l'IMC")
#Initialiser l'imc 
imc = None
# Entrer le poids en kgs
weight = st.number_input("Entrer votre poids (en kgs)")

# Entrer la taille
# radio button to choose height format
status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))
 
# compare status value
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')
     
    try:
        imc = weight / ((height/100)**2)
    except:
        st.text("Entrez votre taille")
         
elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')
     
    try:
        imc = weight / (height ** 2)
    except:
        st.text("Entrez votre taille")
         
else:
    # take height input in feet
    height = st.number_input('Feet')
     
    # 1 meter = 3.28
    try:
        imc = weight / (((height/3.28))**2)
    except:
        st.text("Entrez votre taille")
 
# check if the button is pressed or not
if(st.button('Calculate imc')):
    if (imc is not None) :
        # print the imc INDEX
        st.text("Votre IMC est  {}.".format(imc))
        
        # give the interpretation of imc index
        if(imc < 16):
            st.error("Vous etes extremenent mince")
        elif(imc >= 16 and imc < 18.5):
            st.warning("Vous etes mince")
        elif(imc >= 18.5 and imc < 25):
            st.success("Votre IMC est correcte")       
        elif(imc >= 25 and imc < 30):
            st.warning("Vous etes en surpois")
        elif(imc >= 30):
            st.error("Vous etes obese")
    else:
        st.write("Veuillez d'abord renseigner votre poids et votre taille")