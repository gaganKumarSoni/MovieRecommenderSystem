import pickle
import streamlit as st
import requests

movi = pickle.load(open('mov.pkl', 'rb'))
siml = pickle.load(open('sim.pkl', 'rb'))

def fetch_poster(id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(id)
    data = requests.get(url).json()
    return "https://image.tmdb.org/t/p/w185/"+data['poster_path']

def recomend(mov): 
    df_ind = movi[movi.title==mov].index[0]
    sim_movi = sorted(list(enumerate(siml[df_ind])), reverse=True, key=lambda x:x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in sim_movi[1:7]:
        recommended_movie_names.append(movi.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movi.iloc[i[0]].id))
    return recommended_movie_names, recommended_movie_posters

st.header('Movie Recommender System')
mvlist = movi["title"].values
selected_movie = st.selectbox("Type or select movie from dropdown", mvlist)
if st.button("Recommend Movie"):
    name, poster = recomend(selected_movie)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    col4, col5, col6 = st.columns(3)
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])
    with col6:
        st.text(name[5])
        st.image(poster[5])