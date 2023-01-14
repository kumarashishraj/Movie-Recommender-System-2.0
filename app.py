import streamlit as st
import pandas as pd
import pickle
import requests

API_key = '72cf47d64d785bdac488491d7c41af28'



def get_poster (movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key='.format(movie_id) + API_key + '&language=en-US'
    response = requests.get(url)
    data = response.json()
    #print (data)
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


def recommend (movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_list = list(sorted(enumerate(similarity[movie_index]), reverse = True, key = lambda x: x[1]))[0:6]
    l = []
    poster = []
    
    for final in movie_list:
        l.append(movies.iloc[final[0]].title)
        
        ## we need to get the posters from the API calls ## we need to get the posters from the API calls 
        m_id = movies.iloc[final[0]].id
        #print (m_id)
        
        poster.append(get_poster(m_id))
        
    return l, poster

def moviedetails (movie):
    selfmovieid = movies[movies['title'] == movie].id
    st.text (selfmovieid)
    #selfposter =  get_poster (selfmovieid[0])
    
    #st.image(selfposter)
    
    
    
movies_dict = pickle.load(open('movie_dictionary.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame (movies_dict)



st.title ('Movie Recommender System')

movie_selected = st.selectbox(
'Pick a movie',
movies['title'].values)

if st.button('Recommend'):
    reco, poster = recommend(movie_selected)
    
    column1, column2 = st.columns(2)
    with column1:
        st.image (poster [0], width = 150)
    with column2:
        st.header (movie_selected)
        
        
        
    
    
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    
    
    
    
    
    with col1:
       st.text(reco[1])
       st.image(poster[1])
    
    with col2:
       st.text(reco[2])
       st.image(poster[2])
    
    with col3:
       st.text(reco[3])
       st.image(poster[3])
       
    with col4:
       st.text(reco[4])
       st.image(poster[4])
    
    with col5:
       st.text(reco[5])
       st.image(poster[5])
       

    
    
       