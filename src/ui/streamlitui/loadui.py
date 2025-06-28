import streamlit as st
import os
from src.ui.uiconfig import UIConfig

class LoadUI:
    def __init__(self):
        self.config = UIConfig()
        self.user_controls = {}

    def load_ui(self): 

        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            st.sidebar.title("Configuration")

            self.user_controls["selected_llm"] = st.sidebar.selectbox("Select LLM", self.config.get_llm_option())
            self.user_controls["selected_usecase"] = st.sidebar.selectbox("Select Use Case", self.config.get_usecase_option())
            if self.user_controls["selected_llm"] == "Groq":
                self.user_controls["selected_groq_model"] = st.sidebar.selectbox("Select Groq Model", self.config.get_groq_model_option())
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.sidebar.text_input("API Key",type="password")
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
            
            else:
                self.user_controls["selected_groq_model"] = None
                self.user_controls["GROQ_API_KEY"] = None

        return self.user_controls