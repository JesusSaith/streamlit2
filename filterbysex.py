import streamlit as st
import pandas as pd

st.title('Streamlit - Filter by sex')

DATA_URL = ('https://firebasestorage.googleapis.com/v0/b/streamlit-46e89.appspot.com/o/csv%2Fjesus%2Fdataset.csv?alt=media&token=dc71bc31-949e-4588-9998-4598d6c97b32')

def load_data():
    data = pd.read_csv(DATA_URL)
    return data

def load_data_bysex(sex):
    data = pd.read_csv(DATA_URL)
    filtered_data_bysex = data[data['sex']== sex]

    return filtered_data_bysex

data = load_data()
selected_sex = st.selectbox("Select sex",data['sex'].unique())
btnFilterbySex = st.button('Filter by sex')

if(btnFilterbySex):
    filterbysex=load_data_bysex(selected_sex)
    count_row = filterbysex.shape[0]
    st.write(f"Total Items: {count_row}")

    st.dataframe(filterbysex)