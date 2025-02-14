import string

def remove_punctuation(text):
    """Membersihkan teks dari tanda baca"""
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

sample_text = "Hello! This text contains: commas (,), periods (.), questions marks (?), and others! @2023 #NLP"

print("Original Text:")
print(sample_text)
clean_text = remove_punctuation(sample_text)
print("\nClean Text:")
print(clean_text)

"""
Output yang diharapkan:

Original Text: Hello! This text contains: commas (,), periods (.), questions marks (?), and others! @2023 #NLP

Clean Text: Hello This text contains commas  periods  questions marks  and others 2023 NLP
"""