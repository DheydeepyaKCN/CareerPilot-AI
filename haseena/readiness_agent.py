from groq import Groq
from dotenv import load_dotenv
import os
import json
from scoring_engine import calculate_readiness

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def readiness_agent(candidate_data):
    score = calculate_readiness(candidate_data)
    if score >= 90:
        level = "Excellent"
    elif score >= 75:
        level = "Job Ready"
    elif score >= 60:
        level = "Almost Ready"
    elif score >= 40:
        level = "Needs Improvement"
    else:
        level = "Beginner"
    prompt = f"""
The candidate has:

ATS Score: {candidate_data["ats_score"]["score"]}

Career Match Score: {candidate_data["career_match"]["match_score"]}

Experience:
{candidate_data["resume_analysis"]["experience_years"]} years

Missing Skills:
{candidate_data["skill_gap"]["missing_skills"]}

Overall Readiness Score:
    {score}

Explain:

1. Why this score?
2. Strengths
3. Weaknesses
4. Learning priorities
5. Interview readiness

Return ONLY JSON.
"""

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[

                {
                    "role":"system",
                    "content":"Return only JSON."
                },

                {
                    "role":"user",
                    "content":prompt
                }

            ],

            response_format={"type":"json_object"},

            temperature=0.2

        )

        result = json.loads(response.choices[0].message.content)

        return {
            "agent_name": "Job Readiness Agent",
            "status": "success",
            "overall_score": score,
            "readiness_level": level,
            "llm_feedback": result
        }

    except Exception as e:

        return {

            "agent_name":"Job Readiness Agent",

            "status":"failed",

            "error":str(e)

        }
