from spellchecker import SpellChecker

def fix_spelling(text):
    """Memperbaiki kesalahan ketik dalam teks"""
    spell = SpellChecker()
    words = text.split()
    corrected = [spell.correction(word) for word in words]
    return ' '.join(filter(None, corrected))

sample_text = "Ths is an exmple of text with spelingg errrors"

print("Original Text:")
print(sample_text)
corrected_text = fix_spelling(sample_text)
print("\nCorrected Text:")
print(corrected_text)

"""
Output yang diharapkan:

Original Text: Ths is an exmple of text with spelingg errrors

Corrected Text: the is an example of text with spelling errors
"""