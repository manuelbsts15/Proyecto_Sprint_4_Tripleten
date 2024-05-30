import streamlit as st
import pandas as pd
import plotly.express as px
st.title('Proyecto_Sprint_4')
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Constriur histograma') # crear boton
st.header('Histograma')
if hist_button : #al hacer click en el boton
    #escribir mensaje
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')

    #crear un histograma
    fig = px.histogram(car_data, x = 'odometer')

    #mostrar un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width = True)

build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
st.header('Diagrama de dispersion')
hist_button = st.button('Construir diagrama de dispersion')
if hist_button: #al hacer click en el boton
    
    #escribir un mensaje
    st.write('Creacion de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')
    
    #crear un grafico de dispersion
    fig = px.scatter(car_data, x="odometer", y="price") 
    
    #mostrar un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width = True)