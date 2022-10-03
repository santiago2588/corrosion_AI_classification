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


model = load_model('AI_models/corrosion_regressor_random_mpy')


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

    CO2_gas = st.slider(label = 'Fraccion CO2 gas', min_value = 0.0,
                        max_value = 1.0 ,
                        value = 0.5,step=0.1)

    Salinidad = st.slider(label = 'Salinidad, ppm', min_value = 0,
                          max_value = 100000 ,
                          value = 50000,step=100)

    sulfatos = st.slider(label = 'Sulfatos, ppm', min_value = 0,
                         max_value = 200,
                         value = 50,step=1)

    Fe = st.slider(label = 'Fe, ppm', min_value = 0,
                   max_value = 200,
                   value = 50,step=1)

    Bicarbonatos = st.slider(label = 'Bicarbonatos, ppm', min_value = 0,
                             max_value = 3000,
                             value = 500,step=1)

    output=""

    features = {'bppd': BPPD, 'bapd': BAPD, 'bsw': BSW,
                'mscf': Caudal_gas, 'pres': Presion_cabeza,
                'temp': Temperatura_cabeza, 'Cl': Salinidad,
                'co2_frac': CO2_gas, 'bicarb': Bicarbonatos,
                'Fe': Fe, 'SO4':sulfatos}

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

