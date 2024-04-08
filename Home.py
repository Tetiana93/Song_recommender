# app.py
import streamlit as st
from helpers import song_recom

st.set_page_config(page_icon="🎶", layout="wide")
st.title("Song recommender")
st.write("---")

col1, col2 = st.columns([.5, .5])
client_id = col1.text_input('Client ID')
client_secret = col2.text_input('Client Secret')

st.write("---")

song = st.text_input('Song - Artist')

st.write("---")

if st.button('Recommend'):
    if client_id and client_secret:
        song_recommended = song_recom(client_id, client_secret, song)
        st.header(song_recommended, divider='rainbow')
    else:
        st.warning("Please provide Client ID and Client Secret")
