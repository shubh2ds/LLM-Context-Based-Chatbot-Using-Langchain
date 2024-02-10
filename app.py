## Context based Q&A Chatbot
import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
import os

## Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hi, Let's Talk")

from dotenv import load_dotenv
load_dotenv()


chat=ChatOpenAI(temperature=0.6)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="Yor are a poet like AI assitant")
    ]

## To load OpenAI model and get respones

def get_chatmodel_response(question):

    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input=st.text_input("Input: ",key="input")
response=get_chatmodel_response(input)

submit=st.button("Ask")

## If the button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)