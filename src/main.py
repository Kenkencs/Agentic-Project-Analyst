"""Entry point for the Agentic Project Analyst project."""
import os

from dotenv import load_dotenv
from openai import OpenAI

from rag import retrieve

load_dotenv()

deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

rag_client = OpenAI(
    api_key=deepseek_api_key,
    base_url="https://api.deepseek.com",
)

query = "Why are students struggling with too much workload?"

results = retrieve(query)

context = "\n".join(
    f"- {result}"
    for result in results
)

prompt = f"""
You are a product analyst.

Answer the question using only the retrieved context below.

Retrieved context:
{context}

Question:
{query}

If the retrieved context does not contain enough evidence,
say that there is not enough information.
"""

response = rag_client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
)

answer = response.choices[0].message.content

print("RETRIEVED CONTEXT:")
print(context)

print("\nANSWER:")
print(answer)