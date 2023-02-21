import streamlit as st
import pandas as pd

st.title('Streamlit - Search Range')
DATA_URL=('https://firebasestorage.googleapis.com/v0/b/streamlit-46e89.appspot.com/o/csv%2Fjesus%2Fdataset.csv?alt=media&token=dc71bc31-949e-4588-9998-4598d6c97b32')

def load_data_byrange(startid, endid):
    data=pd.read_csv(DATA_URL)
    filtered_data_byrange = data[(data['index']>= startid) & (data['index']<= endid)]

    return filtered_data_byrange

startid = st.text_input('Start Index')
endid = st.text_input('End Index')
btnRange = st.button ('Search by range')

if(btnRange):
    filterbyrange=load_data_byrange(int(startid), int(endid))
    count_row=filterbyrange.shape[0]
    st.write(f"Total items:{count_row}")

    st.dataframe(filterbyrange)