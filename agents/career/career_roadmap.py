def generate_career_roadmap(user_input):
    """
    Input: dict with skills, interest, year
    Output: structured career roadmap
    """

    skills = user_input.get("skills", [])
    interest = user_input.get("interest", "").lower()
    year = user_input.get("year", "")

    roadmap = {
        "career_path": "",
        "steps": [],
        "skills_to_learn": [],
        "suggestion": ""
    }

    # -------------------------
    # LOGIC BLOCK 1: AI/ML path
    # -------------------------
    if "python" in skills and ("ai" in interest or "ml" in interest or "data" in interest):
        roadmap["career_path"] = "Data Scientist / ML Engineer"

        roadmap["steps"] = [
            "Learn Python deeply + OOP",
            "Master NumPy, Pandas, Matplotlib",
            "Study Machine Learning basics",
            "Learn Scikit-learn and models",
            "Build 3 real projects",
            "Learn Deep Learning (optional)",
            "Apply for internships"
        ]

        roadmap["skills_to_learn"] = [
            "Python Advanced",
            "Statistics",
            "Machine Learning",
            "Data Visualization",
            "SQL"
        ]

        roadmap["suggestion"] = "Focus on projects + Kaggle competitions"

    # -------------------------
    # LOGIC BLOCK 2: Web Dev
    # -------------------------
    elif "html" in skills or "css" in skills or "javascript" in skills:
        roadmap["career_path"] = "Full Stack Web Developer"

        roadmap["steps"] = [
            "Master HTML, CSS, JavaScript",
            "Learn React.js",
            "Backend: Node.js / Flask",
            "Build full stack projects",
            "Learn databases (MySQL/MongoDB)",
            "Deploy projects"
        ]

        roadmap["skills_to_learn"] = [
            "React",
            "Node.js",
            "Databases",
            "APIs"
        ]

        roadmap["suggestion"] = "Focus on building portfolio projects"

    # -------------------------
    # DEFAULT CASE
    # -------------------------
    else:
        roadmap["career_path"] = "Software Developer"

        roadmap["steps"] = [
            "Learn programming fundamentals",
            "Choose a language (Python/Java/C++)",
            "Learn DSA",
            "Build basic projects",
            "Practice coding problems"
        ]

        roadmap["skills_to_learn"] = [
            "Programming",
            "DSA",
            "Problem Solving"
        ]

        roadmap["suggestion"] = "Explore AI, Web Dev, or Data Science"

    return roadmap