from groq import Groq
from dotenv import load_dotenv
import os
import json

from retriever import retrieve_resources

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def rag_agent(skill_gap_output):
    """
    Learning Resource Recommendation Agent (RAG)

    Parameters
    ----------
    skill_gap_output : dict

    Returns
    -------
    dict
    """

    try:

        # -----------------------------
        # Extract missing skills
        # -----------------------------
        missing_skills = skill_gap_output["missing_skills"]

        # Build search query
        query = " ".join(missing_skills)

        # -----------------------------
        # Retrieve documents
        # -----------------------------
        retrieved_docs = retrieve_resources(query, top_k=5)

        # -----------------------------
        # Prompt
        # -----------------------------
        prompt = f"""
You are an AI Career Learning Advisor.

Candidate is missing these skills:

{missing_skills}

Here are the retrieved learning resources:

{json.dumps(retrieved_docs, indent=2)}

Your task:

1. Recommend the BEST learning path.
2. Arrange skills in learning order.
3. Explain why each skill matters.
4. Recommend the best resource.
5. Mention estimated learning duration.

Return ONLY valid JSON.

Example:

{{
    "learning_plan":[
        {{
            "skill":"Docker",
            "priority":"High",
            "reason":"Required for deployment",
            "duration":"2 weeks",
            "recommended_resource":"Docker Get Started"
        }}
    ]
}}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Return only valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": "Return ONLY valid JSON. Do not use markdown or code fences."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            response_format={"type": "json_object"},

            temperature=0.2
        )
        result = json.loads(response.choices[0].message.content)
        return {
            "agent_name": "Learning Resource Recommendation Agent",
            "status": "success",
            "learning_plan": result["learning_plan"]
        }

    except Exception as e:

        return {
            "agent_name": "Learning Resource Recommendation Agent",
            "status": "failed",
            "error": str(e)
        }