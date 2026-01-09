📚 Book Recommendation System (Collaborative Filtering)

This project is an AI-powered Book Recommendation System built using Collaborative Filtering and Cosine Similarity. It analyzes user–book interaction data to recommend books that are most similar to a selected book based on reader behavior.

The system is deployed as an interactive web application using Streamlit, allowing users to browse popular books and receive personalized book recommendations with cover images, author details, and ratings.

🚀 Features

🔥 Top Popular Books Page
Displays the most popular books based on user ratings and engagement.

🔍 Book Recommendation Engine
Users can search or select a book and receive similar book recommendations using collaborative filtering.

📊 Similarity-Based Matching
Uses Cosine Similarity on a User–Book rating matrix to find books with similar reading patterns.

🖼️ Visual Interface
Shows book cover images, author names, and ratings for an enhanced user experience.

⚡ Fast & Lightweight
Pre-trained similarity matrices are stored using pickle for quick inference.

🧠 How It Works

A User–Book interaction matrix is created using pivot tables.

Cosine similarity is computed between all books.

When a user selects a book, the system retrieves the most similar books based on reader behavior.

Results are displayed in a modern web UI built with Streamlit.

🛠️ Tech Stack

Python

Pandas & NumPy

Scikit-learn

Streamlit

Pickle
