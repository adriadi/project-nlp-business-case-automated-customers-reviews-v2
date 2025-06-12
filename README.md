---
title: Nlp Project
emoji: 💻
colorFrom: gray
colorTo: yellow
sdk: streamlit
sdk_version: 1.45.0
app_file: app.py
pinned: false
---


# 🤖 Automated Customer Review Analyzer (NLP Project)

A Natural Language Processing project that reads, understands, and summarizes product reviews — so you don’t have to.

This AI-powered tool classifies review sentiments, groups similar opinions, and generates short summaries to save users time and help businesses make smarter decisions.

---

## ✨ Features

- 🧼 **Data Preprocessing**  
  Clean and prepare review text by removing noise, filtering, and tokenizing.

- 😄 **Sentiment Classification**  
  Uses a fine-tuned RoBERTa model to classify reviews as **Negative**, **Neutral**, or **Positive**.

- 🧩 **Clustering**  
  Groups similar reviews using KMeans, then visualizes the clusters using **PCA** and **t-SNE**.

- ✂️ **Summarization**  
  Summarizes review clusters using **BART** and **T5** models for quick insights.

- 🌐 **Interactive App**  
  A simple Streamlit interface where you can input a review or product name and see:
  - Sentiment prediction
  - Summary of grouped reviews
  - Cluster visualization

---

## 📂 Project Structure

```
├── app.py                                  # Streamlit frontend for the project
├── modules
├────── classify.py                         # Sentiment classification logic using RoBERTa
├────── summarize.py                        # Handles summarization pipeline
├────── cluster.py                          # KMeans clustering on review embeddings
├── notebooks
├────── bart_model.ipynb                    # Summarizes reviews and analyzes products using BART model.
├────── main.ipynb                          # Loads, cleans, clusters, and analyzes customer review data.
├────── sentimental_classification.ipynb    # RoBERTa sentiment classification on Amazon reviews dataset.
├────── t5_model.ipynb                      # Summarizes and analyzes reviews using the T5 model.
├────── visualize_clusters.ipynb            # Visualizes and evaluates review clusters using t-SNE, PCA.
├── scripts
├────── bart_model.py                       # Load and run BART summarization model
├────── get_dataset.py                      # Load and explore the review dataset
├────── map_sentiments.py                   # Maps ratings and predicts sentiment using transformer models.
├────── t5_model.py                         # Load and run T5 summarization model
├────── test_functions-checkpoint.py        # Tests data loading and review preprocessing pipeline functions.
├────── test_functions.py                   # Unit tests and evaluation (confusion matrix, metrics)
├────── visualize_pca.py                    # PCA visualization
├────── visualize_tsne.py                   # t-SNE visualization
├── utils
├────── data_process.py                     # Preprocess the data to ease the development process
├────── metadata.py                         # Stores dataset column mappings & label definitions
├────── preprocessing_pipeline.py           # End-to-end data processing pipeline
├────── text_cleaning.py                    # Preprocessing logic: clean, tokenize, filter
├────── validate_clustering.py              # Clustering validation (e.g., Silhouette score)
```

---

## 🚀 How to Run It Locally

1. **Clone the repo**  
```bash
# Make sure git-lfs is installed (https://git-lfs.com)
git lfs install

git clone https://huggingface.co/spaces/Julseb42/nlp-project
cd nlp-project
```

2. **Create a virtual environment**  
```bash
python -m venv .venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Run the app**  
```bash
streamlit run app.py
```

---

## 🧠 Models Used

- [`cardiffnlp/twitter-roberta-base-sentiment`](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) – For sentiment classification
- [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn) – For review summarization
- [`t5-small`](https://huggingface.co/t5-small) – Alternative summarization model for concise outputs

---

## ✅ Requirements Covered

- Classify reviews into Positive, Neutral, Negative
- Group similar reviews using clustering
- Generate short summaries for each group
- Visualize insights with PCA and t-SNE
- Simple, user-friendly interface via Streamlit

---

## 📊 Sample Output

- Sentiment: **Positive**
- Summary: “Most users loved the product quality and found it easy to use.”
- Visual: [PCA/t-SNE plot of review clusters]

---

## 🎨 Made With

- Python 🐍
- Hugging Face Transformers 🤗
- scikit-learn 📊
- Streamlit/Huggin Face 🎛️
- Matplotlib & Seaborn 📉

---

## 👩‍💻 Authors

**Julien Sebag**
[Portfolio](https://julien-sebag.com/) | [LinkedIn](https://www.linkedin.com/in/julien-sebag/)

**Adrianna Dziadyk**
[Portfolio](https://www.adriannadziadyk.de) | [LinkedIn](https://www.linkedin.com/in/adziadyk/)

---

## 📝 License

MIT License — use it, remix it, just give credit.
