#!/usr/bin/env -S python -m streamlit run

import streamlit as st

narrow, wide = st.columns([1, 4])
narrow.text_input('パスワードを入力してください',
    type='password',
    max_chars=10)

st.markdown('''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Duis ut purus sit amet tortor tristique lobortis. Pellentesque hendrerit,
    mi sed accumsan malesuada, mi dui fermentum ante, non gravida ex nibh eu dui.
    Sed scelerisque nulla in pharetra commodo. Ut molestie ligula at lectus pharetra
    posuere. Integer dui nisl, maximus non ante at, sagittis ornare turpis.''')
