import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

titanic_link = 'https://raw.githubusercontent.com/adsoftsito/nosql/main/csv/titanic.csv'

titanic_data = pd.read_csv(titanic_link)

fig, ax = plt.subplots()

ax.hist(titanic_data.fare)

st.header("Histograma del Titanic")

st.pyplot(fig)
st.markdown("___")
