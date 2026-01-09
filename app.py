import streamlit as st
import pickle
from recommender import recommend

# ---------------- Page Config ----------------
st.set_page_config(page_title="Book Recommendation", layout="wide")

st.title("📚 Book Recommendation System")

# ---------------- Load Data ----------------
book_names = pickle.load(open("book_names.pkl", "rb"))
popular = pickle.load(open("popular.pkl", "rb"))   # top books dataframe

# ---------------- Sidebar Menu ----------------
menu = st.sidebar.radio("Menu", ["Top Books", "Recommend"])

# =========================================================
# 🔵 PAGE 1 : TOP POPULAR BOOKS
# =========================================================
if menu == "Top Books":
    st.subheader("🔥 Top Popular Books")

    total = len(popular)

    for i in range(0, total, 5):
        cols = st.columns(5)

        for j in range(5):
            idx = i + j
            if idx < total:
                book = popular.iloc[idx]
                with cols[j]:
                    st.image(book["Image-URL-M"])
                    st.text(book["Book-Title"])
                    st.text(book["Book-Author"])


# =========================================================
# 🔴 PAGE 2 : RECOMMENDATION (Your Exact Logic)
# =========================================================
if menu == "Recommend":

    st.subheader("🔍 Find Similar Books")

    book_input = st.selectbox("Enter or select a book:", book_names)

    if st.button("Recommend"):
        recommendations = recommend(book_input)

        if recommendations is None or len(recommendations) == 0:
            st.error("❌ Book not found or no similar books available.")
        else:
            st.subheader("📖 Recommended Books")

            total = len(recommendations)

            for i in range(0, total, 5):
                cols = st.columns(5)

                for j in range(5):
                    idx = i + j
                    if idx < total:
                        book = recommendations.iloc[idx]

                        with cols[j]:
                            st.image(book["Image-URL-M"])
                            st.text(book["Book-Title"])
                            st.text(book["Book-Author"])
