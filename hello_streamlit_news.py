import streamlit as st
from news import pandas_load_news

dataframe = pandas_load_news()
st.table(dataframe.head())