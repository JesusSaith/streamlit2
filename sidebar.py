import streamlit as st

st.title("Mi primer App con Sidebar")

sidebar = st.sidebar
sidebar.title("Esta la barra lateral")
sidebar.write("Elementos de Entrada")

st.header("Informacion Sobre el conjunto de datos")
st.header("Descripcion de los datos")

st.write("""

este es un simple ejemplo de una app

Esta app predice datos


""")