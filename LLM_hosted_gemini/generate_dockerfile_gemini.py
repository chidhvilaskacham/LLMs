import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = "XXXXXXXXXXXXXXXXXXXXXX"

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro')

PROMPT = """
ONLY generate ideal Dockerfile for {language} with best practices. Just share the Dockerfile without any explanation between two lines to make copying dockerfile easy.
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
- Multi stage build
"""

def generate_dockerfile(language):
    response = model.generate_content(PROMPT)
    return response.text

if __name__ == "__main__":
    language = input("Enter a Programming Language:")
    print(generate_dockerfile(language))


