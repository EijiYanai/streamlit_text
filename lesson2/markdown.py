import streamlit as st

html = '<p style = "color: dodgerblue;">HTMLテキスト</p>'
st.markdown(html)
st.markdown(html, unsafe_allow_html=True)
st.html(html)
