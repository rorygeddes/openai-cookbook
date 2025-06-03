import streamlit as st
import asyncio
from question_runner import run_workflow

st.title("💼 Investment Research Assistant")
question = st.text_area("Enter your financial question:")

if st.button("Submit"):
    if not question.strip():
        st.warning("Please enter a valid question.")
    else:
        st.info("Analyzing... Please wait.")
        result = asyncio.run(run_workflow(question))
        st.success("Answer:")
        st.write(result)
