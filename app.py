import streamlit as st
import pickle
import requests

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=d38cc7c0100b2aff332d099996393bee".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list=movies['title'].values

st.header("Movie Recommender System")

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

imageUrls = [
    fetch_poster(504253), #iwteyp
    fetch_poster(357786), #kizu1
    fetch_poster(635302), #mugentrain
    fetch_poster(299534), #endgame
    fetch_poster(896499), #fruitsbasketprelude
    fetch_poster(634649), #spidermannwh
    fetch_poster(572154), #rascalbunnygirl
    fetch_poster(155), #darkknight
    fetch_poster(428707), #kurokolastgame
    fetch_poster(505642), #wakandaforever
    fetch_poster(810693), #jjk0
    fetch_poster(284052), #doctorstrange
    fetch_poster(820067), #quintq
    fetch_poster(569094)  #spiderverse
   ]

imageCarouselComponent(imageUrls=imageUrls, height=250)
selectValue = st.selectbox("Select movie from dropdown", movies_list)
    
def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append((movies.iloc[i[0]].title))
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

if st.button("Show Recommended"):
    movie_name, movie_poster=recommend(selectValue)
    col1, col2, col3, col4, col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])        
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
