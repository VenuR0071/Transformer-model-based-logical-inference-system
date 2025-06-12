import streamlit as st
from file_utils import read_file
from mcq_generator import generate_mcqs
from ui_components import create_mcq_question

def main():
    # Initialize session state for MCQ list
    if 'mcq_list' not in st.session_state:
        st.session_state['mcq_list'] = []

    uploaded_file = st.file_uploader("Upload a text file", type="txt")

    if uploaded_file is not None:
        full_text = read_file(uploaded_file)
        compression_ratio = st.slider("Compression Ratio", min_value=0.3, max_value=1.0, value=0.8, step=0.01)

        if st.button("Generate MCQs"):
            mcq_list = generate_mcqs(full_text, compression_ratio)
            st.session_state['mcq_list'] = mcq_list
            st.experimental_rerun()  # Rerun to show MCQ selection page

    # Render MCQs if generated
    if st.session_state['mcq_list']:
        create_mcq_question(st.session_state['mcq_list'])

if __name__ == "__main__":
    main()