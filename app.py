import streamlit as st
from modules.classify import classify_text
from modules.summarize import summarize_text
from modules.cluster import run_clustering_interface

st.set_page_config(page_title="NLP Review App", layout="wide")
st.title("📊 NLP Review Insights")

tab1, tab2, tab3 = st.tabs(["💬 Classify Review", "📚 Summarize", "🔍 Clustering"])

with tab1:
    st.header("Classify a Review")
    text_input = st.text_area("Enter your review text:")
    if st.button("Classify"):
        result = classify_text(text_input)
        st.success(f"Sentiment: {result}")

with tab2:
    st.header("Summarize Review Text")
    summary_input = st.text_area("Paste long text to summarize:")
    model = st.radio("Choose a summarization model", ["t5", "bart"])
    if st.button("Summarize"):
        summary = summarize_text(summary_input, model)
        st.success(summary)

with tab3:
    st.header("Visualize Clusters")
    run_clustering_interface()
