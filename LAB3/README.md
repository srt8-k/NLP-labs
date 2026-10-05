# LAB3 — N-gram Language Models

## Overview

This lab introduces N-gram language models and Maximum Likelihood Estimation (MLE). It applies a bigram language model to tweet data and evaluates how well the model predicts text.

## Completed Work

The task includes:

- Loading a public dataset of tweets from Pakistan
- Cleaning tweets by removing:
  - RT markers
  - hashtags
  - URLs
  - mentions
  - emojis
- Tokenizing the cleaned tweets
- Building a **bigram MLE language model**
- Evaluating the language model
- Calculating a bigram probability for **"pakistan is"**
- Calculating perplexity for the requested example
- Generating text using the trained N-gram model

## Files

- `Lab3_N_Grams_ipynb.ipynb` — completed lab notebook

## Main Libraries

- NLTK
- pandas
- emoji
- kagglehub
- scikit-learn
- re

## Key Concepts

- N-grams
- Bigram models
- Maximum Likelihood Estimation
- Conditional probability
- Perplexity
- Text generation

## Run

Run the notebook from top to bottom. The tweet dataset is downloaded through `kagglehub`, and NLTK resources are downloaded automatically if required.
