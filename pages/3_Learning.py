import streamlit as st

from agents.resume.resume_analyzer import run_resume_analysis
from agents.learning.learning_rag import generate_learning_path

st.title("📚 Learning Resources")
st.write("AI-powered personalized learning recommendations.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

career = st.selectbox(
    "Target Career",
    [
        "ML Engineer",
        "Data Scientist",
        "Software Engineer",
        "Data Analyst"
    ]
)

if uploaded_file and st.button("Generate Learning Plan"):

    # ------------------------------------
    # Save Uploaded Resume
    # ------------------------------------
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # ------------------------------------
    # Analyze Resume
    # ------------------------------------
    resume = run_resume_analysis("temp_resume.pdf")

    st.success("✅ Resume analyzed successfully!")

    st.subheader("🛠 Detected Skills")

    if resume["skills"]:
        st.write(", ".join(resume["skills"]))
    else:
        st.warning("No skills detected.")

    # ------------------------------------
    # Course Recommendations
    # ------------------------------------
    st.subheader("📚 Recommended Courses")

    all_courses = []
    shown = set()

    for skill in resume["skills"]:

        result = generate_learning_path({
            "interest": skill,
            "level": "Beginner"
        })

        for course in result["recommended_courses"]:

            name = course.get("course", "")

            if name not in shown:
                shown.add(name)
                all_courses.append(course)

    if all_courses:

        for course in all_courses:

            st.markdown("---")

            st.markdown(f"### 📘 {course['course']}")

            st.write(f"**Topic:** {course['topic']}")
            st.write(f"**Platform:** {course['platform']}")
            st.write(f"**Level:** {course['level']}")

    else:

        st.warning("No matching courses found for the detected skills.")

    # ------------------------------------
    # Generic Learning Roadmap
    # ------------------------------------
    st.subheader("🛣 Suggested Learning Path")

    steps = [
        "Learn programming fundamentals",
        "Master Python",
        "Practice SQL",
        "Build real-world projects",
        "Learn Git & GitHub",
        "Practice interview questions",
        "Apply for internships/jobs"
    ]

    for i, step in enumerate(steps, 1):
        st.write(f"**Step {i}:** {step}")

    st.success("🎯 Keep learning consistently and build projects to strengthen your profile!")