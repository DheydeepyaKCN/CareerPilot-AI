#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pypdf import PdfReader

print("✅ Everything ready! No installation needed!")


# In[2]:


def extract_text_from_pdf(pdf_path):
    text = ""
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        text += page.extract_text()
    return text

def analyze_resume(text):
    skills_list = [
        "python", "java", "sql", "machine learning", "deep learning",
        "excel", "communication", "leadership", "data analysis",
        "tensorflow", "pytorch", "html", "css", "javascript", "c++"
    ]

    text_lower = text.lower()
    found_skills = [skill for skill in skills_list if skill in text_lower]
    email = re.findall(r'\S+@\S+', text)
    word_count = len(text.split())

    print("=" * 40)
    print("📄 RESUME ANALYSIS REPORT")
    print("=" * 40)
    print(f"✅ Skills Found: {', '.join(found_skills) if found_skills else 'None detected'}")
    print(f"📧 Email: {email[0] if email else 'Not found'}")
    print(f"📝 Resume Length: {word_count} words")
    print("=" * 40)

    return found_skills

print("✅ Resume Analyzer ready!")


# In[3]:


# Creates a fake resume as a text file for testing
fake_resume = """
Name: Reddi Lahari
Email: reddilahari@gmail.com
Phone: 9876543210
LinkedIn: linkedin.com/in/reddilahari
GitHub: github.com/reddilahari

OBJECTIVE
Aspiring Data Scientist with passion for machine learning and data analysis.

SKILLS
Python, SQL, Machine Learning, Data Analysis, Excel, Communication

EDUCATION
B.Tech Computer Science - 2024

PROJECTS
1. Student Performance Predictor using Python and machine learning
2. Data Analysis dashboard using Excel and SQL

CERTIFICATIONS
Coursera - Python for Data Science
NPTEL - Data Analytics
"""

with open("test_resume.txt", "w") as f:
    f.write(fake_resume)

print("✅ Test resume created!")

# Test the analyzer with it
resume_text = fake_resume
skills = analyze_resume(resume_text)


# In[4]:


def detect_links(text):
    print("=" * 40)
    print("🔗 GITHUB / LINKEDIN DETECTION")
    print("=" * 40)

    github = re.findall(r'github\.com/[^\s]+', text, re.IGNORECASE)
    linkedin = re.findall(r'linkedin\.com/in/[^\s]+', text, re.IGNORECASE)

    if github:
        print(f"✅ GitHub Found: {github[0]}")
    else:
        print("❌ No GitHub link — add one to your resume!")

    if linkedin:
        print(f"✅ LinkedIn Found: {linkedin[0]}")
    else:
        print("❌ No LinkedIn link — add one to your resume!")
    print("=" * 40)

def detect_certifications(text):
    print("=" * 40)
    print("🏅 CERTIFICATION DETECTION")
    print("=" * 40)

    cert_keywords = [
        "certified", "certification", "certificate", "aws", "google cloud",
        "microsoft", "coursera", "udemy", "nptel", "oracle", "cisco"
    ]

    text_lower = text.lower()
    found_certs = [c for c in cert_keywords if c in text_lower]

    if found_certs:
        print(f"✅ Found: {', '.join(found_certs)}")
    else:
        print("❌ No certifications detected!")
    print("=" * 40)

# RUN BOTH
detect_links(resume_text)
detect_certifications(resume_text)


# In[5]:


career_map = {
    "Data Scientist":     ["python", "machine learning", "deep learning", "sql", "tensorflow"],
    "Web Developer":      ["html", "css", "javascript", "python"],
    "Data Analyst":       ["excel", "sql", "data analysis", "python"],
    "ML Engineer":        ["python", "tensorflow", "pytorch", "machine learning"],
    "Software Developer": ["java", "python", "c++", "javascript"],
    "Business Analyst":   ["excel", "communication", "data analysis", "leadership"]
}

def career_match_agent(skills):
    print("=" * 40)
    print("💼 CAREER MATCH RESULTS")
    print("=" * 40)

    match_scores = {}
    for role, required in career_map.items():
        matched = [s for s in skills if s in required]
        score = (len(matched) / len(required)) * 100
        match_scores[role] = round(score, 1)

    sorted_careers = sorted(match_scores.items(), key=lambda x: x[1], reverse=True)

    for role, score in sorted_careers:
        bar = "█" * int(score // 10)
        print(f"{role:<25} {bar} {score}%")

    print("=" * 40)
    print(f"🏆 Best Match: {sorted_careers[0][0]}")
    print("=" * 40)

career_match_agent(skills)


# In[6]:


def missing_skills_per_job(skills):
    print("=" * 40)
    print("⭐ MISSING SKILLS PER JOB ROLE")
    print("=" * 40)

    for role, required in career_map.items():
        missing = [s for s in required if s not in skills]
        matched = [s for s in required if s in skills]
        score = round((len(matched) / len(required)) * 100, 1)

        print(f"\n💼 {role} — {score}% match")
        if missing:
            print(f"   ❌ Missing: {', '.join(missing)}")
        else:
            print(f"   ✅ You have ALL required skills!")

    print("\n" + "=" * 40)

missing_skills_per_job(skills)


# In[7]:


def plot_skill_chart(skills):
    roles = list(career_map.keys())
    scores = []

    for role, required in career_map.items():
        matched = [s for s in skills if s in required]
        score = (len(matched) / len(required)) * 100
        scores.append(round(score, 1))

    colors_list = ['#2ecc71' if s >= 60 
                   else '#e67e22' if s >= 30 
                   else '#e74c3c' 
                   for s in scores]

    plt.figure(figsize=(10, 5))
    bars = plt.barh(roles, scores, color=colors_list)
    plt.xlabel("Match Percentage (%)")
    plt.title("Career Match - Skill Percentage Chart")
    plt.xlim(0, 100)

    for bar, score in zip(bars, scores):
        plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                 f'{score}%', va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig("skill_chart.png")
    plt.show()
    print("✅ Chart saved!")

plot_skill_chart(skills)


# In[8]:


def ats_score_checker(text, job_description=""):
    print("=" * 40)
    print("🤖 ATS SCORE CHECKER")
    print("=" * 40)

    score = 0
    feedback = []

    if re.search(r'\S+@\S+', text):
        score += 10
        feedback.append("✅ Email found (+10)")
    else:
        feedback.append("❌ No email found")

    if re.search(r'\d{10}|\d{3}[-.\s]\d{3}[-.\s]\d{4}', text):
        score += 10
        feedback.append("✅ Phone number found (+10)")
    else:
        feedback.append("❌ No phone number found")

    sections = ["education", "experience", "skills", "projects", "objective"]
    for section in sections:
        if section in text.lower():
            score += 10
            feedback.append(f"✅ '{section.title()}' section found (+10)")
        else:
            feedback.append(f"❌ Missing '{section.title()}' section")

    words = len(text.split())
    if 300 <= words <= 700:
        score += 20
        feedback.append(f"✅ Good resume length: {words} words (+20)")
    else:
        feedback.append(f"⚠️ Resume length: {words} words (ideal: 300-700)")

    if job_description:
        jd_words = set(job_description.lower().split())
        resume_words = set(text.lower().split())
        overlap = jd_words & resume_words
        keyword_score = min(20, len(overlap))
        score += keyword_score
        feedback.append(f"✅ Job keyword matches: {len(overlap)} (+{keyword_score})")

    print(f"\n📊 ATS SCORE: {score}/100\n")
    for f in feedback:
        print(f)

    print("\n🎯 VERDICT:", end=" ")
    if score >= 70:
        print("🟢 Strong Resume!")
    elif score >= 50:
        print("🟡 Average — needs improvement")
    else:
        print("🔴 Weak — major changes needed")
    print("=" * 40)

    return score

job_desc = "python developer with machine learning and sql data analysis skills"
ats_score = ats_score_checker(resume_text, job_description=job_desc)


# In[9]:


job_desc = "python developer with machine learning and sql data analysis skills"
ats_score = ats_score_checker(resume_text, job_description=job_desc)

# Check actual word count
print(f"\n📝 Actual words extracted: {len(resume_text.split())}")
print(f"\n📄 Resume text preview:")
print(resume_text[:500])


# In[10]:


import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        full_path = os.path.join(dirname, filename)
        print(full_path)


# In[11]:


resume_text = extract_text_from_pdf("/kaggle/input/datasets/laharireddi28/myresume/reddilahari_resume.PDF")
skills = analyze_resume(resume_text)

detect_links(resume_text)
detect_certifications(resume_text)
career_match_agent(skills)
missing_skills_per_job(skills)
plot_skill_chart(skills)

job_desc = "python developer with sql data analysis html css javascript skills"
ats_score = ats_score_checker(resume_text, job_description=job_desc)


# In[12]:


def highlight_keywords(text, skills):
    print("=" * 40)
    print("🔍 KEYWORD HIGHLIGHT SUMMARY")
    print("=" * 40)

    words = text.split()
    highlighted = []
    found = []

    for word in words:
        clean = word.lower().strip(".,;:()")
        if clean in skills:
            highlighted.append(f"[**{word}**]")
            found.append(clean)
        else:
            highlighted.append(word)

    print(f"✅ Keywords detected in resume: {list(set(found))}")
    print(f"\n📄 Resume preview with highlights (first 100 words):")
    print(" ".join(highlighted[:100]) + "...")
    print("=" * 40)

highlight_keywords(resume_text, skills)


# In[13]:


def generate_report(name, skills, ats_score, career_map):
    report_lines = []
    report_lines.append("=" * 50)
    report_lines.append("    AI CAREERPILOT - RESUME ANALYSIS REPORT")
    report_lines.append("=" * 50)
    report_lines.append(f"Candidate Name  : {name}")
    report_lines.append(f"Email           : laharireddi36@gmail.com")
    report_lines.append(f"ATS Score       : {ats_score}/100")
    report_lines.append("=" * 50)

    report_lines.append("\nSKILLS FOUND:")
    report_lines.append(f"  {', '.join(skills)}")

    report_lines.append("\nCAREER MATCH RESULTS:")
    for role, required in career_map.items():
        matched = [s for s in skills if s in required]
        missing = [s for s in required if s not in skills]
        score = round((len(matched)/len(required))*100, 1)
        report_lines.append(f"  {role:<25} {score}% match")
        if missing:
            report_lines.append(f"  Missing skills : {', '.join(missing)}")

    report_lines.append("\nATS VERDICT:")
    if ats_score >= 70:
        report_lines.append("  Strong Resume — likely to pass ATS!")
    elif ats_score >= 50:
        report_lines.append("  Average Resume — needs improvement")
    else:
        report_lines.append("  Weak Resume — major changes needed")

    report_lines.append("\nRECOMMENDATIONS:")
    report_lines.append("  1. Add GitHub profile link to resume")
    report_lines.append("  2. Add LinkedIn profile link to resume")
    report_lines.append("  3. Add Objective section at the top")
    report_lines.append("  4. Learn TensorFlow to boost Data Scientist match")

    report_lines.append("\n" + "=" * 50)
    report_lines.append("Generated by AI CareerPilot")
    report_lines.append("=" * 50)

    report_text = "\n".join(report_lines)

    with open("resume_analysis_report.txt", "w") as f:
        f.write(report_text)

    print(report_text)
    print("\n✅ Report saved! Download from Kaggle Output panel!")

generate_report("Reddi Lahari", skills, 87, career_map)


# In[14]:


print("=" * 50)
print("         AI CAREERPILOT")
print("   Resume Intelligence System")
print("=" * 50)
print("Running all 9 features...\n")

resume_text = extract_text_from_pdf("/kaggle/input/datasets/laharireddi28/myresume/reddilahari_resume.PDF")

skills = analyze_resume(resume_text)
detect_links(resume_text)
detect_certifications(resume_text)
career_match_agent(skills)
missing_skills_per_job(skills)
plot_skill_chart(skills)

job_desc = "python developer with sql data analysis html css javascript skills"
ats_score = ats_score_checker(resume_text, job_description=job_desc)

highlight_keywords(resume_text, skills)
generate_report("Reddi Lahari", skills, ats_score, career_map)

print("\n" + "=" * 50)
print("✅ ALL 9 FEATURES COMPLETED SUCCESSFULLY!")
print("=" * 50)


# In[ ]:




