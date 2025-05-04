# 🐳 LLM-based Dockerfile Generator with Ollama

This project uses a local Large Language Model (LLM) powered by [Ollama](https://ollama.com/) to generate Dockerfiles for different programming languages.

---

## 📦 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/download) installed and running locally
- Git (optional, for cloning)

---

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
