import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

st.markdown("# Informacion")

st.write("""
        ### Bienvenido al demo de ASTRO: la herramienta digital para la gestión del tratamiento químico en la industria petrolera
        """)

with st.expander('Para que sirve ASTRO❓'):
    
    st.markdown("""
    ### ASTRO genera los siguientes beneficios:
    - Reduce los costos asociados al tratamiento químico y las pérdidas de producción por eventos de corrosión e incrustaciones
    - Identifica los pozos críticos en tus operaciones con nuestra metodología para priorizar y optimizar el tratamiento químico
    - Disminuye el tiempo para el procesamiento de datos, genera reportes automáticos y libera tiempo valioso para optimizar la rentabilidad y seguridad de las operaciones""")

    st.write("")

    st.markdown("ASTRO es una solucion modular que se adapta a tus necesidades y genera valor en tus operaciones. ASTRO incluye los siguientes modulos:")
    
    image1 = Image.open('Resources/modulos astro.png')
    st.image(image1)
      
    st.markdown('En esta demostracion, te presentamos el Modulo de Inteligencia Artificial, que permite calcular la velocidad de corrosion de los pozos petroleros.')
                 
with st.expander("Para que sirve el modulo de inteligencia artificial de ASTRO❓"):

    st.markdown("""
    ### El modulo de inteligencia artificial de ASTRO te sirve para:
    - Predecir la velocidad de corrosión de los pozos de petróleo en función de varios parametros de produccion y laboratorio. 
    - Generar ahorros por optimizacion de los quimicos e incremento de la produccion de los pozos debido a un tratamiento quimico adecuado. 
    """)

with st.expander("Instrucciones"):

    st.markdown("""
    ### Por favor, sigue estas instrucciones para utilizar el modulo de calculos:
    - Si deseas obtener las predicciones para un pozo, selecciona la hoja "Calculos 1 pozo". Luego, ajusta el valor de cada parametro y presiona el boton Calcular para ver los resultados.
    - Si deseas obtener las predicciones para multiples pozos, selecciona la hoja "Calculos varios pozos". Carga el archivo CSV con los parametros de produccion y laboratorio de los pozos. Despues, da click en los botones que se indican para obtener los resultados. 
    """)
