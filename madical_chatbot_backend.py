from langgraph.graph import StateGraph , START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_community.chat_models import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv()

repo_id = "GanjinZero/biollm-chat"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.3,
    max_new_tokens=512
)

class ChatState(TypedDict):
  messages: Annotated[list[BaseMessage],add_messages]
def chat_node(state: ChatState):
  messages = state["messages"]
  response = llm.invoke(messages)
  return{"messages":[response]}

Checkpointer = InMemorySaver()

graph = StateGraph(ChatState)

graph.add_node("chat_node",chat_node)

graph.add_edge(START,"chat_node")

graph.add_edge("chat_node",END)

chatbot = graph.compile(checkpointer=Checkpointer)