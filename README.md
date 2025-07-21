#  ML Basics: Feature Vector Generator for Named Entity Recognition (NER)

This repository contains foundational code to help me understand how Natural Language Processing (NLP) models like Named Entity Recognition (NER) work inside.

###  File: `feature_vectors.py`

This script generates **feature vectors** for each word in a sentence. These vectors are used to train machine learning models like CRF, SVM, or LSTM for tasks like NER.

---

## Working

For each word in a sentence, it extracts:
-  Word itself
-  Lowercase form
-  Capitalization features
-  Prefixes & suffixes
-  Is it a number?
-  Is it punctuation?
- Previous & next word info
-  Part-of-speech (POS) tag *(using NLTK)*

---

## Dependencies

- Python 3.7+ (as usual)
- `nltk`

Install required packages:

```bash
pip install nltk


## Download NLTK resources
## if windows, try adding NLTK package address in the environment variable for the same name
## This fixed the nltk installation issues for me

import nltk
nltk.download('averaged_perceptron_tagger')

