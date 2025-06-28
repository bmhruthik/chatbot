from src.state.state import State
from langchain_core.messages import AIMessage

class BasicChatbotNode:
    """A basic chatbot node that uses the State class to manage messages."""

    def __init__(self,model):
        self.model=model 

    def process(self,state: State) -> dict: 
        response = self.model.invoke(state["messages"])
        
        # Ensure the response is properly formatted as an AIMessage
        if not isinstance(response, AIMessage):
            response = AIMessage(content=str(response))
            
        return {"messages": [response]}