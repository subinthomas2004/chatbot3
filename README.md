# ✉️ AI Professional Email Generator

An interactive web application built with **Streamlit** and **Ollama** (`tinyllama:latest`) that generates professional, customized emails based on recipient, purpose, tone, and key discussion points.

---

## 🚀 Features

- **Intuitive Web UI**: Built with Streamlit for quick and clean interactions.
- **Tone Customization**: Choose between Professional, Formal, Friendly, Direct, Persuasive, Urgent, or define custom tones.
- **Local & Private**: Powered by local LLMs via Ollama—no API keys required, your data stays on your machine.
- **Download & Export**: Easily download generated emails as text files.
- **Model Flexibility**: Defaults to `tinyllama:latest`, but configurable in the sidebar to any local Ollama model (e.g., `llama3`, `mistral`, `phi3`).

---

## 📋 Prerequisites

1. **Python 3.9+** installed on your system.
2. **Ollama**:
   - Download and install from [ollama.com](https://ollama.com).
   - Pull the TinyLlama model:
     ```bash
     ollama run tinyllama
     ```
   - Ensure Ollama is running (`ollama serve` or via system tray).

---

## 🛠️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <repository-directory>
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Application

Launch the Streamlit app:
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 📤 Pushing to GitHub

If you are initializing a new repository to push to your GitHub account:

```bash
git init
git add .
git commit -m "Initial commit: Streamlit email generator app with Ollama"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```
