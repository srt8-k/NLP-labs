# LAB10 — Introduction to Machine Translation

## Overview
Practice English–French translation using an encoder–decoder LSTM.

## Completed Tasks
- Task 1: Short answers about Embedding, Encoder LSTM, Decoder LSTM, and softmax.
- Task 2: Download the specified English–French Kaggle dataset and train an encoder–decoder LSTM.
- Use teacher forcing so the decoder learns to predict the next French token.
- Evaluate token accuracy without counting padding, and print three actual test translations.

## Files
- `Lab10_Introduction_to_Machine_Translation-2.ipynb`

## Run
Use Jupyter or Google Colab with `tensorflow`, `numpy`, `pandas`, `scikit-learn`, and `kagglehub`. Run all cells and save the notebook with outputs. The dataset is downloaded from Kaggle at runtime. This exercise trains on 6,000 short sentence pairs. It shows token accuracy without counting padding, unknown-token frequency, and generated translations. The current output is still not reliable for real translation; it is a small educational LSTM, not a production translator.
