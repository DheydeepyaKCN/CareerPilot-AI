import pandas as pd
from agents.dashboard.event_logger import AGENT_LOG


def show_dashboard():

    if len(AGENT_LOG) == 0:
        print("No agents have executed.")
        return

    df = pd.DataFrame(AGENT_LOG)

    print("\n=========== Progress Dashboard ===========\n")

    print(df[["agent", "status", "execution_time"]])

    completed = (df["status"] == "Completed").sum()

    total = len(df)

    progress = round((completed / total) * 100)

    print(f"\nOverall Progress : {progress}%")