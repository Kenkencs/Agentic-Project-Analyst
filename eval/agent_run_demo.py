"""Manual agent run for inspecting tool calls and final output."""

from agents import Runner

from src.agent import agent


def main() -> None:
    result = Runner.run_sync(
        agent,
        "Why are students struggling with too much workload?",
    )

    print("\nFINAL OUTPUT:")
    print(result.final_output)

    print("\nRUN ITEMS:")

    for item in result.new_items:
        print(type(item).__name__)
        print(item)
        print("------------------")


if __name__ == "__main__":
    main()
