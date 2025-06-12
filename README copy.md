![logo_ironhack_blue](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Project NLP | Business Case: Automated Customer Reviews

## Project Goal

This project aims to develop a product review system powered by NLP models that aggregate customer feedback from different sources. The key tasks include classifying reviews, clustering product categories, and using generative AI to summarize reviews into recommendation articles.

## Problem Statement

With thousands of reviews available across multiple platforms, manually analyzing them is inefficient. This project seeks to automate the process using NLP models to extract insights and provide users with valuable product recommendations.

## Main Tasks

### 1. Review Classification
   - **Objective**: Classify customer reviews into **positive**, **negative**, or **neutral** categories to help the company improve its products and services.
   - **Task**: Create a model for classifying the **textual content** of reviews into these three categories.

####  Mapping Star Ratings to Sentiment Classes  
Since the dataset contains **star ratings (1 to 5)**, you should map them to three sentiment classes as follows:  

| **Star Rating** | **Sentiment Class** |
|---------------|------------------|
|  1 - 2     | **Negative**  |
|  3         | **Neutral**  |
|  4 - 5     | **Positive**  |

 This is a simple approach, but you are encouraged to experiment with different mappings! 


**Model Building**

For classifying customer reviews into **positive, negative, or neutral**, use **pretrained transformer-based models** to leverage powerful language representations without training from scratch.  

#### Suggested Models  
- **`distilbert-base-uncased`** – Lightweight and fast, ideal for limited resources.  
- **`bert-base-uncased`** – A strong general-purpose model for sentiment analysis.  
- **`roberta-base`** – More robust to nuanced sentiment variations.  
- **`nlptown/bert-base-multilingual-uncased-sentiment`** – Handles multiple languages, useful for diverse datasets.  
- **`cardiffnlp/twitter-roberta-base-sentiment`** – Optimized for short texts like social media reviews.  

Explore models on [Hugging Face](https://huggingface.co/models) and experiment with fine-tuning to improve accuracy.

### Model Evaluation

#### Evaluation Metrics

- Evaluated the model's performance on a separate test dataset using various evaluation metrics:
  - Accuracy: Percentage of correctly classified instances.
  - Precision: Proportion of true positive predictions among all positive predictions.
  - Recall: Proportion of true positive predictions among all actual positive instances.
  - F1-score: Harmonic mean of precision and recall.
- Calculated confusion matrix to analyze model's performance across different classes.

####  Results

- Model achieved an accuracy of X% on the test dataset.
 - Precision, recall, and F1-score for each class are as follows:
 - Class 1: Precision=X%, Recall=X%, F1-score=X%
 - Class 2: Precision=X%, Recall=X%, F1-score=X%
 - ...
- Confusion matrix showing table and graphical representations


### 2. Product Category Clustering
   - **Objective**: Simplify the dataset by clustering product categories into **4-6 meta-categories**.
   - **Task**: Create a model to group all reviews into 4-6 broader categories. Example suggestions:
     - Ebook readers
     - Batteries
     - Accessories (keyboards, laptop stands, etc.)
     - Non-electronics (Nespresso pods, pet carriers, etc.)
   - **Note**: Analyze the dataset in depth to determine the most appropriate categories.

### 3. Review Summarization Using Generative AI
   - **Objective**: Summarize reviews into articles that recommend the top products for each category.
   - **Task**: Create a model that generates a short article (like a blog post) for each product category. The output should include:
     - **Top 3 products** and key differences between them.
     - **Top complaints** for each of those products.
     - **Worst product** in the category and why it should be avoided.

     Consider using **Pretrained Generative Models** like **T5**, **GPT-3**, or **BART** for generating coherent and well-structured summaries. These models excel at tasks like summarization and text generation, and can be fine-tuned to produce high-quality outputs based on the extracted insights from reviews. 
     You are encouraged to explore other **Transformer-based models** available on platforms like **Hugging Face**. Fine-tuning any of these pre-trained models on your specific dataset could further improve the relevance and quality of the generated summaries.

## Datasets

- **Primary Dataset**: [Amazon Product Reviews](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products/data)
- **Larger Dataset**: [Amazon Reviews Dataset](https://cseweb.ucsd.edu/~jmcauley/datasets.html#amazon_reviews)
- **Additional Datasets**: You are free to use other datasets from sources like HuggingFace, Kaggle, or any other platform.

<!-- ## Deployment -->

<!-- - **Hosting**: You are free to host the models on your laptop or any cloud platform.
- **Framework**: You can use any framework of your choice (e.g., Gradio, AWS, etc.).

- **Options**:
  - List the models on HuggingFace.
  - Deploy a text file with the final results.
  - Create a website that displays the final results.
  - Build a live review aggregator.
  - Develop a website that generates recommendations by uploading a file with reviews.

- **Inspiration**: Look at websites like Consumer Reviews, The Verge, or The Wirecutter for ideas. -->


## Deployment Guidelines

### Expectations

- You are expected to showcase a webpage or web app in which some simple user interactions are possible (for example through buttons, text boxes, sliders, ...).
- All your three components (classification, clustering, and text summarizer) should be visible or possible to interact with on the page in some form.
- You are free to host the models on your laptop or any cloud platform (e.g., Gradio, AWS, etc.).

We provide you with some ideas below. However, you are not limited to these options. Feel free to build a web app or website that does different things to what listed below.

1. **Create a website for the marketing department in your company**, who needs to gain insights on how well the products are received by customers (from reviews) and what other competitive products exist in the market.  For example, users in your webpage can choose between product categories and be shown statistics insights (distribution of ratings, best product ratings, etc), and text summarization for that specific category (which are the best product in this category, etc).
2. **Build a live review aggregator**: this could be a website like, for example, https://www.trustpilot.com/ or https://www.yelp.com/, organizing reviews strategically for buyers. You could add functionality for users to add reviews (for example, through a form, a user could write about a product, selecting which cluster category it belongs to and the rating given). Once a review is submitted, it could be displayed on the page as a ‘recently added review’. Feel free to come up with your own ideas about how you would like your live review aggregator to look like and behave
3. **Develop a website that generates recommendations by allowing users to upload a csv file with reviews**. For example, this website could allow business owners to upload a dataset of their products and respective reviews. Your website would process these, classifying them, clustering them, and showing insights in the form of small articles listing top products, main product issues, etc., for example (e.g., a list of articles, one per product; a list of articles, one per cluster).
4. **Develop a website that allows users to search for information about a product or product category through a text box**. This could be a text box where users type in what they are looking for / would like to buy. The output could display recommendations of products in text summary format, the category of the product, and the sentiment distribution for that product.

## Deliverables

1. **Source Code**:
   - Well-organized and linted code (use tools like `pylint`).
   - Notebooks should be structured with clear headers/sections.
   - Alternatively, provide plain Python files with a `main()` function.
2. **README**:
   - A detailed README file explaining how to run the code and reproduce the results.
3. **Final Output**:
   - Generated blog posts with product recommendations.
   - A website, text file, or Word document containing the final results.
4. **PPT Presentation**:
   - A presentation (no more than 15 minutes) tailored for both technical and non-technical audiences.
5. **Deployed Model**:
   - A deployed web app using the framework of your choice.
   - Bonus: Host the app so it can be queried by anyone.

## Evaluation Criteria

| **Task**                              | **Points** |
|---------------------------------------|------------|
| Data Preprocessing                    | 15         |
| Model for Review Classification       | 20         |
| Clustering Model                      | 20         |
| Summarization Model                   | 20         |
| Deployment of the Model               | 10         |
| PDF Report (Approach, Results, Analysis) | 5          |
| PPT Presentation                      | 10         |
| **Bonus**: Hosting the App Publicly   | 10         |

**Passing Score**: 70 points.

## Additional Notes

- **Teamwork**: Work in groups of no more than 3 people. If necessary, one group may have 4 members.
- **Presentation**: Tailor your presentation for both technical and non-technical audiences. Refer to the "Create Presentation" guidelines in the Student Portal.

## Suggested Workflow

1. **Data Collection**: Gather and preprocess the dataset(s).
2. **Model Development**:
   - Build and evaluate the review classification model.
   - Develop and test the clustering model.
   - Create the summarization model using Generative AI.
3. **Deployment**: Deploy the models using your chosen framework.
4. **Documentation**: Prepare the README, PDF report, and PPT presentation.
5. **Final Delivery**: Submit all deliverables, including the deployed app and final output.




### Comparison of T5 and BART Models

**T5 (Text-to-Text Transfer Transformer):**
- Generates concise summaries but sometimes omits nuanced details.
- Summaries are more extractive and may sound less natural.
- Handles short reviews well, but longer or complex reviews may lose context.
- Tends to focus on key phrases but can be repetitive for similar inputs.
- Faster inference for small models (e.g., `t5-small`).

**BART (Bidirectional and Auto-Regressive Transformers):**
- Produces more fluent, human-like summaries.
- Better at capturing the main point, even in longer or complex reviews.
- Summaries are often more abstractive and readable.
- Handles negative reviews and complaint extraction with clearer language.
- Larger models (e.g., `bart-large-cnn`) may require more resources but yield higher quality.

**Summary Table:**

| Aspect                | T5 Model                  | BART Model                  |
|-----------------------|---------------------------|-----------------------------|
| Summary Style         | Concise, extractive       | Fluent, abstractive         |
| Detail Retention      | May omit nuances          | Captures more context       |
| Language Naturalness  | Less natural              | More human-like             |
| Handling Long Reviews | May lose context          | Handles well                |
| Resource Usage        | Lower (small models)      | Higher (large models)       |
| Complaint Extraction  | Clear, but less nuanced   | Clear and more readable     |

**Conclusion:**  
BART generally produces more natural and context-aware summaries, especially for longer or more complex reviews. T5 is efficient and effective for shorter texts or when computational resources are limited. For customer review summarization at scale, BART is preferred for quality, while T5 is suitable for speed and simplicity.