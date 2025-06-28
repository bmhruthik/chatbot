import streamlit as st
from src.ui.streamlitui.loadui import LoadUI
from src.LLMS.groqllm import GroqLLM
from src.graph.graph_builder import GraphBuilder
from src.state.state import State
from src.ui.streamlitui.display_message import DisplayResultStreamlit
def load_chat_app():
    # Load UI
    ui = LoadUI()
    user_input = ui.load_ui()


    if user_input:
        user_message = st.chat_input("Enter your message:")
        if user_message:
            try:
                if user_input["selected_llm"] != "Groq": 
                    llm = GroqLLM(user_input).get_llm()
                else:
                    llm = None
 
                if not llm:
                    st.error("Error: LLM model could not be initialized")
                    return
                
                usecase = user_input["selected_usecase"]
                if not usecase:
                    st.error("Error: Use case not selected")
                    return
                
                graph_builder = GraphBuilder(llm)
                try:
                    graph = graph_builder.setup_graph(usecase)
                    print(user_message)
                    # Display the result in the Streamlit app
                    display_result = DisplayResultStreamlit(usecase, graph, user_message)
                    display_result.display_result_on_ui()
                except Exception as e:
                    st.error(f"Error setting up graph: {e}")
                    return
 
 
                
              
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please select an LLM and a use case with API key to proceed.")