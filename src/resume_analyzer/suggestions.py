def generate_suggestions(breakdown, word_count):

    suggestions = []

    if breakdown["Certifications"] == 0:
        suggestions.append(
            "Consider adding relevant certifications to strengthen your resume."
        )

    if breakdown["Skills"] < 20:
        suggestions.append(
            "Consider adding more relevant technical skills to your resume."
        )

    if word_count < 300:
        suggestions.append(
            "Your resume is quite concise. Consider adding more detail to your projects or achievements."
        )
        if breakdown["Experience"] == 0:
         suggestions.append(
            "Consider adding relevant internships, work experience, or practical experience to your resume."
        )
         if breakdown["Projects"] == 0:
          suggestions.append(
        "Add 1–2 relevant projects and describe your contribution and technologies used."
    )



    return suggestions


