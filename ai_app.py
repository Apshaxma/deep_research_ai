# app.py

import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import your backend logic
from main import compiled_graph, ResearchState  # Adjust according to your file structure

# Streamlit app
st.set_page_config(page_title="AI Deep Research", page_icon="🔍", layout="centered")

st.title("🔍 AI Deep Research Assistant")

# User input
user_query = st.text_input("Enter your research question:")

# Button to trigger search
if st.button("Search"):
    if user_query:
        with st.spinner('Researching... Please wait...'):
            initial_state = ResearchState(query=user_query)
            result = compiled_graph.invoke(initial_state)
            st.success("Research Completed!")

            st.subheader("📝 Final Drafted Answer:")
            st.write(result.drafted_answer)
    else:
        st.warning("Please enter a question to research!")
