from readiness_agent import readiness_agent
import json

candidate = {

    "resume_analysis":{

        "skills":[
            "Python",
            "SQL",
            "Pandas"
        ],

        "experience_years":1

    },

    "career_match":{

        "target_role":"Data Analyst",

        "match_score":82

    },

    "ats_score":{

        "score":76

    },

    "skill_gap":{

        "missing_skills":[

            "Power BI",

            "Statistics",

            "Excel"

        ]

    }

}

result = readiness_agent(candidate)

print(json.dumps(result,indent=4))