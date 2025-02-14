import spacy

def perform_lemmatization(text):
    """Mengubah kata ke bentuk dasar linguistik"""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc])

sample_text = "The runners are running faster in the final races"

print("Original Text:")
print(sample_text)
lemmatized_text = perform_lemmatization(sample_text)
print("\nLemmatized Text:")
print(lemmatized_text)

"""
Output yang Diharapkan:

Original Text: The runners are running faster in the final races

Lemmatized Text: the runner be run fast in the final race
"""