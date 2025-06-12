import streamlit as st

def create_mcq_question(mcq_list):
    st.title("MCQ Generator")
    for mcq in mcq_list:
        st.write(mcq["question"])
        st.write("Answer choices:")
        mcq['selected_option'] = st.radio(
            "Select the correct answer:",
            options=mcq["options"],
            key=mcq["question"]
        )
        st.write(f"Your answer: {mcq['selected_option']}")
        st.write("---")

    if st.button("Confirm Selection"):
        save_mcqs(mcq_list)

def save_mcqs(mcq_list):
    modified_questions = []
    for mcq in mcq_list:
        modified_question = mcq["question"].replace("___", mcq['selected_option'])
        modified_questions.append(modified_question)
    save_path = "modified_questions.txt"
    with open(save_path, "w", encoding="utf-8") as file:
        file.write("\n\n".join(modified_questions))
    st.success("Modified questions saved successfully.")