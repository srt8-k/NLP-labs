# LAB5 — Text Representation

## Overview

This lab explores different ways to represent and compare text numerically, from TF-IDF vectors to distributed Word2Vec embeddings.

## Completed Tasks

### Task 1 — Cosine Similarity
- Convert the provided documents into vectors
- Calculate pairwise cosine similarity
- Compare how similar the sentences are

### Task 2 — TF-IDF
- Build TF-IDF vectors for the provided sentences
- Display TF-IDF values
- Identify words with higher importance

### Task 3 — Word2Vec
- Load the Simpsons script dataset
- Clean the `spoken_words` column
- Tokenize the dialogue
- Train a skip-gram Word2Vec model using:
  - `vector_size=100`
  - `window=5`
  - `min_count=1`
  - `sg=1`

### Task 4 — Similar Words
Use `wv.most_similar()` for:

- homer
- marge
- bart

### Task 5 — Odd Word
Use `wv.doesnt_match()` to identify the word that does not belong in each requested group.

## Files

- `Lab5_Text_Representation-2.ipynb` — completed lab notebook
- `dataset/` — dataset information / runtime dataset location

## Main Libraries

- scikit-learn
- pandas
- gensim
- re

## Key Concepts

- Bag-of-words style vectorization
- TF-IDF
- Cosine similarity
- Word embeddings
- Word2Vec
- Skip-gram

## Run

Run the notebook from top to bottom. If the Simpsons dataset is not present locally, the notebook downloads the public lab copy automatically.
