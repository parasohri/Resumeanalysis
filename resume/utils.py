from PyPDF2 import PdfReader
import google.generativeai as genai
from django.conf import settings
import json
import re
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    # Explicit cleanup
    file.close()

    return text
genai.configure(api_key=settings.GEMINI_API_KEY)


def analyze_resume_with_ai(resume_text: str, job_description: str):
    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    prompt = f"""
You are an expert ATS system and senior technical interviewer.

Analyze the resume against the job description and prepare interview insights.

Resume:
{resume_text}

Job Description:
{job_description}

Your tasks:
1. Calculate match percentage between resume and job description
2. Identify missing or weak skills
3. Identify strong points
4. Suggest improvements
5. Generate expected interview questions based on BOTH resume and job description

Interview questions must include:
- Technical questions (core skills, tools, frameworks)
- Project-based questions (from resume projects)
- Behavioral questions (teamwork, problem-solving)
- Gap-focused questions (missing or weak skills)

Return ONLY valid JSON in the following format:
{{
  "match_percentage": number,
  "missing_skills": [string],
  "strong_points": [string],
  "improvement_suggestions": [string],
  "expected_interview_questions": {{
    "technical": [string],
    "project_based": [string],
    "behavioral": [string],
    "gap_focused": [string]
  }}
}}

Do NOT include any explanations, markdown, or extra text.
"""


    response = model.generate_content(prompt)

    raw_text = response.text.strip()

    # 🔥 Gemini sometimes adds ```json ``` – clean it
    cleaned = re.sub(r"```json|```", "", raw_text).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "error": "AI response parsing failed",
            "raw_response": raw_text
        }
