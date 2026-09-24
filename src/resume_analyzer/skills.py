def extract_skills(text):

    skills = [
        "Python",
        "Java",
        "C++",
        "C",
        "HTML",
        "CSS",
        "JavaScript",
        "SQL",
        "Git",
        "GitHub",
        "Machine Learning",
        "Deep Learning",
        "React",
        "Node.js",
        "MongoDB",
        "MySQL",
        "Django",
        "Flask"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills
