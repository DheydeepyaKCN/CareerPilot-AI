# 🚀 CareerPilot AI

CareerPilot AI is an AI-powered career guidance platform that helps students and job seekers analyze resumes, identify skill gaps, receive personalized learning recommendations, explore suitable job opportunities, and evaluate their job readiness. The platform integrates multiple AI agents to provide an end-to-end career assistance experience.

---

# 📌 Features

## 📄 Resume Intelligence
- Upload resumes in PDF format.
- Extracts contact information.
- Detects technical and soft skills.
- Calculates ATS (Applicant Tracking System) Score.
- Suggest improvements to better match job requirements.

## 🎯 Career Guidance
- AI-based Skill Gap Analysis.
- Personalized Career Roadmap.
- Job Readiness Score.
- AI-generated career suggestions.

## 📚 Learning Resources
- Recommends learning resources based on detected skills.
- Displays structured learning paths.
- Suggests relevant courses from the learning dataset.

## 💼 Job Recommendations
- Matches candidates with suitable job roles.
- Displays company, location, experience, and required skills.
- Uses a job dataset for recommendations.

## 📊 Dashboard
- Displays an overall summary of resume analysis.
- Shows career match scores.
- Displays ATS analysis.
- Shows AI agent execution status.

---

# 🤖 AI Agents

The project consists of the following AI agents:

- 📄 Resume Analysis Agent
- 🎯 Career Match Agent
- ⭐ ATS Score Agent
- 🛠 Skill Gap Analysis Agent
- 🗺 Career Roadmap Agent
- 📚 Learning Recommendation Agent
- 💼 Job Recommendation Agent
- 📊 Dashboard Agent

---

# 🛠️ Technologies Used

## Programming Language
- Python

## Frontend
- Streamlit

## AI Model
- Groq API (Llama 3.3 70B Versatile)

## Python Libraries
- Streamlit
- Pandas
- PyPDF
- Matplotlib
- python-dotenv
- Groq SDK

## Data Sources
- Resume PDF Files
- CSV Datasets (`courses.csv`, `jobs.csv`)

---

# 📂 Project Structure

```text
CareerPilot-AI/
│
├── agents/
│   ├── career/
│   ├── learning/
│   ├── resume/
│   └── jobs/
│
├── pages/
│   ├── 1_Resume_Intelligence.py
│   ├── 2_Career_Guidance.py
│   ├── 3_Learning.py
│   ├── 4_Jobs.py
│   └── 5_Dashboard.py
│
├── data/
│   ├── courses.csv
│   └── jobs.csv
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 📋 Workflow

1. Upload a Resume (PDF).
2. Resume Analysis Agent extracts resume information.
3. ATS Score is calculated.
4. Career Match is identified.
5. Skill Gap Analysis is performed.
6. Career Roadmap is generated.
7. Learning resources are recommended.
8. Suitable jobs are suggested.
9. Dashboard summarizes the complete career analysis.

---

# 📸 Application Modules

- 🏠 Home
- 📄 Resume Intelligence
- 🎯 Career Guidance
- 📚 Learning Resources
- 💼 Job Recommendations

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/DheydeepyaKCN/CareerPilot-AI.git
```

Navigate to the project folder:

```bash
cd CareerPilot-AI
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key:

```text
GROQ_API_KEY=your_groq_api_key_here
```

## 🚀 Run the Application

```bash
python -m streamlit run streamlit_app.py
```

Alternatively, if Streamlit is available in your PATH:

```bash
streamlit run streamlit_app.py
```
---

# 🎯 Future Enhancements

- AI Interview Preparation
- Resume ATS Optimization
- Cover Letter Generation
- Live Job Portal Integration
- User Authentication
- Cloud Deployment
- Progress Tracking Dashboard

---

# 👥 Team Members

- Haseena Rahaman
- K. C. N. Dheydeepya
- Reddi Lahari
- Bammidi Lahari

---

# 🙏 Acknowledgements

- Groq
- Llama 3.3
- Streamlit
- Python Community
- Open Source Libraries

---

# 📜 License

This project is developed for academic and educational purposes as part of the **Google AI Agents Capstone Project**.