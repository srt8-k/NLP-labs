# LAB4 — Classification and Evaluation

## Overview

This lab applies supervised machine learning to NLP text classification. The main assignment uses Amazon unlocked-mobile-phone reviews for sentiment classification.

## Completed Tasks

The notebook completes the required workflow:

1. Load the dataset
2. Apply five text preprocessing steps
3. Create a proper training/testing split
4. Convert text into TF-IDF features
5. Train a **Multinomial Naive Bayes** classifier
6. Evaluate predictions on the test set
7. Print accuracy and a classification report
8. Print the confusion matrix

Ratings are converted into three sentiment classes:

- Positive
- Neutral
- Negative

The notebook also contains the earlier Disneyland review classification example used in the lab material.

## Files

- `Lab4_Classification_and_evaluation.ipynb` — completed lab notebook

## Main Libraries

- pandas
- NLTK
- scikit-learn
- kagglehub
- re

## Key Concepts

- Text classification
- Text preprocessing
- TF-IDF
- Naive Bayes
- Train/test split
- Accuracy
- Precision, recall and F1-score
- Confusion matrix

## Run

Run the notebook from top to bottom. The Amazon review dataset is downloaded from Kaggle at runtime.
