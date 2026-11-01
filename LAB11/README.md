# LAB11 — Attention with RNN

## Overview
Train a small PyTorch RNN with attention on the provided question-and-answer dataset.

## Completed Tasks
- Task 1: Plot attention for three different questions and print the highest-weight word.
- Task 2: Compare two similar questions about breathing and their attention weights.

## Files
- `Lab_11_Attention_with_RNN.ipynb`
- `dataset/Lab_11_QnA_Dataset.csv`

## Run
Use Jupyter or Colab with `pandas`, `torch`, `tensorflow`, and `matplotlib`. Run the notebook from its LAB11 folder or the repository root. The dataset is included, and Colab can fetch the same CSV from this GitHub repository if it is not on the local runtime. The RNN uses batch-first sequences and ignores padding positions in the attention scores.
