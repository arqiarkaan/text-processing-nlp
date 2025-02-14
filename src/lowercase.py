def convert_to_lowercase(text):
    """Mengonversi teks ke huruf kecil semua"""
    return text.lower()

sample_text = "Python Programming is FUN! Let's try NLP with 123 Examples & @Symbols."

print("Original Text:")
print(sample_text)
print("\nLowercase Text:")
result = convert_to_lowercase(sample_text)
print(result)

"""
Output yang diharapkan:

Original Text: Python Programming is FUN! Let's try NLP with 123 Examples & @Symbols.

Lowercase Text: python programming is fun! let's try nlp with 123 examples & @symbols.
"""