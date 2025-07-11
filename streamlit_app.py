import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit UI
st.set_page_config(page_title="Blog Generator Showcase", page_icon="✍️")
st.title("📝 AI Blog Generator")
st.markdown("---")

# Sidebar with app info
with st.sidebar:
    st.header("About This App")
    st.write("""
    This application showcases a blog generation system built with:
    - **FastAPI** for the backend
    - **LangGraph** for workflow orchestration
    - **Groq LLM** (Llama 3.1 8B) for content generation
    - **Streamlit** for the frontend
    """)
    
    st.markdown("---")
    st.write("Upload your own topic and see the AI generate a blog post!")

# Main app
def main():
    # Initialize session state
    if 'generated_blog' not in st.session_state:
        st.session_state.generated_blog = None
    
    # Input form
    with st.form("blog_form"):
        st.subheader("Enter Your Blog Topic")
        topic = st.text_input(
            "What topic would you like to generate a blog about?",
            placeholder="e.g., Artificial Intelligence in Healthcare"
        )
        
        submitted = st.form_submit_button("Generate Blog", type="primary")
        
        if submitted and topic:
            with st.spinner("Generating your blog... This may take a moment."):
                try:
                    # Call your FastAPI endpoint
                    response = requests.post(
                        "https://agentic-blog-generator-1.onrender.com/blogs",
                        json={"topic": topic}
                    )
                    
                    if response.status_code == 200:
                        st.session_state.generated_blog = response.json()["data"]
                        st.success("✅ Blog generated successfully!")
                    else:
                        st.error(f"❌ Error: {response.text}")
                        
                except requests.exceptions.ConnectionError:
                    st.error("❌ Could not connect to the backend API. Make sure your FastAPI app is running on port 8000.")
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")

    # Display generated blog if available
    if st.session_state.generated_blog:
        st.markdown("---")
        st.subheader("📄 Generated Blog")
        
        blog_data = st.session_state.generated_blog
        
        # Display title
        if 'blog' in blog_data and 'title' in blog_data['blog']:
            st.markdown(f"# {blog_data['blog']['title']}")
        
        # Display content
        if 'blog' in blog_data and 'content' in blog_data['blog']:
            st.markdown(blog_data['blog']['content'])
        
        # # Display raw data for debugging
        # with st.expander("🔍 View Raw Response"):
        #     st.json(blog_data)

if __name__ == "__main__":
    main()