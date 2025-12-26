#!/usr/bin/env -S python -m streamlit run

from acceptlang import parse_accept_lang_header
import streamlit as st

_MESSAGES = {
    'ja': 'Streamlit にようこそ',
    'en': 'Welcome to Streamlit',
    'es': 'Bienvenido a Streamlit',
    'cn': '欢迎来到 Streamlit',
    'unknown': 'tlhInganpu'
}

def find_language(al):
    for lang in al:
        if lang.name in _MESSAGES:
            return lang.name

    return 'unknown'


lang = getattr(st.query_params, 'lang', None)
if lang not in _MESSAGES.keys():
    al_value = st.context.headers['accept-language']
    al_parsed = parse_accept_lang_header(al_value)
    lang = find_language(al_parsed)

st.markdown(f'## {_MESSAGES[lang]} :green[{lang}]')

st.write(st.query_params)
st.write(st.context.headers)
