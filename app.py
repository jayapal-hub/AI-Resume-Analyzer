import streamlit as st

from src.resume_analyzer.parser import extract_text_from_pdf
from src.resume_analyzer.analyzer import analyze_resume
from src.resume_analyzer.skills import extract_skills
from src.resume_analyzer.scorer import calculate_score
from src.resume_analyzer.suggestions import generate_suggestions

from src.resume_analyzer.job_matcher import (
    extract_job_skills,
    compare_skills,
    calculate_job_match_score,
    categorize_missing_skills
)


st.title("AI Resume Analyzer")


uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)


job_description = st.text_area(
    "Paste the Job Description",
    height=250,
    placeholder="Paste the job description here..."
)


if job_description:

    job_skills = extract_job_skills(job_description)

    st.subheader("Job Skills Detected")

    if job_skills:
        st.write(", ".join(job_skills))
    else:
        st.write("No technical skills detected.")


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

    # Extract resume skills
    skills = extract_skills(resume_text)

    st.subheader("Skills Detected")

    if skills:
        st.write(", ".join(skills))
    else:
        st.write("No skills detected.")

    # Job Match Analysis
    if job_description:

        matched_skills, missing_skills = compare_skills(
            skills,
            job_skills
        )

        job_match_score = calculate_job_match_score(
            matched_skills,
            job_skills
        )

        missing_skill_categories = categorize_missing_skills(
            missing_skills
        )

        st.subheader("🎯 Job Match Analysis")

        st.metric(
            "Job Match Score",
            f"{job_match_score}%"
        )

        st.write("Matched Skills:")

        if matched_skills:
            st.success(", ".join(matched_skills))
        else:
            st.write("No matching skills found.")

        st.write("Missing Skills:")

        if missing_skills:
            st.warning(", ".join(missing_skills))
        else:
            st.success("No missing skills!")

        # Skill Gap Analysis
        st.subheader("🎯 Skill Gap Analysis")

        for category, skills_list in missing_skill_categories.items():

            if skills_list:

                st.write(f"**{category}**")

                st.warning(", ".join(skills_list))

    # Calculate score
    score, breakdown = calculate_score(
        resume_text,
        skills
    )

    # Generate suggestions
    suggestions = generate_suggestions(
        breakdown,
        analysis["word_count"]
    )

    st.subheader("Resume Score")

    st.write(
        f"🎯 Your Resume Score: {score}/90"
    )

    # Score breakdown
    st.subheader("📊 Score Breakdown")

    for category, points in breakdown.items():

        st.write(
            f"{category}: {points}"
        )

    # Suggestions
    st.subheader("💡 Suggestions")

    for suggestion in suggestions:

        st.warning(suggestion)