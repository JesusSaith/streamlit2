import streamlit as st
import pandas as pd
import codecs


st.sidebar.image("222.jpeg")

st.title ('NETFLIX BY SAITHCOND')

@st.cache
def load_data(nrows):
    doc=codecs.open('movies.csv', 'rU', 'latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

data_load_state = st.text('Loading..')
data = load_data(500)
data_load_state.text('DONE')

st.dataframe(data)

sidebar = st.sidebar
sidebar.title("NETFLIX")

agree = sidebar.checkbox("Mostar tods los filmes")
if agree:
    st.dataframe(data)

def load_data_byname(name):
    doc=codecs.open('movies.csv', 'rU', 'latin1')
    data = pd.read_csv(doc)
    filtered_data_byname= data[data["name"].str.contains(name)]
    return filtered_data_byname

byname = sidebar.text_input("Nombre:")
if(byname):
    filterbyname = load_data_byname(byname)
    count_row=filterbyname.shape[0]

    st.dataframe(filterbyname)

byname = sidebar.button('Mostrar Filmes')
print(byname)
if(byname):
    filterbyname = load_data_byname(byname)

    st.dataframe(filterbyname)

def load_data_director(director):
    doc=codecs.open('movies.csv', 'rU', 'latin1')
    data = pd.read_csv(doc)
    filtered_data_bydirector = data[data["director"]== director]
    return filtered_data_bydirector

data = select_direc = sidebar.selectbox("Select Director",data['director'].unique())
btnFilterbyDirec = sidebar.button('Filtrar director')

if(btnFilterbyDirec):
    filterbydirec=load_data_director(select_direc)
    count_row = filterbydirec.shape[0]

    st.dataframe(filterbydirec)











