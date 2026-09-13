
from rag import retrieve

query = "Why are students struggling with too much workload?"

results = retrieve(query)

context = "\n".join(results)

print("QUESTION:")
print(query)

print("\nRETRIEVED CONTEXT:")
print(context)

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

print(prompt)