import pickle
import numpy as np
import pandas as pd

book_names = pickle.load(open("book_names.pkl", "rb"))
similarity_scores = pickle.load(open("similarity_scores.pkl", "rb"))
books = pickle.load(open("books.pkl", "rb"))


def recommend(book_name):
    # case insensitive match
    book_name = book_name.lower()
    book_names_lower = np.array([b.lower() for b in book_names])

    matches = np.where(book_names_lower == book_name)[0]

    if len(matches) == 0:
        return None

    index = matches[0]

    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    data = []

    for i in similar_items:
        temp = books[books['Book-Title'] == book_names[i[0]]]
        if not temp.empty:
            book = temp.iloc[0]
            data.append({
                "Book-Title": book["Book-Title"],
                "Book-Author": book["Book-Author"],
                "Image-URL-M": book["Image-URL-M"],
                "avg_rating": book.get("avg_rating", 0)
            })

    if len(data) == 0:
        return None

    return pd.DataFrame(data)
