# Sentiment Analysis on Mobile Reviews

## Overview
This project aims to perform sentiment analysis on mobile reviews using various machine learning techniques. The goal is to classify customer reviews as positive or negative, which can be useful for businesses to strategize and improve customer engagement.

**Publication**: International Journal of Computer Science Trends and Technology (IJCST) – Volume 9 Issue 3, May-Jun 2021  
**Authors**: Aditi Linge, Bhavya Malviya, Digvijay Raut, Payal Ekre  
**Institution**: Department of Information Technology, Government College of Engineering, Amravati, Maharashtra, India

## Introduction
Sentiment analysis is an automated process for understanding the emotions underlying a text. This project investigates whether sentiment analysis can be used to classify mobile reviews from customers into positive or negative categories. The analysis is conducted using various machine learning algorithms, and the results can help businesses refine their strategies based on customer feedback.

## Methodology

### Machine Learning Library
- **Jupyter Notebook**: Used to implement the machine learning algorithms.
- **Scientific Computing Libraries**: scikit-learn, numpy, matplotlib.

### Dataset
- **Source**: Kaggle, Amazon.com reviews.
- **Details**: The dataset includes 400,000 reviews of unlocked mobile phones with fields like Product Title, Brand, Price, Rating, and Review Text.

### Data Pre-processing
- Removed missing and duplicate data points.
- Classified reviews with ratings 1 and 2 as 'negative' and the remaining as 'positive'.
- Tokenized the reviews, built a vocabulary, and created a matrix for sentiment analysis.
- Used N-grams to capture language structure.

### Algorithms
1. **Support Vector Clustering (SVC)**: Maps data points to a high-dimensional space and forms cluster boundaries.
2. **Random Forest**: A supervised classification algorithm that creates a "forest" of decision trees.
3. **Logistic Regression**: Used for binary classification, implemented with count vectorizer, TF-IDF, and N-gram methods.

### Data Resampling
- The dataset was split into 75% training data and 25% testing data.
- Applied machine learning algorithms to the vectorized data.

## Results

### Model Accuracy Comparison

| Model                                  | Accuracy  |
|----------------------------------------|-----------|
| Random Forest Classifier               | 86.71%    |
| Logistic Regression (TF-IDF)           | 88.99%    |
| Logistic Regression (Count Vectorizer) | 89.74%    |
| Support Vector Clustering (SVC)        | 89.75%    |
| Logistic Regression (N-gram)           | 91.04%    |

Logistic regression with the N-gram method achieved the highest accuracy at 91.04%.

## Conclusion and Future Work
Logistic regression proved to be the most effective for sentiment analysis in this project. Future improvements could include training models on more comprehensive datasets and incorporating slang or evolving language trends. Additionally, experimenting with different algorithms could further enhance accuracy.

## Acknowledgment
The authors express their gratitude to Prof. B. V. Wakode, Department of Information Technology, Government College of Engineering, Amravati, for his guidance and support throughout the research.

## References
1. Pang, Lee, and Vaithyanathan. *Sentiment Classification Using Machine Learning Techniques*. ACL-02 Conference on Empirical Methods in Natural Language Processing, 2002.
2. [Sentiment Analysis for Amazon.com Reviews](https://www.researchgate.net/publication/332622380_SENTIMENT_ANALYSIS_FOR_AMAZONCOM_REVIEWS)
3. [Kaggle Dataset](https://www.kaggle.com/benroshan/sentiment-analysis-amazon-reviews)
4. [How Random Forest Algorithm Works](https://medium.com/@synced/how-random-forest-algorithm-works-in-machine-learning-3c0fe15b6674)
5. [Scikit-Learn](https://scikit-learn.org/stable/)
