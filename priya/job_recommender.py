import requests
import os
from dotenv import load_dotenv
from google import genai

# =========================
# LOAD GEMINI KEY
# =========================
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# =========================
# GET REAL JOBS
# =========================
def fetch_jobs():
    url = "https://www.arbeitnow.com/api/job-board-api"
    res = requests.get(url)

    if res.status_code != 200:
        return []

    jobs = res.json().get("data", [])[:30]

    # simple filter (SAFE - always returns something)
    keywords = ["python", "developer", "engineer", "backend", "data", "software"]

    filtered = []

    for job in jobs:
        text = (job.get("title","") + job.get("description","")).lower()

        if any(k in text for k in keywords):
            filtered.append(job)

    # 🔥 fallback: if nothing matches, return original jobs
    if not filtered:
        filtered = jobs[:10]

    return filtered[:10]


# =========================
# FORMAT JOBS
# =========================
def format_jobs(jobs):
    text = ""

    for i, job in enumerate(jobs):
        text += f"""
Job {i+1}
Title: {job.get('title')}
Company: {job.get('company_name')}
Location: {job.get('location')}
Description: {job.get('description','')[:200]}
Link: {job.get('url')}
------------------------
"""
    return text


# =========================
# GEMINI RANKER (SAFE TEXT OUTPUT)
# =========================
def rank_jobs(jobs, user_query):

    job_text = format_jobs(jobs)

    prompt = f"""
You are a job recommender.

User query: {user_query}

Task:
- Pick best 5 jobs
- Explain briefly why each is suitable
- Keep output simple and readable
- Use spacing and bullet points

Jobs:
{job_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# =========================
# MAIN FUNCTION
# =========================
def get_job_recommendations(user_query):

    jobs = fetch_jobs()

    return rank_jobs(jobs, user_query)