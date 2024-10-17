api_key='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'

import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceHub

# Set up Hugging Face API token
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = api_key

# Initialize Hugging Face model
model_id = "gpt2"  # You can change this to a more suitable model
llm = HuggingFaceHub(repo_id=model_id, model_kwargs={"temperature": 0.7, "max_length": 64})

# Create a prompt template
template = """Suggest a creative and unique name for a web design agency based on the following keywords:

Keywords: {keywords}

Agency Name:"""

prompt = PromptTemplate(template=template, input_variables=["keywords"])

# Create the LLMChain
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Streamlit UI
st.title("Web Design Agency Name Generator")

keywords = st.text_input("Enter keywords for your web design agency (comma-separated):")

if st.button("Generate Name"):
    if keywords:
        result = llm_chain.run(keywords)
        st.success(f"Suggested Agency Name: {result.strip()}")
    else:
        st.warning("Please enter some keywords.")

st.markdown("---")
st.markdown("Powered by Langchain and Hugging Face")