import os

from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain.messages import (
    SystemMessage,
    HumanMessage,
)

load_dotenv()

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
)

from langchain.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

messages = [
    SystemMessage(
        "You are an AI product analyst."
    ),

    HumanMessage(
        "Users complain that study plans contain too many tasks."
    ),

    AIMessage(
        "The main issue appears to be excessive daily workload."
    ),

    HumanMessage(
        "What should we improve first?"
    ),
]

response = model.invoke(messages)

print(response.content)