import streamlit as st

st.set_page_config(page_title="AI Portfolio",layout="wide")

# Sidebar
st.sidebar.title("Madhavi Manikala")
st.sidebar.write("AI/ML Engineer")

st.sidebar.info("""
Skills:
- Python
- SQL
- Machine Learning
- AI
""")

# Main Title
st.title("🚀 AI Resume Dashboard")

st.subheader("Madhavi Manikala")
st.write("Python | SQL | Machine Learning | AI")

# About
st.write("### About Me")
st.write("""
Aspiring AI/ML Engineer passionate about Machine Learning,
Computer Vision, and Data Analysis.
""")

# Skills
st.write("## Skills")

st.progress(90,text="Python")
st.progress(85,text="SQL")
st.progress(80,text="Machine Learning")
st.progress(75,text="Artificial Intelligence")

# Projects
st.write("## Projects")

col1,col2 = st.columns(2)

with col1:
    st.success("Predictive Maintenance with Explainable AI")
    st.success("House Price Prediction")

with col2:
    st.success("Computer Vision for Visual Quality Control")
    st.success("Automatic E-Governance using AI")

# Contact
st.write("## Contact")

st.write("📧 madhavimanikala060@gmail.com")
st.write("📍 Hyderabad")