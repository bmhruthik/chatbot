import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase= usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase= self.usecase
        graph = self.graph
        user_message = self.user_message
        print(user_message)
        if usecase =="Basic Chatbot": 
            initial_state = {'messages': [HumanMessage(content=user_message)]}
            for event in graph.stream(initial_state):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        # Handle the response message properly
                        if value["messages"]:
                            last_message = value["messages"][-1]
                            if hasattr(last_message, 'content'):
                                st.write(last_message.content)
                            else:
                                st.write(str(last_message))