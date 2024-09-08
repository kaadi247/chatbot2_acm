import streamlit as st # allows us to use streamlit
from langchain import HuggingFaceHub # allows us to use huggingface and call api mode
from langchain.chains import LLMChain # allows us to use LLMChain for output
from langchain.prompts import PromptTemplate # allows us to give prompt to system according to syntax

st.title("Hugging Face Chatbot") # title on streamlit

HUGGINGFACE_API_KEY = "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" #api key from huggingface

model_name = "mistralai/Mistral-7B-Instruct-v0.3" #ai model used

#gives prompt to system
prompt_template = """ 
You are polite, helpful assistant. Respond to the users queries while holding context across messages
Human: {input}
System:
"""

template = PromptTemplate(input_variables=["input"], template=prompt_template) #creates final prompt template 

llm = HuggingFaceHub(repo_id=model_name, huggingfacehub_api_token=HUGGINGFACE_API_KEY) #creates llm using HuggingFaceHub

llm_chain = LLMChain(prompt=template, llm=llm) # creates llm_chain using LLMChain to produce output

st.write("Ask me a question") # message displayed on streamlit
user_input = st.text_input("You: ", placeholder="Ask me a question") #message displayed on searchbar and takes input

if user_input: # runs the code and gets response using the AI model
    response = llm_chain.run(user_input)
    st.write(f"System: {response}")
