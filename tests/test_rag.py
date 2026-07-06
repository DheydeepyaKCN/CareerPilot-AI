from rag_agent import rag_agent
import json

skill_gap_output = {
    "agent_name": "Skill Gap Analysis Agent",
    "status": "success",
    "career_role": "Machine Learning Engineer",

    "missing_skills": [
        "Docker",
        "AWS",
        "Leadership"
    ]
}

result = rag_agent(skill_gap_output)

print(json.dumps(result, indent=4))