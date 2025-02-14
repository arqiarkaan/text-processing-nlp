## 🛠️ Setup Project

### 1. Buat Virtual Environment
```bash
python -m venv .venv
venv\Scripts\activate
```
```bash
venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download Resources Tambahan
```bash
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt stopwords
```

## 📂 Struktur Folder
```
text-processing-nlp/
├── .venv/                 
├── src/                 
│   ├── lowercase.py        
│   ├── tokenizing.py       
│   └── ...                 
├── requirements.txt        
└── README.md               
```

## 💻 Requirements
- Python > 3.7 && < 3.13
