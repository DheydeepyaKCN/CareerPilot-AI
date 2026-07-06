import pandas as pd

def load_courses():
    df = pd.read_csv("data/courses.csv")

    # normalize EVERYTHING (THIS IS THE FIX)
    df.columns = df.columns.str.lower()
    df = df.apply(lambda col: col.astype(str).str.lower().str.strip())
    print(df.head())
    print(df.columns)

    return df


def retrieve_courses(query, level=None):
    df = load_courses()

    print("\nQUERY:", query)
    print("\nTOPICS IN DATA:")
    print(df["topic"].tolist())

    query = str(query).lower().strip()

    filtered = df[df["topic"].str.contains(query, na=False)]

    print("\nFILTERED RESULT:")
    print(filtered)

    return filtered.to_dict(orient="records")


def generate_learning_path(user_input):
    interest = user_input.get("interest", "")
    level = user_input.get("level", None)

    courses = retrieve_courses(interest, level)

    return {
        "interest": interest,
        "recommended_courses": courses,
        "learning_steps": [
            f"Start learning {interest} basics",
            "Practice daily coding",
            "Build small projects",
            "Learn intermediate concepts",
            "Apply in real projects"
        ],
        "message": "Learning path generated successfully"
    }