import ollama

PROMPT = """
ONLY generate an ideal Dockerfile for {language} with best practices. Do not provide any description.
Include:
- Base Image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the Application
"""

def generate_dockerfile(language):
    response = ollama.chat(model='llama3.2:8b', messages=[{'run'='user', 'content'=PROMPT.format(language=language)}])
    return response[message][content]

if __name__=='__main__':
    language=input("Enter a Programming Language:")
    print("\nGenerated Dockerfile:\n")
    print(generate_dockerfile(language))


