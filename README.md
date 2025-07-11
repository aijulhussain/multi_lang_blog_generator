Built with:
- 🧠 **Groq LLM** (LLaMA 3.1 8B)
- ⚙️ **FastAPI** for backend API
- 🔗 **LangGraph** for workflow orchestration
- 🎨 **Streamlit** for frontend UI

---

## 📸 Demo

![Streamlit App Screenshot](./blog_generation(topic).png)

---

## 🚀 Features

- Generate SEO-optimized blog titles and long-form content from a topic
- Interactive Streamlit UI
- API-based architecture for easy integration
- Built-in LLM workflow using LangGraph + Groq



## 📦 Installation (Run Locally)

```bash
git clone https://github.com/aijulhussain/Agentic_Blog_Generator.git
.venv\Scripts\activate
uv add -r requirements.txt
streamlit run streamlit_app.py


## Update streamlit_app.py with your public backend URL:
API_URL = "https://your-backend.onrender.com/blogs"
