import streamlit as st
from langchain import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Initialize Streamlit app
st.title("Hugging Face Chatbot")

# Hugging Face API Key
HUGGINGFACE_API_KEY = "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"

# Hugging Face Model
model_name = "mistralai/Mistral-7B-Instruct-v0.3"

# Define the prompt template for LangChain
prompt_template = """
You are polite, helpful assistant. Respond to the users queries while holding context across messages
Human: {input}
System:
"""

# Create the LangChain prompt template
template = PromptTemplate(input_variables=["input"], template=prompt_template)

# Initialize the Hugging Face model
llm = HuggingFaceHub(repo_id=model_name, huggingfacehub_api_token=HUGGINGFACE_API_KEY)

# Chain the prompt with the model
llm_chain = LLMChain(prompt=template, llm=llm)

# Streamlit Chatbot UI
st.write("Ask me a question")
user_input = st.text_input("You: ", placeholder="Ask me a question")

if user_input:
    # Get the response from the LLM chain
    response = llm_chain.run(user_input)

    # Display the assistant's response
    st.write(f"System: {response}")