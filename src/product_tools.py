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


