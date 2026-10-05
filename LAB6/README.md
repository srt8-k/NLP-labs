# LAB6 — Deep Learning for NLP

## Overview

This lab applies deep learning to sentiment classification using Yelp restaurant reviews. It compares text representations and builds neural networks with PyTorch.

## Lab Workflow

The notebook first demonstrates a TF-IDF-based neural network and then completes the assigned Word2Vec tasks.

### Task 1 — Word2Vec Representation

- Tokenize training and testing reviews
- Train Word2Vec using only the training reviews
- Use the required settings:
  - `vector_size=200`
  - `window=5`
  - `min_count=1`
  - `sg=1`
- Represent each review using a single averaged Word2Vec vector
- Convert the vectors into PyTorch tensors

### Task 2 — Neural Network

Build a network with the required architecture:

```text
Input
  ↓
128
  ↓
64
  ↓
32
  ↓
1 Output
```

Training configuration:

- ReLU activations
- BCEWithLogitsLoss
- Adam optimizer
- Learning rate = 0.001
- 15 epochs

The final section evaluates the model using test accuracy.

## Files

- `Lab6_deep_learning_for_nlp-3.ipynb` — completed lab notebook
- `dataset/07-yelp-dataset.txt` — Yelp sentiment dataset

## Main Libraries

- pandas
- scikit-learn
- gensim
- NumPy
- PyTorch

## Run

Run the notebook from top to bottom. The local Yelp dataset is included under the `dataset` folder.
