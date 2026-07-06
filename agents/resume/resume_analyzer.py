import re
import matplotlib.pyplot as plt
from pypdf import PdfReader

# =====================================================
# CAREER MAP
# =====================================================

career_map = {
    "Data Scientist": [
        "python",
        "machine learning",
        "deep learning",
        "sql",
        "tensorflow"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "python"
    ],

    "Data Analyst": [
        "excel",
        "sql",
        "data analysis",
        "python"
    ],

    "ML Engineer": [
        "python",
        "tensorflow",
        "pytorch",
        "machine learning"
    ],

    "Software Developer": [
        "java",
        "python",
        "c++",
        "javascript"
    ],

    "Business Analyst": [
        "excel",
        "communication",
        "data analysis",
        "leadership"
    ]
}


# =====================================================
# PDF READER
# =====================================================

def extract_text_from_pdf(pdf_path):

    text = ""

    reader = PdfReader(pdf_path)

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


# =====================================================
# SKILL DETECTION
# =====================================================

def analyze_resume(text):

    skills_database = [

        "python",
        "java",
        "sql",
        "machine learning",
        "deep learning",
        "excel",
        "communication",
        "leadership",
        "data analysis",
        "tensorflow",
        "pytorch",
        "html",
        "css",
        "javascript",
        "c++"

    ]

    text_lower = text.lower()

    found_skills = [

        skill

        for skill in skills_database

        if skill in text_lower

    ]

    email = re.findall(r"\S+@\S+", text)

    phone = re.findall(
        r"\d{10}|\d{3}[-.\s]\d{3}[-.\s]\d{4}",
        text
    )

    return {

        "skills": found_skills,

        "email": email[0] if email else None,

        "phone": phone[0] if phone else None,

        "word_count": len(text.split())

    }


# =====================================================
# LINK DETECTION
# =====================================================

def detect_links(text):

    github = re.findall(

        r"github\.com/[^\s]+",

        text,

        re.IGNORECASE

    )

    linkedin = re.findall(

        r"linkedin\.com/in/[^\s]+",

        text,

        re.IGNORECASE

    )

    return {

        "github":

        github[0] if github else None,

        "linkedin":

        linkedin[0] if linkedin else None

    }


# =====================================================
# CERTIFICATIONS
# =====================================================

def detect_certifications(text):

    keywords = [

        "certified",

        "certificate",

        "certification",

        "aws",

        "coursera",

        "google cloud",

        "oracle",

        "udemy",

        "nptel",

        "cisco",

        "microsoft"

    ]

    text_lower = text.lower()

    found = [

        c

        for c in keywords

        if c in text_lower

    ]

    return found


# =====================================================
# CAREER MATCH
# =====================================================

def career_match_agent(skills):

    scores = {}

    for role, required in career_map.items():

        matched = [

            s

            for s in skills

            if s in required

        ]

        percentage = (

            len(matched)

            /

            len(required)

        ) * 100

        scores[role] = round(percentage, 1)

    best = max(

        scores,

        key=scores.get

    )

    return {

        "best_match": best,

        "scores": scores

    }


# =====================================================
# MISSING SKILLS
# =====================================================

def missing_skills_per_job(skills):

    result = {}

    for role, required in career_map.items():

        missing = [

            skill

            for skill in required

            if skill not in skills

        ]

        result[role] = missing

    return result
    # =====================================================
# ATS SCORE
# =====================================================

def ats_score_checker(text, job_description=""):

    score = 0
    feedback = []

    # Email
    if re.search(r"\S+@\S+", text):
        score += 10
        feedback.append("Email Found")
    else:
        feedback.append("Email Missing")

    # Phone
    if re.search(r"\d{10}|\d{3}[-.\s]\d{3}[-.\s]\d{4}", text):
        score += 10
        feedback.append("Phone Found")
    else:
        feedback.append("Phone Missing")

    # Sections
    sections = [
        "education",
        "experience",
        "skills",
        "projects",
        "objective"
    ]

    for section in sections:

        if section in text.lower():
            score += 10

    # Resume Length

    words = len(text.split())

    if 300 <= words <= 700:
        score += 20

    # JD Matching

    if job_description:

        jd = set(job_description.lower().split())

        resume = set(text.lower().split())

        overlap = jd & resume

        score += min(20, len(overlap))

    if score >= 70:
        verdict = "Strong Resume"

    elif score >= 50:
        verdict = "Average Resume"

    else:
        verdict = "Needs Improvement"

    return {

        "score": score,

        "verdict": verdict,

        "feedback": feedback

    }


# =====================================================
# KEYWORD HIGHLIGHT
# =====================================================

def highlight_keywords(text, skills):

    words = text.split()

    highlighted = []

    for word in words:

        clean = word.lower().strip(".,;:()")

        if clean in skills:

            highlighted.append(f"**{word}**")

        else:

            highlighted.append(word)

    return " ".join(highlighted)


# =====================================================
# SKILL CHART
# =====================================================

def plot_skill_chart(skills, save_path="skill_chart.png"):

    roles = []

    scores = []

    for role, required in career_map.items():

        matched = [

            s

            for s in skills

            if s in required

        ]

        score = (

            len(matched)

            /

            len(required)

        ) * 100

        roles.append(role)

        scores.append(round(score, 1))

    colors = []

    for s in scores:

        if s >= 60:

            colors.append("#2ecc71")

        elif s >= 30:

            colors.append("#f39c12")

        else:

            colors.append("#e74c3c")

    plt.figure(figsize=(10,5))

    bars = plt.barh(

        roles,

        scores,

        color=colors

    )

    plt.xlim(0,100)

    plt.xlabel("Match %")

    plt.title("Career Match")

    for bar, score in zip(bars, scores):

        plt.text(

            bar.get_width()+1,

            bar.get_y()+bar.get_height()/2,

            f"{score}%"

        )

    plt.tight_layout()

    plt.savefig(save_path)

    plt.close()

    return save_path


# =====================================================
# REPORT
# =====================================================

def generate_report(

        analysis,

        career,

        ats,

        output_file="resume_report.txt"

):

    lines = []

    lines.append("="*50)

    lines.append("CAREERPILOT AI REPORT")

    lines.append("="*50)

    lines.append("")

    lines.append(f"Email : {analysis['email']}")

    lines.append(f"Phone : {analysis['phone']}")

    lines.append("")

    lines.append("Detected Skills:")

    for skill in analysis["skills"]:

        lines.append(f"• {skill}")

    lines.append("")

    lines.append(f"ATS Score : {ats['score']}")

    lines.append(f"Verdict : {ats['verdict']}")

    lines.append("")

    lines.append(f"Best Career Match : {career['best_match']}")

    lines.append("")

    lines.append("Career Scores")

    for role, score in career["scores"].items():

        lines.append(f"{role} : {score}%")

    report = "\n".join(lines)

    with open(output_file,"w",encoding="utf-8") as f:

        f.write(report)

    return report


# =====================================================
# MASTER FUNCTION
# =====================================================

def run_resume_analysis(

        pdf_path,

        job_description=""

):

    text = extract_text_from_pdf(pdf_path)

    analysis = analyze_resume(text)

    links = detect_links(text)

    certifications = detect_certifications(text)

    career = career_match_agent(

        analysis["skills"]

    )

    missing = missing_skills_per_job(

        analysis["skills"]

    )

    ats = ats_score_checker(

        text,

        job_description

    )

    highlighted = highlight_keywords(

        text,

        analysis["skills"]

    )

    chart = plot_skill_chart(

        analysis["skills"]

    )

    report = generate_report(

        analysis,

        career,

        ats

    )

    return {

        # Original outputs
        "text": text,

        "analysis": analysis,

        "links": links,

        "certifications": certifications,

        "career_match": career,

        "career_scores": career["scores"],

        "missing_skills": missing,

        "ats_score": ats,

        "highlighted_resume": highlighted,

        "chart": chart,

        "report": report,

        # -------- Added for other agents --------
        "skills": analysis["skills"],

        "email": analysis["email"],

        "phone": analysis["phone"],

        "word_count": analysis["word_count"],

        "experience_years": 0

    }