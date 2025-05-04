import streamlit as st
import pandas as pd
import plotly.express as px

#Encabezado de la aplicación
st.header("Análisis de vehículos: condiciones, precios y años de fabricación")

#Leer datos
df = pd.read_csv("Data/vehicles_us.csv")

# Mostrar una vista previa del dataset
st.write("Vista previa del dataset:")
st.dataframe(df.head())

#Crear el histograma condition vs. model_year
hist_button =st.button("Construir histograma: condition vs. model_year")
if hist_button:
    st.write("Creación de un histograma para la distribución de condition vs model_year")
    if "condition" in df.columns and "model_year" in df.columns:
        fig =px.histogram(df, x="model_year", color="condition", title="Distribucion de condition vs. model_year")
        st.plotly_chart(fig, use_container_width=True)

#Crear grafico de dispersion : price vs. model_year
disp_button=st.button("Construir gráfico de dispersión para comparar price vs. model_year")
if disp_button:
    st.write("Creación de un gráfico de dispersión para comparar price vs. model_year")
    if "price" in df.columns and "model_year" in df.columns:
        fig =px.scatter(df, x="model_year", y="price", title ="Comparación entre price vs model_year")
        st.plotly_chart(fig, use_container_width=True)
