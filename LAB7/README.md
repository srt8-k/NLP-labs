# LAB7 — Large Language Models

## Overview

This lab introduces the three main Transformer model families and shows how each architecture is suited to different NLP tasks.

## Transformer Families

- **Encoder-only** — classification, sentiment analysis and NER
- **Encoder–decoder** — translation, summarization and question answering
- **Decoder-only** — text generation, conversation and completion

## Completed Tasks

### Task 1 — Model Families

Select the most suitable Transformer family for:

- Sentiment classification
- Machine translation
- Open-ended text generation
- Named Entity Recognition
- Text summarization

### Task 2 — Encoder-only Model

Use a DistilBERT sentiment classifier on three provided sentences and print the predicted label and confidence score.

### Task 3 — Encoder–Decoder Model

Use **FLAN-T5-small** to summarize a short paragraph.

### Reflection

Explain why a decoder-only autoregressive model is suitable for conversational systems such as chatbots.

## Models Used

- `distilgpt2`
- `google/flan-t5-small`
- `distilbert-base-uncased-finetuned-sst-2-english`

## Files

- `Lab7_LLMs.ipynb` — completed lab notebook

## Main Libraries

- Hugging Face Transformers
- PyTorch
- SentencePiece

## Run

Run the notebook from top to bottom. The pretrained models are downloaded from Hugging Face when first used, so an internet connection is required.
