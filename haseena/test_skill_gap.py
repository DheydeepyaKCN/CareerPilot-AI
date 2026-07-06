from skill_gap_agent import skill_gap_agent
import json

# -----------------------------
# Mock Resume Data
# -----------------------------

resume_data = {
    "name": "John Doe",

    "skills": [
        "Python",
        "SQL",
        "Machine Learning",
        "Pandas",
        "NumPy"
    ],

    "projects": [
        "Spam Detection using Machine Learning",
        "Movie Recommendation System"
    ],

    "education": "B.Tech Computer Engineering",

    "experience": "Fresher",

    "certifications": [
        "Google Gen AI Intensive Course",
        "IBM SkillsBuild AI"
    ]
}

career_role = "Machine Learning Engineer"

# -----------------------------
# Run Agent
# -----------------------------

print("=" * 60)
print("Running Skill Gap Analysis Agent...")
print("=" * 60)

result = skill_gap_agent(
    resume_data,
    career_role
)

print("\nAgent Output:\n")

print(json.dumps(result, indent=4))