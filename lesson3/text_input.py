#!/usr/bin/env -S python -m streamlit run

import streamlit as st

st.text_input('パスワードを入力してください',
    type='password',
    max_chars=10)