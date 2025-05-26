import pandas as pd

# Load the movie list
movies = pd.read_pickle('artifacts/movie_list.pkl')

# Print the structure of the DataFrame
print(movies.head())
print(movies.columns)
