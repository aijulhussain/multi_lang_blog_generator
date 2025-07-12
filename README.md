Built with:
- 🧠 **Groq LLM** (LLaMA 3.1 8B)
- ⚙️ **FastAPI** for backend API
- 🔗 **LangGraph** for workflow orchestration
- 🎨 **Streamlit** for frontend UI

---

## 📸 Demo

![Streamlit App Screenshot](./blog_generation(diff_lang).png)

---

## 🚀 Features

- Multi language blog generator(Hindi+French+Assamese) by defauilt English language
- Generate SEO-optimized blog titles and long-form content from a topic
- Interactive Streamlit UI

- Built-in LLM workflow using LangGraph + Groq



## 📦 Installation (Run Locally)

```bash
git clone https://github.com/aijulhussain/Agentic_Blog_Generator.git
.venv\Scripts\activate
uv add -r requirements.txt
uvicorn app:app --reload
open another powershell and run: streamlit run streamlit_app.py


