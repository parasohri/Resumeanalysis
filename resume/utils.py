from PyPDF2 import PdfReader
from google import genai
from django.conf import settings
import json
import re


# ---------------- PDF TEXT EXTRACTION ----------------
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    file.close()
    return text


# ---------------- GEMINI CLIENT (NEW SDK) ----------------
client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


# ---------------- RESUME ANALYSIS ----------------
def analyze_resume_with_ai(resume_text: str, job_description: str):
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
- Technical questions
- Project-based questions
- Behavioral questions
- Gap-focused questions

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

Do NOT include explanations, markdown, or extra text.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
        )

        raw_text = response.text.strip()

        # Clean ```json wrappers if Gemini adds them
        cleaned = re.sub(r"```json|```", "", raw_text).strip()

        return json.loads(cleaned)

    except json.JSONDecodeError:
        return {
            "error": "AI response parsing failed",
            "raw_response": raw_text
        }

    except Exception as e:
        return {
            "error": "Gemini service failed",
            "details": str(e)
        }
