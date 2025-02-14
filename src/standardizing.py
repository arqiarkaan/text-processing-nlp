import re

def standardize_text(text):
    """Membersihkan dan merapikan format teks"""
    text = re.sub(r'http\S+', '', text)  # Hapus URL
    text = re.sub(r'@\w+', '', text)     # Hapus mention
    text = re.sub(r'[^\w\s]', '', text)  # Hapus karakter khusus
    text = re.sub(r'\d+', '', text)      # Hapus angka
    text = ' '.join(text.split())        # Merapikan spasi
    return text.lower()

sample_text = "@user: Check this cool project https://example.com!!! 2025 BEST AI PROJECT!!! 100%   SUCCESS!!! 😎😎😎😎"

print("Original Text:")
print(sample_text)
standardized_text = standardize_text(sample_text)
print("\nStandardized Text:")
print(standardized_text)

"""
Output yang diharapkan:

Original Text: RT @user: Check this cool project https://example.com!!! 2025 BEST AI PROJECT!!! 100%   SUCCESS!!! 😎😎😎😎

Standardized Text: check this cool project best ai project success
"""