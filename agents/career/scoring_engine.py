def calculate_readiness(candidate):
    """
    Calculates overall job readiness score.

    candidate should contain:
    {
        "ats_score": {"score":80},
        "career_match":{"match_score":80},
        "resume_analysis":{"experience_years":0},
        "skill_gap":{"missing_skills":[]}
    }
    """

    # -----------------------------
    # ATS Score
    # -----------------------------
    ats = candidate["ats_score"]["score"]

    # -----------------------------
    # Career Match Score
    # -----------------------------
    career_match = candidate["career_match"]

    # Support both old and new formats
    if "match_score" in career_match:
        match = career_match["match_score"]
    else:
        match = max(candidate["career_scores"].values())

    # -----------------------------
    # Experience
    # -----------------------------
    experience = candidate["resume_analysis"].get(
        "experience_years",
        0
    )

    # -----------------------------
    # Missing Skills
    # -----------------------------
    missing_skills = len(
        candidate["skill_gap"]["missing_skills"]
    )

    # -----------------------------
    # Experience Score
    # -----------------------------
    if experience >= 5:
        exp_score = 100
    elif experience >= 3:
        exp_score = 80
    elif experience >= 1:
        exp_score = 60
    else:
        exp_score = 40

    # -----------------------------
    # Skill Gap Score
    # -----------------------------
    if missing_skills == 0:
        gap_score = 100
    elif missing_skills <= 2:
        gap_score = 85
    elif missing_skills <= 4:
        gap_score = 70
    elif missing_skills <= 6:
        gap_score = 50
    else:
        gap_score = 30

    # -----------------------------
    # Final Score
    # -----------------------------
    final_score = (
        ats * 0.30
        + match * 0.30
        + gap_score * 0.25
        + exp_score * 0.15
    )

    return round(final_score)