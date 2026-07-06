from event_logger import log_agent
from progress_dashboard import show_dashboard
from collaboration_viewer import show_collaboration

log_agent(
    "Resume Analyzer",
    "Completed",
    "resume.pdf",
    "Python, SQL, Docker",
    1.2,
)

log_agent(
    "Career Match",
    "Completed",
    "Python SQL Docker",
    "Machine Learning Engineer",
    0.7,
)

log_agent(
    "Skill Gap",
    "Completed",
    "ML Engineer",
    ["AWS", "TensorFlow"],
    1.1,
)

log_agent(
    "Learning Resources",
    "Running",
    ["AWS", "TensorFlow"],
    None,
)

show_dashboard()

show_collaboration()