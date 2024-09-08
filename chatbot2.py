import streamlit as st
from langchain import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

st.title("Hugging Face Chatbot")

HUGGINGFACE_API_KEY = "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"

model_name = "mistralai/Mistral-7B-Instruct-v0.3"

prompt_template = """
You are polite, helpful assistant. Respond to the users queries while holding context across messages
Human: {input}
System:
"""

template = PromptTemplate(input_variables=["input"], template=prompt_template)

llm = HuggingFaceHub(repo_id=model_name, huggingfacehub_api_token=HUGGINGFACE_API_KEY)

llm_chain = LLMChain(prompt=template, llm=llm)

st.write("Ask me a question")
user_input = st.text_input("You: ", placeholder="Ask me a question")

if user_input:
    response = llm_chain.run(user_input)
    st.write(f"System: {response}")
