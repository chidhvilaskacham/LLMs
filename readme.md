# 🐳 LLM-based Dockerfile Generator

This repository explores Large Language Models (LLMs) with a focus on practical applications and prompt engineering techniques.  It provides Python code examples and resources to demonstrate how to effectively interact with LLMs for various tasks.

---

## 📦 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/download) installed and running locally
- Git (optional, for cloning)

---

**Key Features:**

* **Prompt Engineering Examples:** The repository includes diverse examples demonstrating different prompt engineering strategies, including zero-shot, few-shot, and chain-of-thought prompting.  These examples illustrate how to craft effective prompts for tasks like text summarization, question answering, code generation, and creative writing.

* **LLM Interaction Code:** Python scripts demonstrate how to use popular LLM APIs (e.g., OpenAI) to send prompts and receive generated text.  The code provides a clear and concise way to understand the basic mechanics of interacting with LLMs programmatically.

* **Practical Applications:** The repository focuses on applying LLMs to real-world scenarios.  Examples may include automating tasks, generating creative content, building chatbots, or extracting insights from text data.

## ⚙️ Installing Ollama

1. **Download and install Ollama** from the [official site](https://ollama.com/download).
2. Once installed, verify it's by pulling the model:

   ```bash
   ollama pull llama3.2:1b
   ```

## 🚀 Project Setup

1. Set up a Python virtual environment (optional but recommended):
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

2. Install required packages:
```bash
pip install -r requirements.txt
```
3. Run the Application
```bash
python generate_dockerfile.py
```
## 🧠 How It Works
1. You provide the name of a programming language (e.g., java, python, go, etc.).
2. The script sends a prompt to a local LLM via the ollama Python API.
3. The LLM returns a Dockerfile suitable for that language.
4. The Dockerfile content is printed to the console.

## 💻 Example Usage

Run the script:

```bash
python generate_dockerfile.py
Enter a Programming Language: java
Generated Dockerfile:
#....
``` 
