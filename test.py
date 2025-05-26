import pickle
import streamlit as st
from PIL import Image

# Mock data for movie posters
mock_posters = {
    1452: "https://image.tmdb.org/t/p/w500/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg",
    278: "https://image.tmdb.org/t/p/w500/d8tuQnsr2lfuKooF98PdwuUkI0o.jpg",
    2978: "https://image.tmdb.org/t/p/w500/6X2YjjdfVwWqY7fx9T8EEtHtD2B.jpg",
    246655: "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8EkB8CB4qYaEcM.jpg",
    49026: "https://image.tmdb.org/t/p/w500/5N20RdWtaC1fbTyesXBowO2tTNX.jpg",
    155: "https://image.tmdb.org/t/p/w500/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg",
    157: "https://image.tmdb.org/t/p/w500/d8tuQnsr2lfuKooF98PdwuUkI0o.jpg",
    158: "https://image.tmdb.org/t/p/w500/6X2YjjdfVwWqY7fx9T8EEtHtD2B.jpg",
    159: "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8EkB8CB4qYaEcM.jpg",
    160: "https://image.tmdb.org/t/p/w500/5N20RdWtaC1fbTyesXBowO2tTNX.jpg"
}

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id  # Use the correct column name
        recommended_movie_posters.append(mock_posters.get(movie_id, "https://via.placeholder.com/500"))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

st.header('Movie Recommender System Using Machine Learning')
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])