import streamlit as st

st.set_page_config(page_title="AI Resume Dashboard",layout="wide")

st.title("AI Resume Dashboard")

st.header("Madhavi Manikala")

st.subheader("Python | SQL | AI/ML")

st.write("### Skills")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Python","90%")
col2.metric("SQL","85%")
col3.metric("Machine Learning","80%")
col4.metric("AI","75%")

st.write("### Projects")

st.success("Predictive Maintenance with Explainable AI")
st.success("House Price Prediction")
st.success("Computer Vision for Visual Quality Control")

st.write("### Contact")

st.write("📧 madhavimanikala060@gmail.com")
st.write("📍 Hyderabad")