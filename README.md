# NLP Labs

This repository contains my Natural Language Processing (NLP) lab work. Each lab has its own folder with a Jupyter notebook, a short README, and any required dataset files when practical.

## Repository Structure

| Lab | Topic | Main Work |
| --- | --- | --- |
| [LAB1](./LAB1) | Introduction to NLP | Dataset selection, downloading, loading, and basic exploration |
| [LAB2](./LAB2) | Text Preprocessing & Regular Expressions | Hashtag analysis, regex, spaCy, and NLTK tokenization |
| [LAB3](./LAB3) | N-gram Language Models | Tweet preprocessing, bigram MLE, sentence probability, and perplexity |
| [LAB4](./LAB4) | Classification & Evaluation | Text preprocessing, TF-IDF, Naive Bayes, and evaluation metrics |
| [LAB5](./LAB5) | Text Representation | Cosine similarity, TF-IDF, and Word2Vec |
| [LAB6](./LAB6) | Deep Learning for NLP | TF-IDF and Word2Vec features with PyTorch neural networks |
| [LAB7](./LAB7) | Large Language Models | Transformer model families, sentiment classification, and summarization |
| [LAB8](./LAB8) | Part-of-Speech (POS) Tagging | NLTK and spaCy POS tagging, word usage, and dependency visualization |
| [LAB9](./LAB9) | Named Entity Recognition (NER) | Entity extraction, custom spaCy patterns, and training a small NER model |
| [LAB10](./LAB10) | Introduction to Machine Translation | English–French translation using an encoder–decoder LSTM |
| [LAB11](./LAB11) | Attention with RNN | Question classification, attention weights, and comparison of similar questions |
| [LAB12](./LAB12) | Transformers | DistilBERT example, BERT layer and head counts, and self-attention visualization |

## Tools and Libraries

The labs use Python and common NLP and machine-learning libraries:

- pandas and NumPy
- NLTK and spaCy
- scikit-learn and gensim
- PyTorch and TensorFlow
- Hugging Face Transformers
- Matplotlib
- kagglehub

The exact libraries depend on the lab. Check each lab's README and notebook for its requirements.

## Running the Labs

1. Open the folder for the lab you want to run.
2. Open the `.ipynb` notebook in **Jupyter Notebook** or **Google Colab**.
3. Install any missing packages and run the cells from top to bottom.

Some notebooks download datasets or pretrained models, so an internet connection may be needed. Training-based labs may also take longer to run.

## Dataset Notes

- **LAB10:** Downloads the English–French translation dataset from Kaggle at runtime.
- **LAB11:** Includes `dataset/Lab_11_QnA_Dataset.csv`. The notebook can also load the dataset from this GitHub repository when opened directly in Colab.
- Other labs include small data files when practical or download public datasets as needed.

## Course Material

These exercises are based on the NLP lab materials provided by **Dr. Mohammed Mosuily**. The task solutions are included in the corresponding notebooks.
