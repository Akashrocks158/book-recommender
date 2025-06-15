import streamlit as st
import pandas as pd
import pickle
from recommend import recommend
from fetch_cover import fetch_cover

df = pd.read_csv("books.csv")
similarity = pickle.load(open("book_similarity.pkl", "rb"))

st.set_page_config(page_title="Book Recommender", layout="wide")
st.title("📚 Book Recommender System")

search = st.text_input("🔍 Search for a book title")

filtered_titles = df[df["Title"].str.lower().str.contains(search.lower())]["Title"].values

if len(filtered_titles) > 0:
    selected_book = st.selectbox("Matching books:", filtered_titles)

    if st.button("Recommend"):
        recommendations = recommend(selected_book)
        st.subheader("📖 Recommended Books:")
        cols = st.columns(5)
        for i, book in enumerate(recommendations):
            with cols[i]:
                st.image(fetch_cover(book), width=150)
                st.caption(book)
elif search != "":
    st.warning("No matching books found. Try another title.")
