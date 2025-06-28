import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,user_controls):
        self.user_controls = user_controls 

    def get_llm(self):
        try:
            if self.user_controls["selected_llm"] == "Groq":
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
                    return None
                if not self.user_controls["selected_groq_model"]:
                    st.warning("⚠️ Please select a Groq model to proceed.")
                    return None
                else:
                    groq_api_key = self.user_controls["GROQ_API_KEY"]
                    model_name = self.user_controls["selected_groq_model"]
                    llm = ChatGroq(model=model_name, api_key=groq_api_key)
                    return llm
        except Exception as e:
            st.error(f"Error occurred while getting LLM: {e}")
            return None
        return None