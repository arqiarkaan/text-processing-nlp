# word_frequency.py
from collections import Counter
import pandas as pd

def count_word_frequency(text):
    """Menghitung kemunculan tiap kata dalam teks"""
    words = text.split()
    return pd.DataFrame.from_dict(
        Counter(words), 
        orient='index', 
        columns=['Frequency']
    ).sort_values('Frequency', ascending=False)

sample_text = "Text analysis is important for understanding data. Data analysis helps in text understanding. Text 👍"

print("Original Text:")
print(sample_text)

clean_text = sample_text.lower().replace('.', '')
df = count_word_frequency(clean_text)

print("\nWord Frequencies:")
print(df)

"""
Output yang diharapkan:

           Frequency
text              3
analysis          2
data              2
is                1
important         1
...
"""