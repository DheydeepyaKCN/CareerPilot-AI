def calculate_readiness(candidate):

    ats = candidate["ats_score"]["score"]
    match = candidate["career_match"]["match_score"]

    experience = candidate["resume_analysis"]["experience_years"]

    missing_skills = len(candidate["skill_gap"]["missing_skills"])

    # ---------------------------
    # Experience Score
    # ---------------------------

    if experience >= 5:
        exp_score = 100
    elif experience >= 3:
        exp_score = 80
    elif experience >= 1:
        exp_score = 60
    else:
        exp_score = 40

    # ---------------------------
    # Skill Gap Score
    # ---------------------------

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

    # ---------------------------
    # Final Weighted Score
    # ---------------------------

    final_score = (
        ats * 0.30 +
        match * 0.30 +
        gap_score * 0.25 +
        exp_score * 0.15
    )

    return round(final_score)