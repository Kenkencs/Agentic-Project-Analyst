"""Entry point for the Agentic Project Analyst project."""
import os

from dotenv import load_dotenv
from product_tools import search_feedback 
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)

load_dotenv()

deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

client = AsyncOpenAI(
    api_key=deepseek_api_key,
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

    When the user asks about user complaints or user feedback,
    use search_feedback to retrieve evidence.

    After receiving the feedback from the tool,
    analyze the returned evidence and give the user a final answer.

    Do not repeatedly call the same tool unless additional information
    is genuinely required.
    """,
    model=model,
    tools=[search_feedback],
)

result = Runner.run_sync(
    agent,
    "What are students complaining about regarding tasks?",
)

print(result.final_output)


def main() -> None:
    """Run the project analyst."""
    print("Agentic Project Analyst is ready.")


if __name__ == "__main__":
    main()
