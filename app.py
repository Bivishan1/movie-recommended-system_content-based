import streamlit as st
import pickle
import pandas as pd
import requests # to hit the api key

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&language=en-US'.format(movie_id))
    data = response.json() #converting response into json and storing response into data.
    return "https://image.tmdb.org/t/p/original/" +data['poster_path'] #returning poster path means returning image of the movie poster.



def recommend(movie):

    movie_index = movies[movies['title']== movie].index[0]  #dataframe is movies.
    distances = similarity[movie_index] # we don't have similarity metrix, so now we need to dump pickley with simlarity.pkl in jupyter line 
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1:6] #pickle the dump
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id #fetching id from movie (which can be see in jupyter line 209 and 210) id which is here i ko 0th item, means first movie ko id. i here is every single row of movies list.

        # Now, fetching poster from api i.e. tmdb website and passing id to it.

        recommended_movies.append((movies.iloc[i[0]].title)) # appending movies into the list.

        #fetching poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters # returning 5 movies if i pass an input one single movie name as parameter.
    

#movies_list = pickle.load((open('movies.pkl','rb')))
movies_dict = pickle.load(open('movi_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

#similarity function to import
similarity = pickle.load(open('similarity.pkl','rb'))


# movies_list = movies_list['title'].values

st.title("Movie Recommend System")

selected_movie_name = st.selectbox (
'How would you like to be contacts?',
movies['title'].values)

# Button 
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name) #storing both names and posters from function.
    # for i in recommendations:
    #     st.write(i)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

        

