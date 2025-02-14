import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def remove_stopwords(text):
    """Menyaring kata-kata umum yang kurang bermakna"""
    english_stopwords = set(stopwords.words('english'))
    words = text.split()
    return ' '.join([word for word in words if word not in english_stopwords])

sample_text = "This is a sample sentence showing the process of removing stopwords"

print("Original Text:")
print(sample_text)
filtered_text = remove_stopwords(sample_text)
print("\nFiltered Text:")
print(filtered_text)

"""
Output yang diharapkan:

Original Text: This is a sample sentence showing the process of removing stopwords

Filtered Text: This sample sentence showing process removing stopwords
"""