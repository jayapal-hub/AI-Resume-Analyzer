def analyze_resume(text):
    analysis = {}

    analysis["word_count"] = len(text.split())

    analysis["has_email"] = "@" in text

    analysis["has_phone"] = any(char.isdigit() for char in text)

    return analysis