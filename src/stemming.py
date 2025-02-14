from nltk.stem import PorterStemmer

def perform_stemming(text):
    """Mengurangi kata ke bentuk dasar"""
    stemmer = PorterStemmer()
    words = text.split()
    return ' '.join([stemmer.stem(word) for word in words])

sample_text = "running runner runs finally finalized finalization"

print("Original Text:")
print(sample_text)
stemmed_text = perform_stemming(sample_text)
print("\nStemmed Text:")
print(stemmed_text)

"""
Output yang diharapkan:

Original Text: running runner runs finally finalized finalization

Stemmed Text: run runner run final final final
"""