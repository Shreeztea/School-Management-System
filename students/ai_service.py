import os
from google import genai

def ask_ai(question):
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question,
    )

    return response.text