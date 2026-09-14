import os

from dotenv import load_dotenv
from agents import (
    Agent,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)

from src.product_tools import search_product_knowledge


load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

model = OpenAIChatCompletionsModel(
    model="deepseek-v4-flash",
    openai_client=client,
)

set_tracing_disabled(True)

agent = Agent(
    name="Product Analyst",
    instructions="""
    You are an AI product analyst.

    When a question requires evidence from product feedback
    or internal product knowledge, use the
    search_product_knowledge tool.

    Base evidence-related claims on retrieved information.

    If the knowledge base does not contain enough evidence,
    clearly say so.

    For questions that do not require product knowledge,
    answer directly without using the retrieval tool.
    """,
    model=model,
    tools=[
        search_product_knowledge,
    ],
)
