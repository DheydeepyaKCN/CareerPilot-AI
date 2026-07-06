import streamlit as st
import pandas as pd

from agents.resume.resume_analyzer import run_resume_analysis

st.title("💼 Job Recommendations")
st.write("AI-powered job recommendations based on your resume.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file and st.button("Recommend Jobs"):

    # Save uploaded resume
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Analyze Resume
    resume = run_resume_analysis("temp_resume.pdf")

    st.success("✅ Resume analyzed successfully!")

    # -----------------------------
    # Resume Summary
    # -----------------------------
    st.subheader("🛠 Detected Skills")
    st.write(", ".join(resume["skills"]))

    st.subheader("🎯 Best Career Match")
    career = resume["career_match"]["best_match"]
    st.success(career)

    # -----------------------------
    # Load Jobs Dataset
    # -----------------------------
    jobs_df = pd.read_csv("data/jobs.csv")

    recommended = jobs_df[
        jobs_df["career"].str.lower() == career.lower()
    ]

    # -----------------------------
    # Display Jobs
    # -----------------------------
    st.subheader("💼 Recommended Jobs")

    if not recommended.empty:

        for _, job in recommended.iterrows():

            with st.container():

                st.markdown(f"### {job['job_title']}")

                st.write(f"**🏢 Company:** {job['company']}")
                st.write(f"**📍 Location:** {job['location']}")
                st.write(f"**💼 Experience:** {job['experience']}")
                st.write(f"**🛠 Skills:** {job['skills']}")

                st.markdown("---")

    else:
        st.warning("No matching jobs found.")

    # -----------------------------
    # ATS Score
    # -----------------------------
    st.subheader("⭐ ATS Score")

    st.metric(
        "ATS Score",
        f"{resume['ats_score']['score']}%"
    )

    st.progress(resume["ats_score"]["score"] / 100)

    # -----------------------------
    # Career Match Scores
    # -----------------------------
    st.subheader("📌 Career Match Scores")

    st.json(resume["career_scores"])

    st.success("🎉 These jobs best match your current profile!")