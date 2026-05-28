import streamlit as st

# Page Config
st.set_page_config(
    page_title="AI Portfolio",
    page_icon="🚀",
    layout="wide"
)

# Sidebar
st.sidebar.title("👩‍💻 Madhavi Manikala")
st.sidebar.write("AI/ML Engineer")

st.sidebar.markdown("---")

st.sidebar.write("### Skills")
st.sidebar.write("✔ Python")
st.sidebar.write("✔ SQL")
st.sidebar.write("✔ Machine Learning")
st.sidebar.write("✔ Artificial Intelligence")

st.sidebar.markdown("---")

st.sidebar.write("📧 madhavimanikala060@gmail.com")
st.sidebar.write("📍 Hyderabad")

# Main Section
st.title("🚀 AI Resume Dashboard")

st.markdown("""
### Aspiring AI/ML Engineer

Passionate about Artificial Intelligence, Machine Learning,
Data Analysis, and Computer Vision.
""")

# Skills Section
st.write("## Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.write("### Programming")
    st.progress(90, text="Python")
    st.progress(85, text="SQL")

with col2:
    st.write("### AI Technologies")
    st.progress(80, text="Machine Learning")
    st.progress(75, text="Artificial Intelligence")

# Projects Section
st.write("## Projects")

project1, project2 = st.columns(2)

with project1:
    st.info("🔹 Predictive Maintenance with Explainable AI")
    st.info("🔹 House Price Prediction")

with project2:
    st.info("🔹 Computer Vision for Visual Quality Control")
    st.info("🔹 Automatic E-Governance using AI")

# Certifications
st.write("## Certifications")

st.success("🏅 Python Certification - HackerRank")
st.success("🏅 SQL Certification - HackerRank")
st.success("🏅 Full Stack Data Science with Agentic AI")

# Footer
st.markdown("---")

st.write("✨ Built using Python & Streamlit")