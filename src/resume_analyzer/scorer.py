def calculate_score(text, skills):

    score = 0

    breakdown = {}

    # Contact information
    contact_score = 0

    if "@" in text:
        contact_score += 10

    if any(char.isdigit() for char in text):
        contact_score += 10

    score += contact_score
    breakdown["Contact Information"] = contact_score

    # Skills
    skills_score = 0

    if len(skills) >= 5:
        skills_score = 20
    elif len(skills) >= 3:
        skills_score = 15
    elif len(skills) >= 1:
        skills_score = 10

    score += skills_score
    breakdown["Skills"] = skills_score

    # Education
    education_score = 0

    if "education" in text.lower():
        education_score = 15

    score += education_score
    breakdown["Education"] = education_score

    # Experience
    experience_score = 0

    if "experience" in text.lower():
        experience_score = 15

    score += experience_score
    breakdown["Experience"] = experience_score

    # Projects
    projects_score = 0

    if "project" in text.lower():
        projects_score = 15

    score += projects_score
    breakdown["Projects"] = projects_score

    # Certifications
    certification_score = 0

    if "certification" in text.lower():
        certification_score = 5

    score += certification_score
    breakdown["Certifications"] = certification_score

    return score, breakdown