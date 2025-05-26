import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
file_path = "tmdb_5000_movies.csv"
movies = pd.read_csv(file_path)

# Preprocess the data
movies['genres'] = movies['genres'].apply(lambda x: x.replace("'", "").replace('"', '').split(', '))
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(movies['genres'].apply(lambda x: ' '.join(x)))

# Create a similarity matrix
similarity = cosine_similarity(tfidf_matrix)

# Save the processed data
movies.to_pickle('artifacts/movie_list.pkl')
pickle.dump(similarity, open('artifacts/similarity.pkl', 'wb'))

print("Models generated successfully!")
