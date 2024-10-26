# streamlit run main.py
import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
details= pickle.load(open("detailsview.pkl", 'rb'))
movies_list=movies['title'].values
st.header("Movie Recommendation System");

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=1755167c14eee5632fe796d5b867e7e5".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

import streamlit.components.v1 as components
imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")
imageUrls = [
    fetch_poster(19404),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(360814),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(20453),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
    ]
imageCarouselComponent(imageUrls=imageUrls, height=200)
selectvalue=st.selectbox("Select a movie from dropdown menu", movies_list)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    recommend_overview=[]
    recommend_genres=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_overview.append(details.iloc[i[0]].overview)
        recommend_genres.append(details.iloc[i[0]].genre)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster, recommend_overview, recommend_genres

if st.button("Show Recommend"):
    movie_name, movie_poster, movie_overview, movie_genre = recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
        with st.expander("Learn More"):
            st.write(movie_overview[0])
            st.write(movie_genre[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
        with st.expander("Learn More"):
            st.write(movie_overview[1])
            st.write(movie_genre[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
        with st.expander("Learn More"):
            st.write(movie_overview[2])
            st.write(movie_genre[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
        with st.expander("Learn More"):
            st.write(movie_overview[3])
            st.write(movie_genre[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
        with st.expander("Learn More"):
            st.write(movie_overview[4])
            st.write(movie_genre[4])


