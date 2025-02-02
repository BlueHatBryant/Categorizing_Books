import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    """Preprocess text: remove special characters, convert to lowercase, and remove stopwords."""
    text = re.sub(r'\W+', ' ', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    words = text.split()
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    return " ".join(words)

def load_and_preprocess(file_path):
    """Loads dataset, preprocesses text, and applies TF-IDF vectorization."""
    df = pd.read_excel(file_path)
    
    # Apply text cleaning to the 'Description' column
    df["Clean_Description"] = df["Description"].astype(str).apply(clean_text)

    # TF-IDF Vectorization with better filtering
    vectorizer = TfidfVectorizer(max_df=0.85, min_df=2, stop_words="english")
    X = vectorizer.fit_transform(df["Clean_Description"])

    return df, X, vectorizer
