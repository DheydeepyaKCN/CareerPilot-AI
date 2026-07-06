import streamlit as st

from agents.resume.resume_analyzer import run_resume_analysis
from agents.career.skill_gap_agent import skill_gap_agent
from agents.career.career_roadmap import generate_career_roadmap
from agents.career.readiness_agent import readiness_agent

st.title("🎯 Career Guidance")
st.write("AI-powered career planning using multiple intelligent agents.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

career = st.selectbox(
    "Select Target Career",
    [
        "ML Engineer",
        "Data Scientist",
        "Software Engineer",
        "Data Analyst"
    ]
)

if uploaded_file and st.button("Generate Career Guidance"):

    # Save uploaded resume
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # ------------------------------------------------
    # Resume Analyzer
    # ------------------------------------------------
    resume = run_resume_analysis("temp_resume.pdf")

    resume_data = {
        "skills": resume["skills"],
        "email": resume["email"],
        "phone": resume["phone"],
        "certifications": resume["certifications"]
    }

    st.success("✅ Resume analyzed successfully!")

    # ------------------------------------------------
    # Skill Gap Agent
    # ------------------------------------------------
    with st.spinner("Finding Skill Gaps..."):
        gap = skill_gap_agent(resume_data, career)

    st.subheader("⭐ Skill Gap Analysis")

    if gap["status"] == "success":

        st.write("### Strengths")
        for item in gap["strengths"]:
            st.write("•", item)

        st.write("### Missing Skills")
        for item in gap["missing_skills"]:
            st.write("•", item)

        st.write("### Suggestions")
        for item in gap["suggestions"]:
            st.write("•", item)

    else:
        st.error(gap["error"])

    # ------------------------------------------------
    # Career Roadmap
    # ------------------------------------------------
    roadmap_input = {
        "skills": resume["skills"],
        "interest": career,
        "year": "Final Year"
    }

    roadmap = generate_career_roadmap(roadmap_input)

    st.subheader("🗺 Career Roadmap")

    st.success(roadmap["career_path"])

    st.write("### Steps")
    for step in roadmap["steps"]:
        st.write("•", step)

    st.write("### Skills To Learn")
    for skill in roadmap["skills_to_learn"]:
        st.write("•", skill)

    st.info(roadmap["suggestion"])

    # ------------------------------------------------
    # Readiness Agent
    # ------------------------------------------------
    readiness_input = {
        "ats_score": resume["ats_score"],

        "career_match": {
            "match_score": max(resume["career_scores"].values())
        },

        "resume_analysis": {
            "experience_years": resume["experience_years"]
        },

        "skill_gap": gap
    }

    with st.spinner("Calculating Job Readiness..."):
        ready = readiness_agent(readiness_input)

    st.subheader("📈 Job Readiness")

    if ready["status"] == "success":

        st.metric(
            "Readiness Score",
            f'{ready["overall_score"]}%'
        )

        st.progress(ready["overall_score"] / 100)

        st.success(ready["readiness_level"])

        st.subheader("🤖 AI Feedback")
        st.write(ready["llm_feedback"])

    else:
        st.error(ready["error"])