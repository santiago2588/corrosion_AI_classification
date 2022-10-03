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

    st.title("Predicciones para varios pozos: por favor, carga el archivo CSV con los parametros de los pozos")

    file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

    if file_upload is not None:
        data = pd.read_csv(file_upload)
        predictions = predict_model(estimator=model,data=data)
        predictions=predictions.rename({'Label':'Corrosion_rate_mpy'},axis='columns')
        st.write(predictions)

        def convert_df(df):
            return df.to_csv().encode('utf-8')

        csv = convert_df(predictions)

        st.download_button("📥Press to Download",csv,"file.csv","text/csv",key='download-csv')

# In[8]:

if __name__ == '__main__':
    run()

