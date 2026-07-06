from groq import Groq
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def skill_gap_agent(resume_data, career_role):
    """
    Skill Gap Analysis Agent

    Parameters
    ----------
    resume_data : dict
        Dictionary containing extracted resume information.

    career_role : str
        Target career role.

    Returns
    -------
    dict
        {
            "strengths": [],
            "missing_skills": [],
            "suggestions": []
        }
    """

    prompt = f"""
You are an expert AI Career Coach.

Candidate Resume:
{json.dumps(resume_data, indent=2)}

Target Career:
{career_role}

Your task:

1. Identify the candidate's strengths.
2. Identify the important missing skills for the target role.
3. Give practical suggestions to improve.

Return ONLY valid JSON.

Example format:

{{
    "strengths": [
        "Python",
        "Machine Learning"
    ],

    "missing_skills": [
        "Docker",
        "AWS"
    ],

    "suggestions": [
        "Learn Docker",
        "Complete one AWS deployment project"
    ]
}}

Do NOT return markdown.

Do NOT explain anything.

Only return JSON.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You only return valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        content = response.choices[0].message.content

        print("\n========== RAW OUTPUT ==========\n")
        print(content)
        print("\n===============================\n")

        # Remove markdown if Groq returns it
        content = content.strip()

        if content.startswith("```json"):
            content = content.replace("```json", "", 1)

        if content.startswith("```"):
            content = content.replace("```", "", 1)

        if content.endswith("```"):
            content = content[:-3]

        content = content.strip()

        # Convert JSON string into Python dictionary
        result = json.loads(content)

        # Add agent metadata
        result = {
            "agent_name": "Skill Gap Analysis Agent",
            "status": "success",
            "career_role": career_role,
            **result
        }

        return result
    except json.JSONDecodeError:
        return {
            "agent_name": "Skill Gap Analysis Agent",
            "status": "failed",
            "error": "Model did not return valid JSON."
        }

    except Exception as e:
        return {
            "agent_name": "Skill Gap Analysis Agent",
            "status": "failed",
            "career_role": career_role,
            "error": str(e)
        }