
# 📄 AI Research Paper Simplifier + Visual Explainer


---
## 🚀 A powerful AI-powered tool to simplify complex research papers for students, researchers, and lifelong learners.

## 🎯 Features

### ✅ Basic Functionality

- 📄 **Upload Research Paper (PDF)**
  - Parses and splits into sections (Abstract, Intro, Method, Conclusion)

- 🧠 **Layman-Friendly Summary**
  - Extracts & simplifies Abstract or Intro
  - Translates to Hindi / French (optional)

- 📘 **Glossary Generator**
  - Pulls 5–10 technical terms and explains them in plain English

- 🧭 **Methodology Flowchart**
  - Outputs flow as Mermaid.js flowchart (rendered)

- 🎯 **Use Case Generator**
  - Suggests 3 real-world applications for the research

---

### 🚀 Advanced Features

- ❓ **Custom Q&A**
  - Ask any question like “What dataset is used?” or “What are the limitations?”

- 🌐 **Multilingual Support**
  - Output summaries in English, Hindi, or French

- 🪄 **Mermaid.js Flowchart Generator**
  - Markdown-based visual of research methodology (`A → B → C`)

- 📋 **Download Report**
  - Get the simplified report as `.txt` with one click

---

## 🧪 How It Works

1. Upload a **PDF research paper**
2. Click buttons like **Simplify Paper**, **Glossary**, **Use Case Generator**
3. Ask **custom questions** about the paper
4. Download the full simplified report
---
Try it Out...🚀 [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR-STREAMLIT-APP-LINK)
---
## ⚙️ Tech Stack

- **Frontend:** Streamlit  
- **LLM Backend:** [Groq API](https://console.groq.com) + LangChain  
- **PDF Parsing:** PyMuPDF  
- **Translation:** Deep Translator  
- **Flowchart Rendering:** Mermaid.js (via Markdown)  
- **Deployment:** Streamlit Cloud (Free)

---

## 🧑‍💻 Local Setup

1. **Clone the Repo**

```bash
git clone https://github.com/YOUR_USERNAME/AI-Research-Navigator.git
cd AI-Research-Navigator
```

2. **Create Virtual Environment**

```bash
python -m venv .venv
source .venv/bin/activate  # For Windows: .venv\Scripts\activate
```

3. **Install Requirements**

```bash
pip install -r requirements.txt
```

4. **Add Environment Variable**

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_key_here
```

5. **Run App**

```bash
streamlit run main.py
```

---
## Author : [@Kurra-Srinivas](https://github.com/Kurra-Srinivas)
