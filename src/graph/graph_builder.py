from langgraph.graph import StateGraph
from src.state.state import State
from langgraph.graph import START, END
from src.nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graphbuilder=StateGraph(State)

    def build_basic_chatbot_graph(self):

        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        self.graphbuilder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graphbuilder.add_edge(START,"chatbot")
        self.graphbuilder.add_edge("chatbot",END)

    def setup_graph(self,usecase:str):
        if usecase=="Basic Chatbot":
            self.build_basic_chatbot_graph()

        return self.graphbuilder.compile()