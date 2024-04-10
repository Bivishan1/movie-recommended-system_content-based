**Movie Recommendation System**

This Python script is a Content Based Movie Recommendation System built using Streamlit, a web application framework for creating data-driven web applications.

**How it works:**

1. The script loads precomputed data from pickle files (movi_dict.pkl and similarity.pkl) containing movie information and similarity scores between movies.

2. It defines a function fetch_poster(movie_id) that fetches the movie poster image from the TMDB API based on the movie ID.

3. Another function recommend(movie) takes a movie title as input and returns a list of recommended movies along with their poster images. It uses the similarity scores between movies to find similar movies to the input movie.

4. The Streamlit application displays a title "Movie Recommendation System" and provides a dropdown menu (selectbox) where users can select a movie from the available options.

5. Upon clicking the "Recommend" button, the script calls the recommend() function with the selected movie title and displays the top 5 recommended movies along with their poster images.

**How to Use:**

1. Ensure you have the necessary pickle files (movi_dict.pkl and similarity.pkl) containing movie data and similarity scores.

2. Run the script using Streamlit.

3. Select a movie from the dropdown menu.

4. Click the "Recommend" button to see the top 5 recommended movies.

**Tools**
- Python 3.4 or higher installed
- Jupyter notebook

**Note:**

The movie recommendation algorithm is based on the similarity between movies calculated using precomputed similarity scores.
The poster images are fetched dynamically from the TMDB API, so an active internet connection is required for image retrieval.

**Dependencies:**

Streamlit
Pandas
Requests

Author:
This script was created by Bivishan.

Disclaimer:
This script is provided for educational purposes only. It may require additional customization or modifications to work with your specific environment or data. Use it responsibly and ensure compliance with all applicable terms of service and data usage policies.
