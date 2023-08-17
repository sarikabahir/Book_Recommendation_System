import streamlit as st
import pickle
import numpy as np
def recommend_book(book):
    index = np.where(pt.index==book)[0][0]
    similar_books = sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1],reverse=True)[1:6]
    
    data = []
    for i in similar_books:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
    return data
st.header("Book Recommender System")
popular = pickle.load(open('Top50Book.pkl','rb'))
books = pickle.load(open('Boooks.pkl','rb'))
pt = pickle.load(open('Pvt.pkl','rb'))
similarity_score = pickle.load(open('Similar.pkl','rb'))

book_list = pt.index.values
image_url = popular['Image-URL-M'].tolist()
book_title = popular['Book-Title'].tolist() 
book_author = popular['Book-Author'].tolist()
total_ratings = popular['num_ratings'].tolist()
avg_ratings = popular['avg_ratings'].tolist()

st.sidebar.title("Top 20 Books")
if st.sidebar.button("SHOW"):
    num_rows = 20
    num_columns = 5
    for row in range(0, num_rows, num_columns):## loop iterates over rows, each time considering a group of num_columns books.
        cols = st.columns(num_columns) ##This creates a group of columns, each representing a book.
        for col in cols:
            index = row + cols.index(col)
            with col:
                st.image(image_url[index])
                st.text(book_author[index])
                st.text("Ratings:" + str(total_ratings[index]))
                st.text("Avg.Rating:" + str(round(avg_ratings[index], 2)))
st.sidebar.title("Recommend Books")
selected_book = st.sidebar.selectbox("Type or select a book from the dropdown", book_list)

if st.sidebar.button("Recommend Me"):
    moviee = recommend_book(selected_book)
    
    num_recommendations = 5
    num_columns = 5

    for i in range(0, num_recommendations, num_columns):
        cols = st.columns(num_columns)
        
        for col, recommendation in zip(cols, moviee[i:i+num_columns]):
            with col:
                st.image(recommendation[2])
                st.text(recommendation[0])
                st.text(recommendation[1])
