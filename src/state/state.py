from typing_extensions import TypedDict,List
from langgraph.graph import add_messages
from typing import Annotated


class State(TypedDict): 
    """State class to hold the state of the application.""" 

    messages: Annotated[list, add_messages]


 


# if __name__ == "__main__":
#     state = State(messages=[]) 
#     state["messages"].append("Hello, World!")
#     print(state["messages"])
#     print("State is working!")