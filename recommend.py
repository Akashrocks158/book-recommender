
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

df = pd.read_csv("books.csv")
df.fillna("", inplace=True)
df["combined"] = df["Title"] + " " + df["Author"] + " " + df["Genre"] + " " + df["Summary"]

vectorizer = TfidfVectorizer(stop_words='english')
vectors = vectorizer.fit_transform(df["combined"])
similarity = cosine_similarity(vectors)

# Save for future use
pickle.dump(similarity, open("book_similarity.pkl", "wb"))

def recommend(book_title):
    if book_title not in df["Title"].values:
        return []
    index = df[df["Title"] == book_title].index[0]
    scores = list(enumerate(similarity[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    recommended_books = [df.iloc[i[0]]["Title"] for i in sorted_scores]
    return recommended_books
