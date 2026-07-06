import streamlit as st

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# ----------------------------------
# CUSTOM CSS
# ----------------------------------

st.markdown("""
<style>

.main{
    background-color:#f8fafc;
}

.block-container{
    padding-top:2rem;
}

.big-font{
    font-size:42px;
    font-weight:bold;
    color:#1E3A8A;
}

.subtitle{
    font-size:20px;
    color:#475569;
}

.metric-card{
    background:#ffffff;
    border-radius:15px;
    padding:20px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.title("🚀 CareerPilot AI")

st.sidebar.markdown("---")

st.sidebar.success("11 AI Agents")

st.sidebar.info("Google AI Agents Capstone")

st.sidebar.markdown("---")

st.sidebar.write("⬅ Use the pages above to navigate.")

# ----------------------------------
# HOME PAGE
# ----------------------------------

st.markdown("<div class='big-font'>CareerPilot AI</div>", unsafe_allow_html=True)

st.markdown(
"""
<div class='subtitle'>
AI-powered Multi-Agent Career Guidance Platform
</div>
""",
unsafe_allow_html=True
)

st.write("")

st.markdown("""
CareerPilot AI helps students and professionals by combining multiple AI agents.

### Features

- 📄 Resume Intelligence
- 🎯 Career Matching
- ⭐ ATS Score Prediction
- 🧠 Skill Gap Analysis
- 📚 RAG-based Learning Resources
- 📈 Job Readiness Prediction
- 🗺 Personalized Career Roadmaps
- 💼 AI Job Recommendations
- 🤝 Multi-Agent Collaboration Dashboard
""")

st.divider()

col1, col2, col3, col4 = st.columns(4)

col1.metric("AI Agents", "11")
col2.metric("Models", "2")
col3.metric("RAG", "FAISS")
col4.metric("Architecture", "Multi-Agent")

st.divider()

st.subheader("🚀 Start Analysis")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

career = st.text_input(
    "Target Career",
    "Machine Learning Engineer"
)

query = st.text_area(
    "Career Goal",
    "I want to become an AI Engineer."
)

if st.button("🚀 Initialize CareerPilot"):

    st.success("CareerPilot initialized successfully!")

    st.info(
        "Use the pages in the left sidebar to access each AI agent."
    )

st.divider()

st.subheader("🧠 Multi-Agent Workflow")

st.code("""
Resume
   │
   ▼
Resume Analyzer
   │
   ▼
Career Match
   │
   ▼
Skill Gap Agent
   │
   ▼
Learning RAG
   │
   ▼
Career Roadmap
   │
   ▼
Readiness Agent
   │
   ▼
Job Recommendation Agent
""")

