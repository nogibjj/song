import streamlit as st
from nfl import pandas_load_nfl

dataframe = pandas_load_nfl()
st.table(dataframe.head())