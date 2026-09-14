from agents import Runner

from src.agent import agent


def get_called_tools(result) -> list[str]:
    called_tools = []

    for item in result.new_items:
        if type(item).__name__ == "ToolCallItem":
            called_tools.append(
                item.raw_item.name
            )

    return called_tools


def get_tool_outputs(result) -> list[str]:
    outputs = []

    for item in result.new_items:
        if type(item).__name__ == "ToolCallOutputItem":
            outputs.append(str(item.output))

    return outputs


def evidence_found(tool_outputs: list[str], expected_evidence: list[str]) -> bool:
    combined_output = " ".join(tool_outputs).lower()

    return all(
        evidence.lower() in combined_output
        for evidence in expected_evidence
    )


test_cases = [
    {
        "question": "Why are students struggling with workload?",
        "expected_tool": "search_product_knowledge",
    },
    {
        "question": "What do users think about payments?",
        "expected_tool": "search_product_knowledge",
    },
    {
        "question": "Give me three creative names for a study app.",
        "expected_tool": None,
    },
    {
        "question": "Explain what a study planner is.",
        "expected_tool": None,
    },
]


def main() -> None:
    correct = 0

    for case in test_cases:
        result = Runner.run_sync(
            agent,
            case["question"],
        )

        called_tools = get_called_tools(result)
        expected_tool = case["expected_tool"]

        if expected_tool is None:
            passed = len(called_tools) == 0
        else:
            passed = expected_tool in called_tools

        if passed:
            correct += 1

        print("\nQUESTION:", case["question"])
        print("EXPECTED:", expected_tool)
        print("CALLED:", called_tools)
        print("PASS:", passed)

    accuracy = correct / len(test_cases)

    print("\nFINAL RESULT")
    print(f"Passed: {correct}/{len(test_cases)}")
    print(f"Tool Selection Accuracy: {accuracy:.2%}")

    result = Runner.run_sync(
        agent,
        "Why are students struggling with workload?",
    )

    outputs = get_tool_outputs(result)

    print("TOOL OUTPUTS:")
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
