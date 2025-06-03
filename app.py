import streamlit as st
import asyncio
import os
from question_runner import run_workflow

# Configure page
st.set_page_config(
    page_title="Investment Research Assistant",
    page_icon="💼",
    layout="wide"
)

# Check for API keys
if 'OPENAI_API_KEY' not in st.secrets and not os.getenv('OPENAI_API_KEY'):
    st.error("⚠️ OpenAI API key is missing! Please add it to your Streamlit secrets or environment variables.")
    st.stop()

if 'FRED_API_KEY' not in st.secrets and not os.getenv('FRED_API_KEY'):
    st.error("⚠️ FRED API key is missing! Please add it to your Streamlit secrets or environment variables.")
    st.stop()

# Set API keys from Streamlit secrets if available
if 'OPENAI_API_KEY' in st.secrets:
    os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
if 'FRED_API_KEY' in st.secrets:
    os.environ['FRED_API_KEY'] = st.secrets['FRED_API_KEY']

# Main app
st.title("💼 Investment Research Assistant")
st.markdown("""Ask me anything about finance, investments, market analysis, or economic indicators.""")

question = st.text_area(
    "Enter your financial question:",
    placeholder="E.g., How would a planned interest rate cut affect my holdings in GOOGL?"
)

if st.button("Get Analysis", type="primary"):
    if not question.strip():
        st.warning("Please enter a valid question.")
    else:
        st.info("Analyzing... Please wait.")
        result = asyncio.run(run_workflow(question))
        st.success("Answer:")
        st.write(result)
