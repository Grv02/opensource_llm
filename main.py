import os
from langchain_community.llms import Ollama
import streamlit as st
llm = Ollama(model="llama2")

# streamlit framework

st.title('Langchain demo with llama2')
input_text = st.text_input("Ask Question")

if input_text:
    st.write(llm.invoke(input_text))
