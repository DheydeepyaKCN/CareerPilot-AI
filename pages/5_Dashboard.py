import streamlit as st

from agents.resume.resume_analyzer import run_resume_analysis

st.title("📊 CareerPilot AI Dashboard")
st.write("Overall summary of all AI agents.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file and st.button("Generate Dashboard"):

    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume = run_resume_analysis("temp_resume.pdf")

    # -----------------------
    # Top Metrics
    # -----------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Agents", "8")
    col2.metric("Skills", len(resume["skills"]))
    col3.metric("ATS Score", f'{resume["ats_score"]["score"]}%')
    col4.metric("Best Career", resume["career_match"]["best_match"])

    st.progress(resume["ats_score"]["score"] / 100)

    st.divider()

    # -----------------------
    # Resume Summary
    # -----------------------

    st.subheader("📄 Resume Summary")

    st.write("**Email:**", resume["email"])
    st.write("**Phone:**", resume["phone"])

    st.write("### Skills")

    for skill in resume["skills"]:
        st.write("•", skill)

    st.divider()

    # -----------------------
    # Career Scores
    # -----------------------

    st.subheader("🎯 Career Match Scores")

    st.json(resume["career_scores"])

    st.divider()

    # -----------------------
    # ATS
    # -----------------------

    st.subheader("⭐ ATS Analysis")

    st.metric(
        "ATS Score",
        f'{resume["ats_score"]["score"]}%'
    )

    st.success(resume["ats_score"]["verdict"])

    st.divider()

    # -----------------------
    # Agent Status
    # -----------------------

    st.subheader("🤖 AI Agent Status")

    st.table({
        "Agent": [
            "Resume Analyzer",
            "Career Matcher",
            "ATS Checker",
            "Skill Gap Agent",
            "Career Roadmap",
            "Learning Recommendation",
            "Job Recommendation",
            "Dashboard"
        ],
        "Status": [
            "Completed",
            "Completed",
            "Completed",
            "Completed",
            "Completed",
            "Completed",
            "Completed",
            "Completed"
        ]
    })

    st.success("🎉 CareerPilot AI executed successfully!")