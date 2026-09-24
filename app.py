import streamlit as st

from src.resume_analyzer.parser import extract_text_from_pdf
from src.resume_analyzer.analyzer import analyze_resume
from src.resume_analyzer.skills import extract_skills
from src.resume_analyzer.scorer import calculate_score
from src.resume_analyzer.suggestions import generate_suggestions


st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract text from PDF
    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Resume Text")

    st.text_area(
        "Extracted text:",
        resume_text,
        height=400
    )

    # Analyze resume
    analysis = analyze_resume(resume_text)

    st.subheader("Resume Analysis")

    st.write("Word Count:", analysis["word_count"])

    if analysis["has_email"]:
        st.write("✅ Email found")
    else:
        st.write("❌ Email not found")

    if analysis["has_phone"]:
        st.write("✅ Phone number found")
    else:
        st.write("❌ Phone number not found")

    # Extract skills
    skills = extract_skills(resume_text)

    st.subheader("Skills Detected")

    if skills:
        st.write(", ".join(skills))
    else:
        st.write("No skills detected.")

    # Calculate score
    score, breakdown = calculate_score(resume_text, skills)

    # Generate suggestions
    suggestions = generate_suggestions(breakdown,analysis["word_count"])

    st.subheader("Resume Score")

    st.write(f"🎯 Your Resume Score: {score}/90")

    # Score breakdown
    st.subheader("📊 Score Breakdown")

    for category, points in breakdown.items():
        st.write(f"{category}: {points}")

    # Suggestions
    st.subheader("💡 Suggestions")

    for suggestion in suggestions:
        st.warning(suggestion)