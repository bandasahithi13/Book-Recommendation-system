import pickle
import os
import gdown

import streamlit as st
import pickle
import numpy as np

# ---------------- DOWNLOAD FILES ---------------- #

def download_file(file_id, output):
    if not os.path.exists(output):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output, quiet=False)

# books.pkl
download_file(
    "1Ov25KoyDtnghYfs_P6reyofLs7ekcm4E",
    "books.pkl"
)

# pivot_table.pkl
download_file(
    "16ZlZNRqi25eFQlcy-BQeP0Z_7MiyNMRk",
    "pivot_table.pkl"
)

# svd_similarity.pkl
download_file(
    "1X8bLm1Lt9yGf4YcOnC86nvAAZjEVAyEK",
    "svd_similarity.pkl"
)

# ---------------- LOAD PICKLE FILES ---------------- #

books = pickle.load(
    open('books.pkl','rb')
)

pivot_table = pickle.load(
    open('pivot_table.pkl','rb')
)

svd_similarity = pickle.load(
    open('svd_similarity.pkl','rb')
)

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide"
)

# ---------------- LOAD FILES ---------------- #

books = pickle.load(open('books.pkl', 'rb'))
pivot_table = pickle.load(open('pivot_table.pkl', 'rb'))
svd_similarity = pickle.load(open('svd_similarity.pkl', 'rb'))

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Background */

.stApp{
background:
linear-gradient(
rgba(0,0,0,0.75),
rgba(0,0,0,0.75)
),
url("https://images.unsplash.com/photo-1521587760476-6c12a4b040da");

background-size: cover;
background-position: center;
background-attachment: fixed;
}

/* Title */

.main-title{
text-align:center;
font-size:60px;
font-weight:bold;
color:#FFD700;
padding-top:10px;
}

/* Subtitle */

.subtitle{
text-align:center;
font-size:22px;
color:white;
margin-bottom:30px;
}

/* Search Label */

.search-title{
color:white;
font-size:28px;
font-weight:bold;
text-align:center;
margin-top:20px;
}

/* Select Box */

.stSelectbox div[data-baseweb="select"]{
background:white !important;
border-radius:12px !important;
color:black !important;
font-size:18px !important;
}

/* Button */

.stButton > button{
width:100%;
height:60px;

background:linear-gradient(
90deg,
#ff6b6b,
#feca57
);

color:black !important;
font-size:22px !important;
font-weight:bold !important;

border:none !important;
border-radius:12px !important;
}

.stButton > button:hover{
background:linear-gradient(
90deg,
#48dbfb,
#1dd1a1
);
color:white !important;
}

/* Selected Book */

.selected-title{
color:#FFD700;
font-size:30px;
font-weight:bold;
}

.author{
color:white;
font-size:20px;
}

/* Recommendation Cards */

.card{
background:white;
padding:15px;
border-radius:15px;
box-shadow:0px 8px 20px rgba(0,0,0,0.4);
text-align:center;
min-height:250px;
transition:0.3s;
}

.card:hover{
transform:scale(1.05);
}

.score{
color:green;
font-weight:bold;
font-size:18px;
}

/* Footer */

.footer{
text-align:center;
color:white;
font-size:18px;
margin-top:40px;
padding-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.markdown("""
<div class="main-title">
📚 Book Recommendation System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Find your next favorite book based on your current reads!
</div>
""", unsafe_allow_html=True)

# ---------------- RECOMMENDATION FUNCTION ---------------- #

def recommend_svd(book_name, n=5):

    if book_name not in pivot_table.index:
        return []

    idx = np.where(
        pivot_table.index == book_name
    )[0][0]

    similar_books = sorted(
        list(enumerate(svd_similarity[idx])),
        key=lambda x: x[1],
        reverse=True
    )[1:n+1]

    recommendations = []

    for i in similar_books:

        recommended_book = pivot_table.index[i[0]]

        temp_df = books[
            books['Book-Title'] == recommended_book
        ]

        recommendations.append({

            'title':
            temp_df['Book-Title'].values[0],

            'author':
            temp_df['Book-Author'].values[0],

            'image':
            temp_df['Image-URL-M'].values[0],

            'amazon':
            temp_df['Amazon_Link'].values[0],

            'score':
            round(i[1], 3)

        })

    return recommendations

# ---------------- SEARCH ---------------- #

st.markdown("""
<div class="search-title">
🔍 Search Your Favourite Book
</div>
""", unsafe_allow_html=True)

selected_book = st.selectbox(
    "",
    sorted(pivot_table.index)
)

# ---------------- SELECTED BOOK ---------------- #

selected_df = books[
    books['Book-Title'] == selected_book
]

st.write("")

st.markdown("""
<h2 style='color:white'>
📖 Selected Book
</h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,3])

with col1:

    st.image(
        selected_df['Image-URL-M'].values[0],
        width=260
    )

with col2:

    st.markdown(
        f"""
        <div class="selected-title">
        {selected_book}
        </div>

        <br>

        <div class="author">
        ✍️ Author:
        {selected_df['Book-Author'].values[0]}
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- BUTTON ---------------- #

st.write("")
st.write("")

if st.button("🚀 Get Recommendations"):

    recommendations = recommend_svd(
        selected_book,
        5
    )

    st.markdown("""
    <h2 style='color:white'>
    📚 Recommended Books
    </h2>
    """, unsafe_allow_html=True)

    cols = st.columns(5)

    for idx, book in enumerate(recommendations):

        with cols[idx]:

            st.image(
                book['image'],
                use_container_width=True
            )

            st.markdown(
                f"""
                <div class="card">

                <h4>
                {book['title']}
                </h4>

                <p>
                {book['author']}
                </p>

                <p class="score">
                Similarity Score:
                {book['score']}
                </p>

                <a href="{book['amazon']}"
                target="_blank">
                🛒 Buy on Amazon
                </a>

                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------- FOOTER ---------------- #

st.markdown("""
<div class="footer">

Built with ❤️ using SVD Collaborative Filtering

</div>
""", unsafe_allow_html=True)
