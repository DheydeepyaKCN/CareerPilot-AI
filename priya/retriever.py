import pandas as pd

def load_courses():
    return pd.read_csv("data/courses.csv")


def retrieve_courses(query, level=None):
    df = load_courses()

    query = query.lower()

    # simple keyword matching (RAG-lite version)
    filtered = df[df["topic"].str.lower().str.contains(query)]

    if level:
        filtered = filtered[filtered["level"] == level]

    return filtered.to_dict(orient="records")