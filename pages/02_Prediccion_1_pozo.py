#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pycaret.regression import load_model, predict_model

# In[2]:


import streamlit as st


# In[3]:


import pandas as pd
import numpy as np


# In[4]:


model = load_model('AI_models/corrosion_regressor_less_data')


# In[5]:


def predict_corrosion(model, df):
    predictions_data = predict_model(estimator = model, data = df)
    predictions=predictions_data['Label'][0]
    return predictions

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

    BPPD = st.slider(label = 'Barrels of oil per day (BOPD)', min_value = 0,
                      max_value = 2000 ,
                      value = 500,step=1)

    BAPD = st.slider(label = 'Barrels of water per day (BWPD)', min_value = 0,
                      max_value = 5000 ,
                      value = 1000,step=1)

    Caudal_gas = st.slider(label = 'Gas flow rate (MSCFD)', min_value = 0,
                      max_value = 1000 ,
                      value = 100,step=1)

    Presion_cabeza = st.slider(label = 'Head pressure (psi)', min_value = 0,
                      max_value = 500,
                      value = 150,step=1)

    Temperatura_cabeza = st.slider(label = 'Head temperature (F)', min_value = 0,
                      max_value = 300 ,
                      value = 150,step=1)

    Salinidad = st.slider(label = 'Salinity (ppm)', min_value = 0,
                      max_value = 100000 ,
                      value = 50000,step=100)

    CO2_gas = st.slider(label = 'CO2 content in gas (%)', min_value = 0,
                      max_value = 100 ,
                      value = 20,step=1)

    Bicarbonatos = st.slider(label = 'Bicarbonates (ppm)', min_value = 0,
                      max_value = 3000,
                      value = 500,step=1)

    Dosis_IC = st.slider(label = 'Corrosion inhibitor dosis (ppm)', min_value = 0,
                      max_value = 300,
                      value = 100,step=1)

    Fe = st.slider(label = 'Fe (ppm)', min_value = 0,
                      max_value = 200,
                      value = 50,step=1)

    output=""

    features = {'BPPD': BPPD, 'BAPD': BAPD,
        'Caudal_gas_MSCFD': Caudal_gas, 'Presion_cabeza_psi': Presion_cabeza,
        'Temperatura_cabeza_F': Temperatura_cabeza, 'Salinidad_ppm': Salinidad,
        'CO2_gas': CO2_gas, 'bicarbonatos_ppm': Bicarbonatos,
        'dosis_IC_ppm': Dosis_IC, 'Fe_ppm': Fe}

    features_df  = pd.DataFrame([features])

    #st.table(features_df)

    if st.button('Predecir velocidad de corrosion'):
        output = predict_corrosion(model, features_df)

        output1=str("%.2f" % output) + ' mpy'

        st.success('Basado en los datos que ingresaste, la velocidad de corrosion es {}'.format(output1))

        if output < 1:
            st.success("Riesgo de corrosion: Bajo")
        if output>=1 and output<5:
            st.success("Riesgo de corrosion: Moderado")
        if output>=5 and output<10:
            st.success("Riesgo de corrosion: Alto")
        if output >= 10:
            st.success("Riesgo de corrosion: Severo")

if __name__ == '__main__':
    run()

