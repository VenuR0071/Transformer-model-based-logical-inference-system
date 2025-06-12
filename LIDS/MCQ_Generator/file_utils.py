import streamlit as st
import os

def read_file(file):
    file_extension = os.path.splitext(file.name)[1]
    if file_extension == ".txt":
        text = file.read().decode("utf-8")
        return text
    else:
        st.error("Please upload a .txt file.")
        return None