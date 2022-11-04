import requests
import streamlit as st

from main_page import get_ids
from main_page import load_data

url = 'http://127.0.0.1:5000/get_transactions_by_ids/' + get_ids('pattern_4')
patern = requests.get(url)
st.header("Невалидный аккаунт")
df = load_data(patern.json(), 10000)
st.dataframe(df)
