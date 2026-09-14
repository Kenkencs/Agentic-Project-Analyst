"""Manual RAG prompt demo for inspecting retrieved context."""

from src.rag import retrieve


QUERY = "Why are students struggling with too much workload?"


def build_prompt(query: str, context: str) -> str:
    return f"""
You are a product analyst.

Answer the question using only the retrieved context below.

Retrieved context:
{context}

Question:
{query}

If the retrieved context does not contain enough evidence,
say that there is not enough information.
"""


def main() -> None:
    results = retrieve(QUERY)
    context = "\n".join(results)

    print("QUESTION:")
    print(QUERY)

    print("\nRETRIEVED CONTEXT:")
    print(context)

    print(build_prompt(QUERY, context))


if __name__ == "__main__":
    main()
