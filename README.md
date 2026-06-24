# 📚 Book Recommendation System

## Overview

This project is a Machine Learning-based Book Recommendation System developed using the Book-Crossing Dataset. The system recommends books to users based on their rating patterns and reading preferences.

The project implements multiple recommendation techniques including:

* Cosine Similarity
* KNN Collaborative Filtering
* SVD Collaborative Filtering
* Content-Based Filtering
* Hybrid Recommendation System

After comparing all models, **SVD Collaborative Filtering** achieved the best performance and was selected as the final deployed model.

---

## Dataset

The project uses three datasets:

### Users.csv

Contains user information such as:

* User-ID
* Location
* Age

### Books.csv

Contains book information such as:

* ISBN
* Book Title
* Author
* Publisher
* Cover Image URLs

### Ratings.csv

Contains user ratings:

* User-ID
* ISBN
* Book-Rating

---

## Final Model

The deployed model uses **SVD (Singular Value Decomposition) Collaborative Filtering** to generate book recommendations.

---

## Streamlit Features

* Search Book
* View Selected Book Cover
* Top Book Recommendations
* Similarity Scores
* Amazon Purchase Links
* Interactive User Interface

---

## Important Note About .pkl Files

The application requires the following files:

* books.pkl
* pivot_table.pkl
* svd_similarity.pkl

These files may not be included in the GitHub repository because GitHub has file size limitations for large binary files.

If the `.pkl` files are missing, run the notebook to regenerate them before starting the application.

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Streamlit

---

## Author

Sahithi Banda
