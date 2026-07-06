import streamlit as st
import tempfile
import os

from agents.resume.resume_analyzer import run_resume_analysis

st.set_page_config(page_title="Resume Intelligence", page_icon="📄")

st.title("📄 Resume Intelligence")
st.write("Upload your resume and get a complete AI analysis.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Target Job Description (Optional)",
    placeholder="Python Developer with SQL and Machine Learning..."
)

if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:

        tmp.write(uploaded_file.read())

        pdf_path = tmp.name

    with st.spinner("Analyzing Resume..."):

        result = run_resume_analysis(
            pdf_path,
            job_description
        )

    st.success("Resume Analysis Completed!")

    # -------------------------
    # Basic Details
    # -------------------------

    analysis = result["analysis"]

    col1, col2, col3 = st.columns(3)

    col1.metric("Skills", len(analysis["skills"]))

    col2.metric(
        "ATS Score",
        result["ats_score"]["score"]
    )

    col3.metric(
        "Best Career",
        result["career_match"]["best_match"]
    )

    st.divider()

    # -------------------------
    # Skills
    # -------------------------

    st.subheader("🛠 Skills Detected")

    if analysis["skills"]:

        st.write(analysis["skills"])

    else:

        st.warning("No skills detected.")

    # -------------------------
    # Contact Details
    # -------------------------

    st.subheader("📧 Contact Information")

    st.write("Email :", analysis["email"])

    st.write("Phone :", analysis["phone"])

    # -------------------------
    # Links
    # -------------------------

    st.subheader("🔗 Links")

    st.write("GitHub :", result["links"]["github"])

    st.write("LinkedIn :", result["links"]["linkedin"])

    # -------------------------
    # Certifications
    # -------------------------

    st.subheader("🏅 Certifications")

    if result["certifications"]:

        st.write(result["certifications"])

    else:

        st.info("No certifications detected.")

    # -------------------------
    # Career Match
    # -------------------------

    st.subheader("🎯 Career Match Scores")

    st.json(result["career_match"]["scores"])

    # -------------------------
    # Missing Skills
    # -------------------------

    st.subheader("⭐ Missing Skills")

    st.json(result["missing_skills"])

    # -------------------------
    # ATS
    # -------------------------

    st.subheader("🤖 ATS Analysis")

    st.metric(
        "ATS Score",
        result["ats_score"]["score"]
    )

    st.write(result["ats_score"]["verdict"])

    # -------------------------
    # Skill Chart
    # -------------------------

    st.subheader("📊 Career Match Chart")

    st.image(result["chart"])

    # -------------------------
    # Report
    # -------------------------

    st.subheader("📄 Resume Report")

    st.text(result["report"])

    os.remove(pdf_path)