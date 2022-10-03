#!/usr/bin/env python
# coding: utf-8

import joblib
import streamlit as st
import pandas as pd

# In[4]:


model = joblib.load('AI_models/pungo_pred.pkl')


# In[5]:

def predict_corrosion(model, df):

    return model.predict(df)

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data

# In[7]:


def run():
    
    st.title("Predicciones para 1 pozo: Por favor, ajusta el valor de cada parametro")

    BPPD = st.slider(label = 'Barriles de petroleo por dia, BPPD', min_value = 0,
                     max_value = 2000 ,
                     value = 500,step=1)

    BAPD = st.slider(label = 'Barriles de agua por dia, BAPD', min_value = 0,
                     max_value = 5000 ,
                     value = 1000,step=1)

    BSW = st.slider(label = 'BSW %', min_value = 0,
                    max_value = 100 ,
                    value = 50,step=1)


    Caudal_gas = st.slider(label = 'Caudal de gas, MSCFD', min_value = 0,
                           max_value = 1000 ,
                           value = 100,step=1)

    Presion_cabeza = st.slider(label = 'Presion cabeza, psi', min_value = 0,
                                    max_value = 500,
                                    value = 150,step=1)

    Temperatura_cabeza = st.slider(label = 'Temperatura cabeza, F', min_value = 0,
                                   max_value = 300 ,
                                   value = 150,step=1)

    Presion_parcial_CO2 = st.slider(label = 'Presion parcial CO2, psi', min_value = 0,
                               max_value = 500,
                               value = 150,step=1)

    Sodio = st.slider(label = 'Sodio', min_value = 0,
                        max_value = 50000 ,
                        value = 1000,step=1)

    pH = st.slider(label = 'pH', min_value = 1,
                          max_value = 14 ,
                          value = 6,step=1)

    Sulfatos = st.slider(label = 'Sulfatos, ppm', min_value = 0,
                         max_value = 200,
                         value = 50,step=1)

    #Salinidad = st.slider(label = 'Salinidad, ppm', min_value = 0,max_value = 100000,value = 50000,step=1)

    Hierro = st.slider(label = 'Fe, ppm', min_value = 0,
                   max_value = 200,
                   value = 50,step=1)

    Bicarbonatos = st.slider(label = 'Bicarbonatos, ppm', min_value = 0,
                             max_value = 3000,
                             value = 500,step=1)

    #Calcio = st.slider(label = 'Calcio, ppm', min_value = 0,max_value = 5000,value = 500,step=1)

    output=""

    features = {'bapd': BAPD, 'bppd': BPPD, 'bsw': BSW,
                'mscf': Caudal_gas, 'pco2': Presion_parcial_CO2,
                'temp': Temperatura_cabeza, 'Na':Sodio,'pH':pH,
                'SO4':Sulfatos,'Fe': Hierro,
                'bicarb': Bicarbonatos, 'Press': Presion_cabeza
                 }

    features_df  = pd.DataFrame([features])

    #st.table(features_df)

    if st.button('Predecir riesgo de corrosion'):
        output = predict_corrosion(model, features_df)

        st.success(output)


if __name__ == '__main__':
    run()

