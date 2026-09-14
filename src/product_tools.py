from agents import function_tool

from src.rag import retrieve


@function_tool
def search_feedback(query: str) -> str:
    """
    Retrieve user feedback relevant to a product topic.

    Args:
        query: The product topic or problem to investigate.
    """

    print(f"\n[TOOL CALLED] search_feedback")
    print(f"[QUERY] {query}")

    feedback = [
        "Students say their daily study plans contain too many tasks.",
        "Users want unfinished tasks to automatically move to another day.",
        "Some students say notifications are too frequent.",
        "Users like the weekly learning report.",
    ]

    return "\n".join(feedback)


@function_tool
def calculate_priority(
    impact: int,
    confidence: int,
    effort: int,
) -> float:
    """
    Calculate a product feature priority score

    Args:
        impact: Expected impact from 1 to 10.
        confidence: Confidence from 1 to 10.
        effort: Estimated implementation effort from 1 to 10.
    """

    return (impact * confidence) / effort


@function_tool
def search_product_knowledge(query: str) -> str:
    """
    Search the product knowledge base for information relevant
    to the user's question.

    Use this tool when the question requires evidence from
    product feedback or internal product knowledge.

    Args:
        query: The product topic or question to search for.
    """

    print(f"\n[RAG TOOL CALLED] query={query}")

    results = retrieve(query)

    if not results:
        return "No sufficiently relevant product information was found."

    return "\n".join(
        f"- {result}"
        for result in results
    )
