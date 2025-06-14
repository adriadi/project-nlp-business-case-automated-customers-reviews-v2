# modules/cluster.py

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from scripts.visualize_pca import visualize_pca
from utils.text_cleaning import clean_text  # cleaning function


def run_clustering_interface():
    """
    Streamlit UI: Upload CSV → clean reviews → run PCA visualization. 
    """
    st.subheader("🔍 Cluster Reviews with PCA")

    uploaded_file = st.file_uploader("Upload a CSV file with 'reviews.text' and 'reviews.rating' columns", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        if "reviews.text" not in df.columns or "reviews.rating" not in df.columns:
            st.error("❌ CSV must contain 'reviews.text' and 'reviews.rating' columns.")
            return

        # Clean the review texts
        df["cleaned_text"] = df["reviews.text"].astype(str).apply(clean_text)

        st.success("✅ Reviews loaded and cleaned!")

        # This will display the chart using your existing function
        fig = visualize_pca(df)
        st.pyplot(fig)  # Streamlit captures the current figure
