import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize

def tokenize_text(text):
    """Memecah teks menjadi potongan kecil (token)"""
    return {
        "sentences": sent_tokenize(text),
        "words": word_tokenize(text)
    }

# Contoh teks artikel pendek tentang AI
sample_text = "Natural Language Processing (NLP) is a fascinating AI field. Key techniques include: tokenization, stemming, and lemmatization. Let's explore more!"

print("Original Text:")
print(sample_text)

tokens = tokenize_text(sample_text)

print("\nSentence Tokens:")
for i, sentence in enumerate(tokens["sentences"], 1):
    print(f"{i}. {sentence}")

print("\nWord Tokens:")
print(tokens["words"])

"""
Output yang diharapkan:

Original Text: Natural Language Processing (NLP) is a fascinating AI field. Key techniques include: tokenization, stemming, and lemmatization. Let's explore more!

Sentence Tokens:
1. Natural Language Processing (NLP) is a fascinating AI field.
2. Key techniques include: tokenization, stemming, and lemmatization.
3. Let's explore more!

Word Tokens: ['Natural', 'Language', 'Processing', '(', 'NLP', ')', 'is', ...]
"""