from agents import function_tool


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