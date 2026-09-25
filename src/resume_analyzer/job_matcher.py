def extract_job_skills(job_description):

    skills = []

    skill_list = [
        "python",
        "c++",
        "java",
        "sql",
        "mysql",
        "postgresql",
        "git",
        "github",
        "rest api",
        "django",
        "flask",
        "docker",
        "aws",
        "html",
        "css",
        "javascript",
        "react",
        "node.js"
    ]

    job_description = job_description.lower()

    for skill in skill_list:

        if skill in job_description:
            skills.append(skill)

    return skills


def compare_skills(resume_skills, job_skills):

    # Convert resume skills to lowercase
    resume_skills_lower = []

    for skill in resume_skills:
        resume_skills_lower.append(skill.lower())

    matched_skills = []
    missing_skills = []

    for skill in job_skills:

        if skill.lower() in resume_skills_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills


def calculate_job_match_score(matched_skills, job_skills):

    if len(job_skills) == 0:
        return 0

    score = (len(matched_skills) / len(job_skills)) * 100

    return round(score)