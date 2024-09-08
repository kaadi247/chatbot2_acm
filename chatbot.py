from langchain_core.prompts import ChatPromptTemplate # stores prompt template to give prompt to system according to syntax
from langchain_core.output_parsers import StrOutputParser #default output parser for any output
from langchain_community.llms import Ollama #allows us to use third party Ollama to access AI model

import streamlit as st # for streamlit usage
import os # provides functions for interacting with operating system
from dotenv import load_dotenv # ensures the local environment works properly with all imported libraries

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true" #configures environment variables to tell langchain to do tracing
os.environ["LANGCHAIN_API_KEY"] = "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" # langchain API key which allows us to access AI model

#Prompt Template - gives prompt to the system in appropriate syntaz

prompt = ChatPromptTemplate.from_messages   (
    [
        ("system","You are polite, helpful assistant. Respond to the users queries while holding context across messages")
        ("user","Question:{question}")
    ]
)

#streamlit code - allows us to implement streamlit with appropriate title and input box
st.title("Chatbot using mistral for acm")
input = st.text_input("Ask me a question")

#ollama mistral implementation, mistral needs to be downloaded locally from Ollama
bot = Ollama(model="mistral")
outputparser = StrOutputParser()
path = prompt|bot|outputparser

if input:
    st.write(path.invoke({"question":input}))
