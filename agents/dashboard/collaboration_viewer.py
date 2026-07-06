from agents.dashboard.event_logger import AGENT_LOG


def show_collaboration():

    print("\n========== Agent Collaboration ==========\n")

    for i, log in enumerate(AGENT_LOG, start=1):

        print(f"Step {i}")

        print(f"Agent : {log['agent']}")

        print(f"Status : {log['status']}")

        print(f"Input : {log['input']}")

        print(f"Output : {log['output']}")

        print("-" * 50)