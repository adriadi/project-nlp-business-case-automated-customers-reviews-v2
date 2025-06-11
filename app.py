import streamlit as st
from map_sentiments import predict_sentiment
from t5_model import summarize_with_t5
from visualize_pca import run_clustering  

from modules.classify import classify_text
from modules.summarize import summarize_text
from modules.cluster import run_clustering_interface


st.title("📊 Review Insight Dashboard")

tab1, tab2, tab3 = st.tabs(["💬 Classify Review", "📚 Summarize Text", "🔍 Clustering"])

with tab1:
    st.header("Review Classification")
    user_input = st.text_area("Enter a review:")
    if st.button("Classify"):
        sentiment = predict_sentiment([user_input])[0]
        st.write(f"**Sentiment:** {sentiment}")

with tab2:
    st.header("Summarize Product Reviews")
    user_input = st.text_area("Paste text to summarize:")
    if st.button("Summarize"):
        summary = summarize_with_t5(user_input)
        st.write(f"**Summary:** {summary}")

with tab3:
    st.header("Upload Review CSV for Clustering")
    run_clustering()

