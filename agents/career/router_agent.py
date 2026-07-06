from agents.career.job_recommender import get_job_recommendations


def route_query(user_input):

    user_input = user_input.lower()

    if "job" in user_input or "placement" in user_input:
        return get_job_recommendations(user_input)

    return "No matching feature found"